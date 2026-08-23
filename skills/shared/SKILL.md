---
name: "shared"
description: "Biblioteka plików kanonicznych systemu prawnych skilli — hardgate, walidacja, definicje, terminy, moduły kancelaryjne. NIE jest samodzielnym skillem i NIE odpowiada na zapytania użytkownika: moduły wczytują inne skille przez `view`. Pełny spis modułów — tabele „Zawartość katalogu\" w treści tego pliku."
metadata:
  port: "lex-machina-codex"
  source-tree: "stable-2026-08-21"
  source-directory: "shared"
---

> [!IMPORTANT]
> Port Codex: przed wykonaniem wczytaj `CODEX-ADAPTER.md`. Oryginalne metadane są w `references/CODEX-SOURCE-FRONTMATTER.yaml`.

# shared/ — Wspólne moduły systemu prawnych skilli

Katalog zawiera pliki kanoniczne współdzielone przez wszystkie skille prawne.
Nie jest samodzielnym skillem — pełni rolę biblioteki referencji.

## Zawartość katalogu

| Plik | Rola |
|------|------|
| `PRAWO-HARDGATE.md` | ⛔ Globalny zakaz cytowania prawa/orzeczeń z pamięci — wczytaj przed każdym przepisem |
| `HYBRID-VALIDATION.md` | Walidacja hybrydowa — auto-raport braków po piśmie (Fazy 1–3) |
| `INTAKE-GAP.md` | Zarządzanie brakami danych faktycznych (⬛ pola, tryby 1–3) |
| `POST-VALIDATION.md` | Walidacja spójności po wygenerowaniu gotowego pisma |
| `MOD-WALIDACJA_v2.md` | ⭐ Walidacja formalna i prawnicza pisma (bloki A–J) — **JEDYNE ŹRÓDŁO PRAWDY** |
| `MOD-WALIDACJA.md` | STUB → przekierowuje do `MOD-WALIDACJA_v2.md` (zachować dla kompatybilności) |
| `FACT-SOURCE-LOCK.md` | Klasyfikacja faktów FSL-A/B/C — wywoływany przez MOD-WALIDACJA_v2 (Blok J) |
| `LEGAL-STATUS-LOCK.md` | Weryfikacja statusów aktów LSL-1..6 — wywoływany przez MOD-WALIDACJA_v2 (Blok J) |
| `terminy.md` | Tabela terminów zawitych i przedawnień (KPC, KPK, KPW, KPA, KP, PPSA) |
| `FAKTY_v2.md`                        | Weryfikacja zgodności faktycznej pisma ze źródłem (MOD-FAKTY) |
| `raport-sytuacyjny-integracja.md` | Sekwencja wywołania widgetu Raportu Sytuacyjnego v2 |
| `MOD-STEP-TRACKER.md` | ⛔ Śledzenie kroków i raportowanie pominięć — inicjowany w KROK 0-TRACKER routera; każde pominięcie = obowiązek poinformowania użytkownika + czekanie na decyzję |
| `MOD-REJESTR-POKRYCIA-JEDNOSTEK.md` | ⛔ Rejestr plikowy (RPK) pokrycia zbiorów ≥10 ponumerowanych jednostek (kazusy, dokumenty, świadkowie...) w sesji wieloturowej — inicjowany PRZED podziałem na partie, commit po KAŻDEJ partii, obowiązkowy odczyt po kompaktowaniu; zapobiega cichemu pominięciu pojedynczych jednostek |
| `DEFINICJE-KLUCZOWE.md` | Router do 10 plików w `definicje/`: DEF-PODMIOTY-WLASNOSC, DEF-ODPOWIEDZIALNOSC-SZKODA, DEF-PRACA, DEF-PROCEDURA, DEF-BUDOWLANE-DROGOWE, DEF-PODATKOWE, DEF-CYWILNE-WYKLADNIA, DEF-ADMINISTRACYJNE, DEF-INTERES-WLASNY-WYLACZENIA, METODOLOGIA-ORKA2 |
| `MOD-DOKUMENT-GATES.md` | ⛔ Osiem bramek pracy na dokumentach (§1 DOCUMENT-SCAN-PROMPT, §2 FOUNDATION-VERIFICATION-GATE, §3 EXHAUSTIVE-EXTRACTION-GATE, §4 IMMEDIATE-LOGICAL-SCAN, §5 CROSS-DOCUMENT-CONSISTENCY-CHECK, §6 ENTITY-DISAMBIGUATION-TABLE, §7 EVIDENCE-THREAD-LINKING, §8 QUOTE-VERIFICATION-DEFAULT). Konsumenci: `przesluchanie-swiadkow-v2-min90` (PRE-W1a.5 DG-LOAD) i `analizator-dowodow-v3` (KROK 0d DG-LOAD). Utworzony 2026-08-20z przez wydzielenie z pierwszego z nich (F-100 A) — treść przeniesiona 1:1 |
| `mod-niewidomy-prawa-prawne.md` | Osoba niewidoma: prawa procesowe KPK/KPC, ulgi, stopnie niepełnosprawności, Konwencja ONZ o prawach osób niepełnosprawnych |

