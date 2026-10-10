# Governance

How the Millibar.io Code of Conduct is maintained, changed and released.

## Maintainers

Maintainers review pull requests, cut releases and keep translations in sync.
They are listed in [.github/CODEOWNERS](.github/CODEOWNERS).

Maintaining this repository is separate from handling reports. Reports go to
[conduct@millibar.io](mailto:conduct@millibar.io) and are never discussed here.

## Who decides

| Change | Who approves |
| --- | --- |
| Typos, links, formatting | Any maintainer |
| Translation fixes | Any maintainer, after review by a native speaker |
| Changes to meaning (rules, scope, reporting, enforcement) | The Millibar.io team, after discussion in an issue |
| Reporting contact (`conduct@millibar.io`) and who reads it | The founders, after confirming with the people involved |

Changes that affect how reports are handled or who handles them take effect only
once the people involved have confirmed they can fulfil the commitment (for
example, acknowledging reports within 48 hours).

## Versioning

We use [Semantic Versioning](https://semver.org/) adapted to a text document:

- **Major** (`2.0.0`): a change to what is allowed, who it applies to, or how
  reports and enforcement work.
- **Minor** (`1.1.0`): new guidance or clarification that does not change
  existing commitments.
- **Patch** (`1.0.1`): typos, formatting, links, translation-only changes.

Until the code is adopted by the team and published on
[millibar.io](https://millibar.io), it stays at version `0.0.1`, without a
changelog or releases. The first published version is `1.0.0`; from then on,
each release is tagged and its changes are recorded.

## Release process

From `1.0.0` onwards:

1. Update the version in the header comment of
   [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
2. For each translation whose meaning is affected, set `status: outdated` (leave
   `source-version` unchanged) and open a translation issue.
3. Merge, then tag the release: `git tag v1.0.0 && git push --tags`. The release
   workflow publishes a GitHub release with notes generated from the merged pull
   requests.
4. Update every place the code is published (see [docs/adopting.md](docs/adopting.md))
   and tell the team what changed.

## Acknowledgement

Every team member, contractor and advisor reads and acknowledges each **major**
version. The record of acknowledgements is kept internally, not in this
repository.

## Annual review

The code is reviewed at least once a year, and after any report that shows it
needs to change. A maintainer opens a review issue each year using the
[annual review template](.github/ISSUE_TEMPLATE/annual-review.yml); a scheduled
workflow opens it automatically every October.
