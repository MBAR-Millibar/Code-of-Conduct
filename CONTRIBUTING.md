# Contributing

Thank you for helping us make the Millibar.io Code of Conduct clearer and fairer.

> **This repository is not a reporting channel.** To report behaviour that breaks
> the code, email [conduct@millibar.io](mailto:conduct@millibar.io). Never
> describe an incident or name people in an issue or pull request.

By contributing, you agree that your contribution is released under
[CC BY-SA 4.0](LICENSE), and you agree to follow the
[Code of Conduct](CODE_OF_CONDUCT.md) in all discussions here.

## What to contribute

- Clearer or simpler wording
- Gaps: situations the code does not cover but should
- More inclusive language
- Fixes to typos, links or formatting
- Translation reviews and new translations (see [TRANSLATING.md](TRANSLATING.md))

Diving-specific rules (e.g. physical contact during training, dive trips) belong
in the separate Step 2 code for diving operators and communities, not here.

## How to propose a change

1. **Small fixes** (typos, broken links, formatting): open a pull request
   directly.
2. **Changes to meaning** (new rules, changed commitments, reporting or
   enforcement process): open a
   [wording change issue](https://github.com/MBAR-Millibar/Code-of-Conduct/issues/new?template=wording-change.yml) first, so
   the change can be discussed before anyone writes text.
3. Fork the repository and create a branch (`docs/…`, `fix/…` or `i18n/<lang>-…`).
4. Edit [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Keep sentences short and plain:
   many readers use English as a second language.
5. Run the checks locally (see below) and open a pull request.

You do not need to update translations when you change the English text. The
maintainers mark affected translations as outdated, and translators follow up.

## Writing style

- Use "we" for the community and "you" for the reader.
- Prefer plain words to legal language.
- British English spelling (`behaviour`, `apologise`, `licence` as a noun).
- One idea per bullet point.
- Do not add or remove section headings without discussing it first: the
  translations mirror the English structure.

## Checks

CI runs on every pull request:

- **Markdown lint** (`markdownlint-cli2`)
- **Link check** (`lychee`)
- **Translation consistency** (`scripts/check_translations.py`): every
  translation has a valid header and the same section structure as the English
  text, and outdated translations are reported.

Run them locally:

```bash
npx markdownlint-cli2 "**/*.md"
python3 scripts/check_translations.py
```

## Review

Pull requests that change meaning need approval from a maintainer, and the
change becomes official only through a release (see [GOVERNANCE.md](GOVERNANCE.md)).

## Commit convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Use for |
| --- | --- |
| `docs:` | Changes to the code text or documentation |
| `i18n:` | Translations |
| `fix:` | Typos, broken links |
| `ci:` | Workflows and scripts |
| `chore:` | Repository maintenance |