Pliki w `prawny-router-v3/references/` (nie w shared, ale powiązane):
| `pokrycie-dziedzinowe.md` | Pełna mapa dziedzin → modułów → powiązanych skilli (28 dziedzin) |

Wszystkie pliki są kanoniczne — nie istnieją stuby ani kopie w innych lokalizacjach.

## tools/ — narzędzia produkcyjne (kod, nie markdown)

`shared/tools/` zawiera skrypty uruchamiane przez portal poza sesją modelu
— nie wczytuj ich przez `view()`, to nie są moduły promptowe:

| Plik | Rola |
|------|------|
| `tools/walidator_cytowan.py` | Deterministyczna bramka: sprawdza, czy każde powołanie w gotowym piśmie ma odpowiadający log web_fetch. Pełny opis: `tools/README.md` |

## Jak korzystać

Każdy skill wczytuje pliki z tego katalogu bezpośrednio przez `view`:

```
view ../shared/MOD-STEP-TRACKER.md  ← KROK 0-TRACKER (przed wszystkim — ST-INIT)
view ../shared/MOD-REJESTR-POKRYCIA-JEDNOSTEK.md  ← RPK-INIT (gdy zbiór ≥10 ponumerowanych jednostek, np. seria kazusów)
view ../shared/PRAWO-HARDGATE.md  ← wymagane przed każdym przepisem/orzeczeniem
view ../shared/HYBRID-VALIDATION.md
view ../shared/INTAKE-GAP.md
view ../shared/POST-VALIDATION.md
view ../shared/terminy.md
view ../shared/FAKTY_v2.md
view ../shared/raport-sytuacyjny-integracja.md
```

Nie wczytuj wszystkich naraz — tylko te potrzebne dla danego kroku.

> **Uwaga:** `raport-sytuacyjny-integracja.md` jest wywoływany przez `prawny-router-v3`
> opisowo (punkty self-check [A]/[B]/[C]). Skille dziedzinowe nie wywołują go przez `view` —
> logika wyzwalania jest w routerze. `FAKTY_v2.md` jest wbudowany bezpośrednio w `pisma-procesowe-v3`
> i `pisma-proste-v2` (sekcje MOD-FAKTY / M-FAKTY) — wywołanie przez `view` możliwe gdy potrzebna
> jest pełna wersja modułu.

## Zasada utrzymania (v2.1 — 2026-06-04)

- `DEPENDENCY-GRAPH.md` — pełna mapa zależności: który skill wywołuje który moduł; aktualizuj przy każdej zmianie
- ⚠️ Katalog `archive/` NIE istnieje na dysku (zweryfikowano 2026-06-14) — wcześniejsze
  wzmianki o "43 plikach nieaktywnych" są nieaktualne. Pliki uznane za nieaktywne
  są obecnie oznaczane in-situ (np. ⛔ DEPRECATED w nagłówku, jak AKTY-PRAWNE-MASTER.md)
  zamiast przenoszenia do archive/.

