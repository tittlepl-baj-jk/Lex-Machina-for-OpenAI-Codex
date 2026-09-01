<!-- Autor: [CODEX] | Utworzony: 2026-08-23 -->

# Upstream i synchronizacja

## Źródło pierwotne

- Projekt: **Lex Machina**
- Autor: **Michał Wiatrak**
- Repozytorium: <https://github.com/michaleiatrak-star/Lex-Machina>
- Bazowa gałąź: `main`
- Ostatni zsynchronizowany commit:
  `35cfd9ab388e2eca5544eb45fbaa0a1924dd5429`
- Drzewo źródłowe: `Wersja rozwojowa rozpakowana`
- Data synchronizacji pełnego drzewa: 2026-09-01
- Data utworzenia portu: 2026-08-23

## Konfiguracja Git

```powershell
git remote add upstream https://github.com/michaleiatrak-star/Lex-Machina.git
git fetch upstream
```

`origin` powinien wskazywać repozytorium portu, a `upstream` repozytorium
Michała Wiatraka. Port nie powinien wykonywać automatycznego push do upstream.

## Procedura aktualizacji

1. Pobierz zmiany przez `git fetch upstream`.
2. Porównaj nowy upstream z commitem zapisanym powyżej.
3. Sklasyfikuj zmiany jako:
   - wspólna metodologia i treść prawna;
   - element specyficzny dla Claude/Cowork;
   - element wymagający odpowiednika Codex;
   - zmiana nieprzenoszona do portu wraz z uzasadnieniem.
4. Przenieś właściwe zmiany na osobnej gałęzi `codex/upstream-sync-*`.
5. Zachowaj oryginalne informacje o autorstwie i licencji.
6. Zaktualizuj `CHANGELOG.md`, `manifest.json` i commit w tym pliku.
7. Wykonaj walidację statyczną i testy K1-K5 na danych fikcyjnych.
8. Zastosuj `RELEASE_CHECKLIST.md` przed utworzeniem wydania.

## Konwencja commitów

```text
upstream-sync: zmiany przejęte z Lex Machina
codex-port: adaptacja dla OpenAI Codex
feature: nowa funkcja portu
fix: poprawka portu
docs: dokumentacja i informacje licencyjne
```

Commit przenoszący cudzą zmianę powinien wskazywać autora lub źródłowy commit,
jeżeli jest to technicznie możliwe. Nie należy przepisywać historii tak, aby
zmiana upstream wyglądała jak samodzielnie stworzona w porcie.
