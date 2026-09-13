# JEPA-style dynamics and goal planning

Follow DINO-WM → V-JEPA 2-AC → LeWorldModel. DINO-WM uses a pretrained DINO representation; it is grouped here for its embedding-prediction and planning pattern, not because DINO pretraining is itself JEPA.

Snapshot: **2026-09-12**. Core / Next / Optional indicate reading priority.

## DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning

**Core · 2024 · paper / project page**

Gaoyue Zhou; Hengkai Pan; Yann LeCun; Lerrel Pinto. Preprint 2024; ICLR 2025.

A clear offline, reward-free route from action-conditioned feature prediction to goal planning.

**Read for:** Frozen patch features; action-sequence optimization; goal distance and transfer limits.

[Open resource](https://dino-wm.github.io/)

*Verification (2026-09-12): Author page and OpenReview paper checked.*

## V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

**Core · 2025 · paper**

Mido Assran et al.. 2025 research paper; venue not checked.

Connects action-free representation learning to action-conditioned latent control.

**Read for:** Read V-JEPA 2-AC post-training and MPC, rather than concentrating on video understanding scores.

[Open resource](https://arxiv.org/abs/2506.09985)

*Verification (2026-09-12): Paper record and Meta author explanation checked.*

## LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

**Core · 2026 · paper**

Lucas Maes; Quentin Le Lidec; Damien Scieur; Yann LeCun; Randall Balestriero. Preprint; peer-review status not verified.

A recent end-to-end JEPA model using next-embedding prediction and distribution regularization.

**Read for:** How is collapse prevented without relying on a frozen pretrained encoder?

[Open resource](https://arxiv.org/abs/2603.19312)

*Verification (2026-09-12): arXiv abstract and revision history checked; results not reproduced.*

First/event date: 2026-03-13. Last checked revision: 2026-06-03.

[Home](../../README.md)
