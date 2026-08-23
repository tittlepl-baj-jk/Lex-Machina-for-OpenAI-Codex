<!-- Autor: [CODEX] | Utworzony: 2026-08-23 -->

# Changelog

Wszystkie istotne zmiany portu będą dokumentowane w tym pliku. Zmiany przejęte
z upstream są odróżniane od zmian przygotowanych specjalnie dla Codex.

## [Unreleased]

### Planowane

- kontrolowana aktualizacja z „Wersji rozwojowej” upstream, zamrożonej na
  commicie `9e37d6092f84b5f1a2fe41717e07611de062951a`;
- test regresji procesu aktualizacji i wydanie `v0.2.0-codex` po przejściu
  checklisty publikacyjnej.

## [0.1.0] - 2026-08-23

### Upstream

- utworzono port z projektu Lex Machina, commit bazowy
  `3fb42870299738b065cae888ec5526a405fa8f5d`;
- zachowano 32 aktywne skille i ich strukturę zależności.

### Codex port

- dodano adapter operacji Claude/Cowork do Codex;
- zastąpiono historyczne ścieżki `/mnt/skills/user/`;
- wyłączono bezpośrednie wywołania Anthropic API;
- wprowadzono bezpieczne fallbacki dla funkcji niedostępnych w Codex;
- poprawiono wskazane w `manifest.json` martwe odwołania;
- wykonano statyczną walidację 32/32 skilli z wynikiem `PASS`.
- wykonano fikcyjny test integracyjny K1–K5 z wynikiem `PASS`;
- zanonimizowano osobisty e-mail i realistyczne przykłady PESEL oraz dodano
  trwałą kontrolę potencjalnych sekretów i identyfikatorów;
- poprawiono międzyplatformową walidację licencji przez normalizację CRLF/LF.

### Dokumentacja i licencja

- dodano `LICENSE`, `README.md`, `NOTICE.md`, `AUTHORS.md`, `UPSTREAM.md`,
  `CONTRIBUTING.md`, `SECURITY.md` i `RELEASE_CHECKLIST.md`;
- oznaczono port jako nieoficjalne dzieło pochodne na GPLv3;
- zapisano autorstwo Michała Wiatraka i bazowy commit upstream.
- dodano przenośny walidator publikacyjny i workflow GitHub Actions.
- opublikowano publiczne repozytorium i tag `v0.1.0-codex`.
