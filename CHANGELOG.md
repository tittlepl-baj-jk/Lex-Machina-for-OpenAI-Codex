<!-- Autor: [CODEX] | Utworzony: 2026-08-23 -->

# Changelog

Wszystkie istotne zmiany portu będą dokumentowane w tym pliku. Zmiany przejęte
z upstream są odróżniane od zmian przygotowanych specjalnie dla Codex.

## [Unreleased]

Brak zmian.

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
