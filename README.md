# Sambi

Repozytorium zawiera automatyzację Claude Code: wklejasz link(i) do filmu na
YouTube, a Claude transkrybuje film i na tej podstawie tworzy nowy skill w
`.claude/skills/` albo aktualizuje już istniejący, jeśli temat pasuje.

## Jak to działa

Cała logika opisana jest w `.claude/skills/youtube-to-skill/SKILL.md`.
W skrócie:

1. Wklejasz jeden lub więcej linków YouTube w wiadomości do Claude.
2. Claude pobiera transkrypcję (`scripts/fetch_transcript.py` — najpierw
   przez `youtube-transcript-api`, w razie potrzeby fallback do `yt-dlp`).
3. Claude wyciąga z transkrypcji konkretną, wielokrotnego użytku wiedzę
   (metodę, framework, instrukcje) — nie streszczenie filmu.
4. Sprawdza istniejące skille (`scripts/list_skills.py`) i albo aktualizuje
   pasujący, albo tworzy nowy folder skilla.
5. Commituje zmiany.

## Wymagania

Pobranie transkrypcji wymaga dostępu sieciowego do YouTube. Jeśli sesja, w
której działa Claude, ma zablokowany dostęp do `youtube.com` (np. przez
politykę egress w środowisku zdalnym), skrypt zwróci czytelny błąd i Claude
poprosi o wklejenie transkrypcji ręcznie albo o uruchomienie w środowisku
z dostępem do sieci (np. lokalny Claude Code).
