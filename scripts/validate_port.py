#!/usr/bin/env python3
# Autor: [CODEX] | Utworzony: 2026-08-23
"""Portable publication checks for Lex Machina for OpenAI Codex."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED_LICENSE_SHA256 = (
    "230184f60bae2feaf244f10a8bac053c8ff33a183bcc365b4d8b876d2b7f4809"
)
REQUIRED = {
    "LICENSE",
    "README.md",
    "NOTICE.md",
    "AUTHORS.md",
    "UPSTREAM.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "RELEASE_CHECKLIST.md",
    "SECURITY.md",
    "manifest.json",
}
PRIVATE_PATTERNS = (
    rb"D:\\Antigravity",
    rb"C:\\Users",
)
SENSITIVE_PATTERNS = (
    re.compile(rb"PESEL[^\r\n]{0,32}(?<![0-9])[0-9]{11}(?![0-9])", re.IGNORECASE),
    re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(rb"(?:gh[pousr]_|github_pat_)[A-Za-z0-9_]{20,}"),
    re.compile(rb"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}"),
    re.compile(rb"(?<![A-Za-z0-9])AKIA[0-9A-Z]{16}(?![A-Za-z0-9])"),
    re.compile(
        rb"[A-Za-z0-9._%+-]+@(?:gmail\.com|wp\.pl|onet\.pl|interia\.pl|"
        rb"o2\.pl|outlook\.com|hotmail\.com|yahoo\.com)",
        re.IGNORECASE,
    ),
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures: list[str] = []

    missing = sorted(name for name in REQUIRED if not (ROOT / name).exists())
    if missing:
        failures.append(f"missing required files: {', '.join(missing)}")

    try:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        manifest = {}
        failures.append(f"manifest.json is invalid: {exc}")

    if manifest.get("license") != "GPL-3.0-only":
        failures.append("manifest license must be GPL-3.0-only")
    if not re.fullmatch(r"[0-9a-f]{40}", str(manifest.get("source_commit", ""))):
        failures.append("manifest source_commit must be a 40-character Git hash")
    if manifest.get("active_skill_count") != 32:
        failures.append("manifest active_skill_count must equal 32")

    skill_dirs = sorted(
        path for path in SKILLS.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    ) if SKILLS.exists() else []
    names: list[str] = []
    for skill_dir in skill_dirs:
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        match = re.search(r'^name:\s*["\']?([^"\'\n]+)', text, re.MULTILINE)
        if not match:
            failures.append(f"missing skill name: {skill_dir.name}/SKILL.md")
            continue
        names.append(match.group(1).strip())

    if len(skill_dirs) != 32:
        failures.append(f"expected 32 active skills, found {len(skill_dirs)}")
    if len(set(names)) != len(names):
        failures.append("skill names are not unique")

    legacy_paths: list[str] = []
    anthropic_endpoints: list[str] = []
    for path in SKILLS.rglob("*"):
        if not path.is_file():
            continue
        data = path.read_bytes()
        relative = path.relative_to(ROOT).as_posix()
        if b"/mnt/skills/user/" in data:
            legacy_paths.append(relative)
        if b"https://api.anthropic.com" in data:
            anthropic_endpoints.append(relative)

    private_hits: list[str] = []
    sensitive_hits: list[str] = []
    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or ".git" in path.parts
            or path.name == "LICENSE"
            or path.resolve() == Path(__file__).resolve()
        ):
            continue
        data = path.read_bytes()
        relative = path.relative_to(ROOT).as_posix()
        if any(pattern in data for pattern in PRIVATE_PATTERNS):
            private_hits.append(relative)
        if any(pattern.search(data) for pattern in SENSITIVE_PATTERNS):
            sensitive_hits.append(relative)

    if legacy_paths:
        failures.append(f"legacy paths found: {', '.join(legacy_paths)}")
    if anthropic_endpoints:
        failures.append(f"active Anthropic endpoints found: {', '.join(anthropic_endpoints)}")
    if private_hits:
        failures.append(f"private data patterns found: {', '.join(private_hits)}")
    if sensitive_hits:
        failures.append(
            f"potential secrets or personal identifiers found: {', '.join(sensitive_hits)}"
        )

    license_path = ROOT / "LICENSE"
    if license_path.exists() and file_sha256(license_path) != EXPECTED_LICENSE_SHA256:
        failures.append("LICENSE differs from the verified upstream GPLv3 text")

    adapter = SKILLS / "shared" / "CODEX-ADAPTER.md"
    if not adapter.is_file():
        failures.append("Codex adapter is missing")

    result = {
        "pass": not failures,
        "active_skill_count": len(skill_dirs),
        "unique_skill_name_count": len(set(names)),
        "license_sha256": file_sha256(license_path) if license_path.exists() else None,
        "failures": failures,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
