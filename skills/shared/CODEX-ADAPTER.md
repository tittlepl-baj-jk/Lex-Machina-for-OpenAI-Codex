# Adapter Lex Machina dla Codex

Ten plik ma pierwszeństwo przed instrukcjami platformowymi odziedziczonymi
z wersji Claude/Cowork. Nie zmienia metodologii prawnej ani bramek jakości.

## Mapowanie operacji

- `view <ścieżka>`: odczytaj wskazany plik dostępnym narzędziem plikowym Codex.
- `web_search`: użyj wyszukiwania internetowego; dla aktualnego prawa obowiązują
  wyłącznie źródła dopuszczone przez router i pełna weryfikacja przed twierdzeniem.
- `web_fetch`: otwórz i odczytaj konkretną stronę źródłową.
- `show_widget`: użyj wizualizacji lub bezpiecznego artefaktu HTML; gdy ta
  możliwość nie jest dostępna, zwróć równoważny raport tekstowy i ujawnij fallback.
- `create_file`: użyj właściwego narzędzia Codex do dokumentów lub plików.
- `present_files`: zwróć użytkownikowi klikalne odnośniki do utworzonych plików.
- Polecenia `bash`/`python` wykonuj wyłącznie w granicach sandboxa i uprawnień.

## API i dane wrażliwe

- Bezpośrednie wywołania Anthropic API są wyłączone w tym porcie.
- Anonimizer może wykonywać wyłącznie lokalną, deterministyczną anonimizację.
- Tryb AI anonimizera wymaga osobnej decyzji użytkownika o dostawcy API,
  kluczu, retencji danych i zgodzie na wysłanie określonych danych.
- Kreator AI widgetu analizatora dowodów jest wyłączony; użyj istniejącego
  statycznego dashboardu albo raportu narracyjnego.
- Nigdy nie wysyłaj akt, danych osobowych ani tajemnicy zawodowej do usługi
  zewnętrznej bez jawnej zgody użytkownika dotyczącej konkretnej operacji.

## Ścieżki

W porcie ścieżki są względne względem pliku zawierającego instrukcję. Nie używaj
historycznych bezwzględnych ścieżek środowiska Claude.