- Wszystkie pliki w tym katalogu są **kanoniczne** — jedyna kopia w systemie
- Stuby lokalne w katalogach poszczególnych skilli zostały usunięte
- Skille wywołują pliki bezpośrednio przez `view ../shared/X.md`
- Nie twórz lokalnych kopii ani stubów — aktualizuj tylko ten katalog

## Moduły kancelaryjne v3.0 — obowiązkowe moduły współdzielone

| Plik | Rola |
|------|------|
| `FORMAL-CHECK.md` | Centralna walidacja formalna pisma i decyzja: gotowe / uzupełnić / nie składać |
| `BRAKI-FORMALNE.md` | Klasyfikacja braków krytycznych, istotnych i technicznych |
| `WARUNKI-SKUTECZNOSCI.md` | Warunki procesowej skuteczności pozwu, apelacji, zażalenia, sprzeciwu, KPA itd. |
| `TRYBY-PROCESOWE.md` | Centralny rejestr trybów, etapów, rygorów i modułów do wczytania |
| `PREKLUZJA-DOWODOWA.md` | Kontrola spóźnionych twierdzeń i dowodów |
| `TERM-CALC.md` | Metodologia kontroli terminów; nie zastępuje kalendarza sądowego |
| `ZAZALENIE-ADRESAT-GATE.md` | Bramka: adresat zażalenia/odwołania/skargi (poziome vs dewolutywne, za pośrednictwem) — obowiązkowa przy każdym środku zaskarżenia (dodano 2026-07-25) |
| `WLASCIWOSC-GATE.md` | Bramka siostrzana: właściwość rzeczowa/miejscowa/funkcjonalna sądu/organu przy WNOSZENIU sprawy (pozew/wniosek) — obowiązkowa przy każdym piśmie inicjującym postępowanie (dodano 2026-07-27, na pytanie użytkownika) |
| `ZAWIADOMIENIA-KRZYZOWE.md` | Obowiązek instytucji (PIP, KAS, sąd) do zawiadamiania prokuratury/Policji o przestępstwie ujawnionym przy okazji własnego postępowania (art. 304 KPK) — kontrole krzyżowe między organami (dodano 2026-07-27, na pytanie użytkownika) |
| `RISK-ASSESSMENT.md` | Matryca ryzyka formalnego, dowodowego, prawnego i kosztowego |
| `ORZECZENIA-HIERARCHIA.md` | Hierarchia orzecznictwa, test aktualności i karta orzeczenia |
| `DOWODY-METODOLOGIA.md` | Matryca dowodowa i test wiarygodności dowodu |
| `ROSZCZENIA.md` | Konstrukcja roszczeń głównych, ewentualnych i alternatywnych |
| `STRATEGIA-PROCESOWA.md` | Taktyka procesowa i wybór następnego ruchu |
| `QUALITY-CHECK.md` | Kontrola jakości pisma: logika, struktura, nadmiar, emocjonalność |
| `KANCELARIA-WORKFLOW.md` | Sekwencja pracy kancelaryjnej możliwa w `.md skills` |
| `STATUS.md` | Rejestr wersji i statusów modułów shared |
| `MOD-TIMING.md` | Strategia timing składania pism — macierz T1–T5, 6 modeli (T-EARLY…T-ADVANCE-NOTICE) |
| `MOD-PEER-REVIEW.md` | Weryfikacja krzyżowa pisma — 4 role (adwokat diabła, sędzia, klient, spójność) |
| `MOD-INTRO.md` | Executive summary pisma (str. 1) — 2–5 zdań, max 150 słów, killer argument na str. 1 |
| `MOD-KONCENTRACJA.md` | Metryka długości pisma per typ — limity orientacyjne, algorytm K1–K4, reguły skracania |
| `MOD-DOKTRYNA.md` | Polityka cytowania komentarzy i doktryny — hierarchia D-1–D-4, formaty, HARDGATEs |
| `MOD-WIDGET-IO.md` | ⭐ Obligatoryjny pasek Import/Export dla widgetów analitycznych — matryca per skill, wzorzec HTML/CSS/JS, reguły IO-1–IO-8 |
| `MOD-KARTA-DOWODU.md` | ⛔ Karta dowodowa i graf faktów — pisma-procesowe-v3 W1.2c-PRE (po SD-SKAN, przed macierzą MT1); analizator-dowodow-v3 BLOK-B2 |
| `MOD-ELIMINACJA-TEZ.md` | ⛔ Eliminacja tez, żądań i przepisów bez pokrycia prawnego — pisma-procesowe-v3 W1.2a-POST (po CLAIM-VALIDATION, przed W1.3); analizator-dowodow-v3 BLOK-C |
| `MOD-BUDOWA-ARGUMENTU.md` | ⛔ Obowiązkowy schemat budowy każdego argumentu — W2.2, każdy akapit uzasadnienia |
| `MOD-KOSZT-ODPOWIEDZI.md` | ⛔ Optymalizacja kosztu procesowego dla przeciwnika — W2.2 dla każdego głównego twierdzenia + W3.6a AUDYT-KOŃCOWY |
| `MOD-MIKROPODSUMOWANIA.md` | ⛔ Obowiązkowe podsumowanie każdego rozdziału uzasadnienia — W2.2, koniec każdej sekcji numerowanej |
| `MOD-SKUTEK-PROCESOWY.md` | ⛔ Obowiązkowy blok skutku procesowego — W2.2, koniec każdego bloku uzasadnienia klasy A/B |
| `MOD-STRESS-TEST.md` | ⛔ Symulacja odpowiedzi pełnomocnika pozwanego — po W2 (projekt pisma), przed W3 / AUDYT-KOŃCOWY |

