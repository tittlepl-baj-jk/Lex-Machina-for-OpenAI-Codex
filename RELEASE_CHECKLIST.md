<!-- Autor: [CODEX] | Utworzony: 2026-08-23 -->

# Checklista wydania

## Pochodzenie i licencja

- [ ] `LICENSE` zawiera niezmienioną pełną treść GNU GPL version 3.
- [ ] `NOTICE.md` wskazuje Michała Wiatraka i projekt Lex Machina.
- [ ] `UPSTREAM.md` zawiera aktualny commit i datę synchronizacji.
- [ ] Zmodyfikowane elementy mają widoczną informację o zmianie i dacie.
- [ ] Nie dodano warunków ograniczających prawa przyznane przez GPLv3.
- [ ] Wszystkie zależności i materiały zewnętrzne mają zgodne licencje.

## Autorstwo i komunikacja

- [ ] Historia Git rozróżnia zmiany upstream i zmiany portu.
- [ ] `AUTHORS.md` i `CHANGELOG.md` są aktualne.
- [ ] Opis nie sugeruje oficjalnego wsparcia Michała Wiatraka, OpenAI ani Anthropic.
- [ ] Nazwa i opis jednoznacznie identyfikują projekt jako nieoficjalny port.

## Bezpieczeństwo i prywatność

- [ ] Brak kluczy API, haseł, tokenów i prywatnych ścieżek lokalnych.
- [ ] Brak danych osobowych, prawdziwych akt i tajemnicy zawodowej.
- [ ] Bezpośrednie wywołania Anthropic API pozostają wyłączone.
- [ ] Nowe integracje zewnętrzne wymagają jawnej konfiguracji użytkownika.

## Jakość

- [ ] Wszystkie aktywne skille przechodzą walidację statyczną.
- [ ] Testy K1-K5 wykonano na danych fikcyjnych.
- [ ] Nie ma martwych odwołań ani historycznych ścieżek `/mnt/skills/user/`.
- [ ] `manifest.json` nie zawiera prywatnych ścieżek ani tajemnic.
- [ ] Dokumentacja instalacji odpowiada zawartości wydania.
- [ ] `python scripts/validate_port.py` kończy się wynikiem `pass: true`.
- [ ] Workflow GitHub Actions `Validate port` przechodzi poprawnie.

## Publikacja

- [ ] Ustalono właściciela, nazwę i widoczność repozytorium GitHub.
- [ ] `origin` wskazuje port, a `upstream` projekt Michała Wiatraka.
- [ ] Utworzono podpisany lub opisany tag wydania.
- [ ] Opublikowano pełne źródła odpowiadające wydaniu.
