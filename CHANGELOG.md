<!-- Autor: [CODEX] | Utworzony: 2026-08-23 -->

# Changelog

Wszystkie istotne zmiany portu będą dokumentowane w tym pliku. Zmiany przejęte
z upstream są odróżniane od zmian przygotowanych specjalnie dla Codex.

## [Unreleased]

Brak zmian.

## [0.6.0] - 2026-09-18

### Upstream

- wykonano pełną synchronizację z rozwojowym drzewem Lex Machina, commit
  `60faf9695604f438540a2674ec545d5b2250d8b9` projektu Michała Wiatraka;
- przejęto aktualizacje metodologii, routerów, modułów dziedzinowych,
  materiałów audytowych i proweniencji źródeł z tego commitu.

### Codex port

- zbudowano 1292 pliki dla 32 aktywnych skilli; zachowano adapter Codex,
  przenośne ścieżki i zanonimizowane dane kontaktowe;
- walidacja statyczna pakietu zakończyła się wynikiem `PASS` (32/32), a test
  rejestracji modułów i lokalny self-test mock-ELI zakończyły się powodzeniem.

## [0.5.0] - 2026-09-12

### Upstream

- wykonano pełną synchronizację z rozwojowym drzewem Lex Machina, commit
  `05833172bfdef972a8542ca41987c347068fdaaf` projektu Michała Wiatraka;
- przejęto router 3.47, profil lekkiego ładowania zasobów warunkowych oraz
  kontrolę zgodności wersji załadowanej przez hosta z repozytorium;
- przejęto nowe bramki dla aktów prawa miejscowego i kontrolowanej blokady,
  rozszerzone źródła urzędowe, testy nowelizacji po tekście jednolitym oraz
  test pokrycia orkiestratora;
- przejęto aktualizację map i podstaw prawnych, w tym zadeklarowane domknięcie
  listy 61/61 miejsc z przeterminowanymi odwołaniami; statyczny audyt portu
  nie zastępuje niezależnej weryfikacji merytorycznej tych pozycji.

### Codex port

- zbudowano 1266 plików dla 32 aktywnych skilli z adapterem runtime Codex;
- względem `v0.4.0-codex` zsynchronizowano 194 ścieżki skilli: 31 dodano
  i 163 zmieniono;
- walidacja statyczna zakończyła się wynikiem 32/32 `PASS`; brak dawnych
  ścieżek `/mnt/skills/user`, aktywnych endpointów Anthropic i brakujących
  dokładnych celów referencji;
- pełna regresja strukturalna, w tym nowe T22, T23 i mock-ELI, zakończyła się
  `PASS`; T4 i T5 pozostają testami ręcznymi zgodnie z upstreamem.

## [0.4.0] - 2026-09-01

### Upstream

- wykonano pełną synchronizację z rozwojowym drzewem Lex Machina, commit
  `35cfd9ab388e2eca5544eb45fbaa0a1924dd5429` projektu Michała Wiatraka;
- przejęto rozszerzoną analizę przepisu: pełną listę nowelizacji po tekście
  jednolitym, ustalanie właściwego brzmienia na datę analizy, vacatio legis,
  przepisy przejściowe, wyjątki oraz relacje lex specialis także między aktami;
- przejęto aktualizacje map i modułów `current-state-COV` dla 16 dziedzin,
  korekty wartości prawnych oraz materiały audytowe F-108/F-135/F-138;
- router 3.33 przywraca jawny katalog oficjalnych domen orzeczniczych.

### Codex port

- zbudowano 1235 plików dla 32 aktywnych skilli z uniwersalnym adapterem
  runtime i przenośnymi ścieżkami;
- względem `v0.3.1-codex` zsynchronizowano 709 ścieżek skilli: 198 dodano,
  451 zmieniono i 60 usunięto;
- walidacja statyczna zakończyła się wynikiem 32/32 `PASS`; nie pozostały
  ścieżki `/mnt/skills/user`, aktywne endpointy Anthropic ani brakujące
  dokładne cele referencji.

## [0.3.1] - 2026-08-28

### Upstream

- selektywnie przejęto router prawny 3.32 z commitu
  `4a10568863edc77774790cbcc13d2984e259a87d` projektu Michała Wiatraka;
- dodano kontrolowany fallback źródeł przy braku dostępu do ISAP:
  LEX, Legalis lub ArsLege, bez oznaczania wyniku jako zweryfikowanego
  bez potwierdzenia treści i stanu prawnego.

### Codex port

- zachowano zgodność routera z aktywną instalacją Codex na komputerze;
- walidacja statyczna 32 aktywnych skilli zakończyła się wynikiem 32/32 `PASS`.

## [0.3.0] - 2026-08-27

### Upstream

- zsynchronizowano port z uniwersalną wersją rozwojową Lex Machina, commit
  `21bc139886be011691b88b209aae3374b8c2da89` projektu Michała Wiatraka;
- przejęto wspólny `UNIVERSAL-RUNTIME-ADAPTER.md`, manifesty przenośności,
  metadane OpenAI oraz aktualizacje routera, hardgate, narzędzi i modułów;
- zachowano 32 aktywne skille i wyłączenia dwóch katalogów technicznych.

### Codex port

- znormalizowano rozszerzony frontmatter upstream do schematu obsługiwanego
  przez Codex i zachowano oryginalne metadane w referencjach;
- ponownie zastosowano przenośne ścieżki, lokalne zabezpieczenia prywatności
  i blokadę bezpośrednich wywołań Anthropic API;
- walidacja statyczna zakończyła się wynikiem 32/32 `PASS`; nie pozostały
  ścieżki `/mnt/skills/user`, aktywne endpointy Anthropic ani brakujące
  dokładne cele referencji.

## [0.2.0] - 2026-08-23

### Upstream

- zsynchronizowano port z wersją rozwojową Lex Machina, commit
  `9e37d6092f84b5f1a2fe41717e07611de062951a` autorstwa projektu Michała
  Wiatraka;
- przejęto 99 zmian źródłowych: 32 nowe i 67 zmodyfikowanych plików;
- dodano mapy pokrycia, materiały audytowe F-104/F-108 oraz nowe moduły m.in.
  dla spadków, postępowania cywilnego, prawa karnego, PPSA, Ordynacji
  podatkowej i PZP;
- zachowano 32 aktywne skille i wyłączenia dwóch katalogów technicznych.

### Codex port

- ponownie zastosowano adapter Codex, przenośne ścieżki i blokadę bezpośrednich
  wywołań Anthropic API;
- przeniesiono anonimizację przykładów do powtarzalnego procesu budowania;
- rozszerzono walidator publikacyjny o kontrolę kompletności, rozmiaru i SHA-256
  każdego pliku wykazanego w `manifest.json`;
- naprawiono przenośność runnera regresji na Windows oraz rozwiązywanie
  względnych odwołań `view` w testach portu;
- skorygowano sześć liczników modułów oraz rejestrację trzech istniejących
  modułów (`mod-kaucja-najem-lokalu`, `mod-nielegalny-pobor-mediow`,
  `mod-ROZP-SKLADKOWE-podstawa-wymiaru`);
- wykonano walidację statyczną 32/32, kontrolę integralności manifestu,
  prywatności i testy krytyczne T1/T2/T6/T7 z wynikiem `PASS`;
- zachowano jawne ostrzeżenia T3/T11 do dalszego przeglądu merytorycznego map
  aktów prawnych; nie są one automatycznym werdyktem o błędzie aktu.

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
