"""Generate bibliography pages from data/resources.json; preserve reader progress."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "foundations": ("papers/01-foundations/README.md", "Foundations", "Start with PlaNet and MBPO. The original World Models article is optional historical context."),
    "planning": ("papers/02-imagination-and-planning/README.md", "Imagination, planning, and decision-relevant models", "Read Dreamer and TD-MPC side by side, then MuZero and value equivalence. Do not compare benchmark numbers without matching data and compute budgets."),
    "jepa": ("papers/03-jepa-and-goal-planning/README.md", "JEPA-style dynamics and goal planning", "Follow DINO-WM → V-JEPA 2-AC → LeWorldModel. DINO-WM uses a pretrained DINO representation; it is grouped here for its embedding-prediction and planning pattern, not because DINO pretraining is itself JEPA."),
    "frontier": ("papers/04-frontier/README.md", "2025–2026 frontier", "Recent research leads, not a leaderboard. Read the listed preprints critically. Also see [LeWorldModel](../03-jepa-and-goal-planning/README.md), [recent surveys](../../surveys/README.md), and [workshop talks](../../tutorials/README.md)."),
    "surveys": ("surveys/README.md", "Surveys and tutorial papers", "Use Moerland for the conceptual map and the September 2026 control survey for current design tensions. Read robotics-wide surveys selectively for latent dynamics and model–policy coupling."),
    "tutorials": ("tutorials/README.md", "Tutorials, blogs, slides, and videos", "For a current update, begin with the 2026 workshop resources; for mathematical continuity use CS285. Recording announcements do not imply that every video has been watched or independently verified."),
}

def main():
    resources = json.loads((ROOT / "data/resources.json").read_text())
    for category, (path, title, intro) in PAGES.items():
        target = ROOT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        home = "../../README.md" if path.startswith("papers/") else "../README.md"
        lines = [f"# {title}", "", intro, "", "Snapshot: **2026-09-12**. Core / Next / Optional indicate reading priority.", ""]
        for r in resources:
            if r["category"] != category:
                continue
            lines += [f"## {r['title']}", "", f"**{r['priority']} · {r['year']} · {r['kind']}**", "", f"{r['authors']}. {r['status']}.", "", r["why"], "", f"**Read for:** {r['focus']}", "", f"[Open resource]({r['url']})", "", f"*Verification ({r['verified']}): {r['verification']}*", ""]
            if "date" in r:
                lines += [f"First/event date: {r['date']}." + (f" Last checked revision: {r['revised']}." if "revised" in r else ""), ""]
        lines += [f"[Home]({home})", ""]
        target.write_text("\n".join(lines))
    tracker = ROOT / "TRACKER.md"
    if not tracker.exists():
        # GitHub task-list checkboxes are editable directly in Markdown.
        lines = ["# Reading tracker", "", "All entries start unread. Mark a checkbox when complete; add a note link and completion date. Catalog generation preserves this file.", ""]
        for r in resources:
            lines.append(f"- [ ] **{r['priority']}** — [{r['title']}]({r['url']}) ({r['year']}) — notes: — completed:")
        lines += ["", "[Note template](notes/TEMPLATE.md) · [Reading path](READING_PATH.md) · [Home](README.md)", ""]
        tracker.write_text("\n".join(lines))
    print(f"Generated {len(PAGES)} catalog pages for {len(resources)} resources; reading progress preserved.")

if __name__ == "__main__":
    main()