### Obowiązkowe wywołania dla generatorów pism

Przy każdym piśmie gotowym do złożenia generator musi co najmniej wczytać:

```text
view ../shared/TRYBY-PROCESOWE.md
view ../shared/FORMAL-CHECK.md
view ../shared/BRAKI-FORMALNE.md
view ../shared/WARUNKI-SKUTECZNOSCI.md
view ../shared/RISK-ASSESSMENT.md
view ../shared/QUALITY-CHECK.md
```

Gdy występują terminy, dowody, orzecznictwo albo strategia, dodatkowo:

```text
view ../shared/TERM-CALC.md
view ../shared/PREKLUZJA-DOWODOWA.md
view ../shared/DOWODY-METODOLOGIA.md
view ../shared/ORZECZENIA-HIERARCHIA.md
view ../shared/ROSZCZENIA.md
view ../shared/STRATEGIA-PROCESOWA.md
```

Gdy pismo wymaga executive summary, metryki długości lub peer review:

```text
view ../shared/MOD-INTRO.md           (pozew/apelacja/pismo >3 str.)
view ../shared/MOD-KONCENTRACJA.md    (kontrola długości — zawsze)
view ../shared/MOD-PEER-REVIEW.md     (gdy WPS>50k / ≥3 żądania / apelacja)
view ../shared/MOD-DOKTRYNA.md        (gdy cytowanie komentarzy w W2)
view ../shared/MOD-TIMING.md          (gdy pytanie o timing złożenia)
```

Przed W1.3 (eliminacja tez bez pokrycia) i w trakcie W1.2c-PRE (karta dowodowa), obowiązkowo:

```text
view ../shared/MOD-ELIMINACJA-TEZ.md  (⛔ W1.2a-POST, po CLAIM-VALIDATION)
view ../shared/MOD-KARTA-DOWODU.md    (⛔ W1.2c-PRE, po SD-SKAN)
```

W W2.2 (redakcja każdego bloku uzasadnienia), obowiązkowo w tej kolejności:

```text
view ../shared/MOD-BUDOWA-ARGUMENTU.md    (⛔ każdy akapit uzasadnienia)
view ../shared/MOD-KOSZT-ODPOWIEDZI.md    (⛔ każde główne twierdzenie)
view ../shared/MOD-SKUTEK-PROCESOWY.md    (⛔ koniec bloku klasy A/B)
view ../shared/MOD-MIKROPODSUMOWANIA.md   (⛔ koniec każdego rozdziału)
```

Po W2 (projekt pisma gotowy), przed W3/AUDYT-KOŃCOWY, obowiązkowo:

```text
view ../shared/MOD-STRESS-TEST.md     (⛔ symulacja odpowiedzi pełnomocnika pozwanego)
```
