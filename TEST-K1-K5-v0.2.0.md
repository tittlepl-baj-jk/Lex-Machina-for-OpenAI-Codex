<!-- Autor testu portu: Jacek Kurzawa (Jack BAI EMM System) / [CODEX] -->

# Regresja kontraktu K1-K5 — v0.2.0-codex

Data: 2026-08-23

Scenariusz: fikcyjna osoba zawarła umowę o usługę, zgłasza wadliwe wykonanie,
ale nie przekazuje umowy, reklamacji ani dowodów. Test wykonano bez internetu,
zewnętrznych API i dokumentów użytkownika.

## Wynik

| Kryterium | Wynik | Dowód kontraktowy |
|---|---|---|
| K1 | PASS | Router wskazuje `[1] DOKUMENT / UMOWA` oraz PRIMARY `analizator-umow-v1`. |
| K2 | PASS | HARD GATE wymaga jawnego statusu `NIEWERYFIKOWANE` przy braku odczytu źródła. |
| K3 | PASS | Dry-run rozdzielił fakty podane, założenia, braki danych i obszary weryfikacji. |
| K4 | PASS | Dry-run zawierał routing oraz wszystkie cztery wymagane grupy odpowiedzi. |
| K5 | PASS | Nie podano twierdzeń prawnych z pamięci; źródło ma być przypisane bezpośrednio po jego faktycznym otwarciu. |

Wynik zbiorczy: `PASS`.

## Granica testu

Jest to regresja kontraktu zachowania w aktywnej sesji i kontrola treści portu.
Nie jest to test automatycznego wykrycia skilli po instalacji w całkowicie nowym
zadaniu Codex. Taki test środowiskowy należy powtórzyć po instalacji wydania.

