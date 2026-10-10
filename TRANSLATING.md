# Translating

We want everyone in the Millibar community to be able to read the Code of
Conduct in a language they are comfortable with. The English text in
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) is authoritative; translations follow it.

## Translation files

Each language has one file in [`translations/`](translations/), named with its
[ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code, e.g.
`translations/de.md`. Use a regional code only when it really matters
(`pt-BR.md`).

Every file starts with a header comment:

```html
<!-- translation: de | source-version: 0.0.1 | status: needs-review -->
```

| Field | Meaning |
| --- | --- |
| `translation` | The language code, matching the file name |
| `source-version` | The version of the English text this translation follows |
| `status` | `needs-review`, `reviewed` or `outdated` |

### Status

- **`needs-review`**: translated, but not yet checked by a native speaker. New
  translations, including machine-assisted ones, start here.
- **`reviewed`**: a native speaker other than the translator has checked it
  against the English text.
- **`outdated`**: the English text has changed since `source-version`.
  Maintainers set this when releasing a new version.

## Adding a new language

1. Open a [translation issue](https://github.com/MBAR-Millibar/Code-of-Conduct/issues/new?template=translation.yml) so
   nobody duplicates the work.
2. Copy [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to `translations/<code>.md`.
3. Replace the first line with the translation header, `status: needs-review`.
4. Replace the version note under the title with a note saying the English
   version is authoritative, linking to `../CODE_OF_CONDUCT.md`.
5. Translate the text. Keep:
   - the same headings, in the same order (CI checks this);
   - `conduct@millibar.io`, `Millibar.io` and all URLs unchanged;
   - the Creative Commons link, using the localised deed where one exists
     (e.g. `…/by-sa/4.0/deed.de`).
6. Add the language to the table in [README.md](README.md) and the language line
   at the top of [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
7. Run `python3 scripts/check_translations.py` and open a pull request.

## Reviewing a translation

Reviews by native speakers are the most valuable contribution you can make.

1. Read the translation side by side with the English text.
2. Check meaning first, then tone: the code should sound warm and direct, not
   legalistic.
3. Use gender-inclusive language that is natural in the language
   (e.g. `Nutzer*innen` in German, `·` forms or paired nouns in French).
4. Open a pull request with your fixes and set `status: reviewed`. If you have no
   fixes, open a pull request that only changes the status, and say so in the
   description.

## Updating an outdated translation

1. Compare the English text between the old and new version:
   `git diff v<old>..v<new> -- CODE_OF_CONDUCT.md`
2. Update the translation, then set `source-version` to the new version and
   `status` to `needs-review` (or `reviewed` if a second native speaker approved
   it in the pull request).

## Current translations

| Language | Status | Notes |
| --- | --- | --- |
| العربية (`ar`) | needs-review | Machine-assisted draft |
| Български (`bg`) | needs-review | Machine-assisted draft |
| Čeština (`cs`) | needs-review | Machine-assisted draft |
| Deutsch (`de`) | needs-review | Machine-assisted draft |
| Español (`es`) | needs-review | Machine-assisted draft |
| Français (`fr`) | needs-review | Machine-assisted draft |
| Italiano (`it`) | needs-review | Machine-assisted draft |
| 日本語 (`ja`) | needs-review | Machine-assisted draft |
| Polski (`pl`) | needs-review | Machine-assisted draft |
| Русский (`ru`) | needs-review | Machine-assisted draft |

These are the languages of the [Berlin Code of Conduct](https://github.com/rubyberlin/code-of-conduct)
(which uses `cz` for Czech; we use the ISO code `cs`). German, Spanish, French
and Italian are also the languages of the Millibar platform.
