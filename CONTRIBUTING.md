# Keeping this repository useful

## Add a resource

1. Prefer a primary paper, author explanation, official course, or official event page.
2. Confirm title, authors, first publication date, latest revision, and publication status independently. Do not interpret a search-engine crawl date as a publication date.
3. Write why the resource matters for action-conditioned prediction, planning, or policy learning.
4. Record what was actually checked in `verification`: abstract, full paper, code, experiments, or recording.
5. Add a unique record to [data/resources.json](data/resources.json), then run `python3 scripts/build_catalog.py`.
6. Add an unchecked entry to [TRACKER.md](TRACKER.md) if desired; its existing progress is preserved.
7. Run `python3 scripts/check_repo.py` and inspect the edited pages.

## Suggested monthly review

- Browse the [ICLR world-model workshop papers](https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FWorld_Models) and [tutorial survey resource browser](https://clearlab-sustech.github.io/WorldModelSurvey/#resources).
- Search for action-conditioned latent dynamics, model-based RL, latent MPC, decision-aware model learning, and JEPA planning.
- Follow citations to a small anchor set: Dreamer, TD-MPC, DINO-WM, V-JEPA 2-AC, and LeWorldModel.
- Add only a few resources with a clear conceptual contribution. Record negative results and evaluations as well as new methods.
- Update dates only for entries actually rechecked. Do not mark the entire repository verified after changing one item.

This is a manual workflow, not an installed monitor or scheduled task.

## Inclusion criteria

Prefer work that evaluates at least one of: closed-loop return/success, action-conditioned multi-step prediction, policy improvement using a learned model, planning compute, or robustness under model error. Use broader conceptual surveys sparingly and identify the relevant sections.

Do not promote a new preprint solely because it claims state of the art. Do not reproduce copyrighted paper figures or PDFs without permission. Original schematics should be labeled as such, with primary sources linked in surrounding text.

## Generated content

The six category README files are generated from `data/resources.json`; edit that source rather than hand-editing those lists. `scripts/build_figures.py` generates the SVGs. Personal notes and tracker checkboxes are not overwritten.

[Home](README.md)
