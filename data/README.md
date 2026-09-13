# Bibliography and provenance

[resources.json](resources.json) is the source of truth for the curated catalog. The folder reading lists and [reading tracker](../TRACKER.md) are generated from it.

- `year` is the displayed bibliographic year. Some entries use conference/publication year while others use initial preprint year; `status` and `verification` clarify this.
- `date` and `revised`, when present, are dates confirmed from the source.
- `verified` is the research snapshot date, not a promise that the source will remain available.
- `verification` distinguishes a checked abstract or program from a full review, replication, or watched recording.
- `priority` is a learning recommendation: Core, Next, or Optional. It is not a quality score.

`python3 scripts/build_catalog.py` regenerates category lists and creates the tracker only if it does not already exist. It never resets reading progress. New resources can be added to an existing tracker manually.

External links were selected from primary paper records, publisher pages, author project pages, and official event/course sites during the 2026-09-12 research session. The offline integrity check does not request or validate external URLs.

[Home](../README.md)
