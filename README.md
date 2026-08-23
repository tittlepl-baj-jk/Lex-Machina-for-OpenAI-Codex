<!-- Autor: [CODEX] | Utworzony: 2026-08-23 -->

# Lex Machina for OpenAI Codex

Nieoficjalny port projektu **Lex Machina** na środowisko OpenAI Codex.

Projekt pierwotny został stworzony przez **Michała Wiatraka** i jest dostępny
w repozytorium:
<https://github.com/michaleiatrak-star/Lex-Machina>

Ten port zachowuje autorstwo projektu pierwotnego. Nie jest nową, niezależną
implementacją ani oficjalnym produktem autora wersji pierwotnej, OpenAI lub
Anthropic.

Inicjator i opiekun portu: **Jacek Kurzawa (Jack BAI EMM System)** — profil
GitHub: **tittlepl-baj-jk**.

## Status

- 32 aktywne skille dla Codex;
- bazowy upstream: commit `3fb42870299738b065cae888ec5526a405fa8f5d`;
- statyczna walidacja portu: 32/32 `PASS`;
- pakiet jest portem skilli Codex, a nie samodzielną aplikacją ChatGPT ani
  publikacją w katalogu GPT lub Apps.

## Najważniejsze zmiany względem upstream

- mapowanie operacji Claude/Cowork na narzędzia Codex;
- zastąpienie historycznych ścieżek `/mnt/skills/user/` ścieżkami przenośnymi;
- wyłączenie bezpośrednich wywołań Anthropic API;
- lokalna, deterministyczna anonimizacja jako domyślny bezpieczny tryb;
- adapter degradacji funkcji niedostępnych w środowisku Codex;
- poprawki martwych i historycznych odwołań wskazane w `manifest.json`.

Pełne informacje o pochodzeniu znajdują się w [UPSTREAM.md](UPSTREAM.md),
o autorstwie w [AUTHORS.md](AUTHORS.md), a o modyfikacjach w
[CHANGELOG.md](CHANGELOG.md).

Każdy push i pull request jest kontrolowany przez GitHub Actions za pomocą
przenośnego walidatora `scripts/validate_port.py`.

## Instalacja w projekcie Codex

1. Sklonuj lub pobierz repozytorium.
2. Skopiuj wybrane katalogi z `skills/` do `.agents/skills/` projektu Codex.
3. Zachowaj katalog `shared/` oraz strukturę zależności wskazaną przez router.
4. Uruchom walidację statyczną przed wykorzystaniem skilli.
5. Pierwsze testy wykonuj wyłącznie na danych fikcyjnych.

Nie umieszczaj w repozytorium kluczy API, akt spraw ani danych osobowych.
Zasady prywatnego zgłaszania podatności opisuje [SECURITY.md](SECURITY.md).

## Aktualizacje z projektu pierwotnego

Projekt Michała Wiatraka pozostaje źródłem upstream. Aktualizacja portu powinna
przebiegać według procedury z [UPSTREAM.md](UPSTREAM.md) i kończyć się kontrolą
z [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md).

Zalecane zdalne repozytoria Git:

```text
origin   -> repozytorium tego portu
upstream -> https://github.com/michaleiatrak-star/Lex-Machina.git
```

## Licencja

Całość jest rozpowszechniana na warunkach GNU General Public License version 3.
Pełna treść znajduje się w [LICENSE](LICENSE).

Prawa do projektu pierwotnego pozostają przy Michale Wiatraku i ewentualnych
pozostałych uprawnionych współtwórcach. Prawa do nowych, twórczych modyfikacji
pozostają przy ich autorach, przy czym cały rozpowszechniany port podlega GPLv3.

`SPDX-License-Identifier: GPL-3.0-only`

## Brak gwarancji i zastrzeżenie

Projekt jest udostępniany bez gwarancji. Lex Machina wspiera pracę ze źródłami
prawnymi, lecz nie zastępuje profesjonalnej porady prawnej ani samodzielnej
weryfikacji przepisów, orzeczeń i dokumentów.
