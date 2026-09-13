# Imagination, planning, and decision-relevant models

Read Dreamer and TD-MPC side by side, then MuZero and value equivalence. Do not compare benchmark numbers without matching data and compute budgets.

Snapshot: **2026-09-12**. Core / Next / Optional indicate reading priority.

## Dream to Control: Learning Behaviors by Latent Imagination

**Core · 2020 · paper / author resources**

Danijar Hafner et al.. ICLR 2020.

Shows how to train an actor and critic inside a latent model.

**Read for:** Imagined returns, actor gradients, and inference without trajectory search.

[Open resource](https://danijar.com/project/dreamer/)

*Verification (2026-09-12): Author page and original paper checked; preprint 2019.*

## Mastering diverse control tasks through world models (DreamerV3)

**Next · 2025 · paper**

Danijar Hafner; Jurgis Pasukonis; Jimmy Ba; Timothy Lillicrap. Nature 2025.

A mature imagination-based agent across diverse tasks.

**Read for:** What changes improve robustness across reward scales and domains?

[Open resource](https://doi.org/10.1038/s41586-025-08744-2)

*Verification (2026-09-12): Publisher record checked. Publication is 2025; initial DreamerV3 preprint is 2023.*

## Temporal Difference Learning for Model Predictive Control

**Core · 2022 · paper / slides / video**

Nicklas Hansen; Xiaolong Wang; Hao Su. ICML 2022.

Combines short latent planning with learned long-term value.

**Read for:** Latent consistency, reward and TD losses; policy-guided MPC.

[Open resource](https://www.nicklashansen.com/td-mpc/)

*Verification (2026-09-12): Author method page checked; video not independently watched.*

## TD-MPC2: Scalable, Robust World Models for Continuous Control

**Core · 2024 · paper / code / models**

Nicklas Hansen; Hao Su; Xiaolong Wang. ICLR 2024.

A strong reference for task-oriented decoder-free world models.

**Read for:** Which improvements address training stability and multi-task scaling?

[Open resource](https://www.tdmpc2.com/)

*Verification (2026-09-12): Author page and arXiv record checked; initial preprint 2023.*

## Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model

**Core · 2020 · paper**

Julian Schrittwieser et al.. Nature 2020.

Introduces search with learned reward/value/policy predictions.

**Read for:** What constrains a recurrent latent state without reconstruction or explicit next-embedding targets?

[Open resource](https://arxiv.org/abs/1911.08265)

*Verification (2026-09-12): Paper record and DeepMind author blog checked; preprint 2019.*

## The Value Equivalence Principle for Model-Based Reinforcement Learning

**Next · 2020 · theory paper**

Christopher Grimm; André Barreto; Satinder Singh; David Silver. NeurIPS 2020.

Formalizes why decision-useful models can ignore environment details.

**Read for:** Equivalence relative to policy and value-function classes; Bellman operators.

[Open resource](https://arxiv.org/abs/2011.03506)

*Verification (2026-09-12): Paper abstract and proceedings record checked.*

[Home](../../README.md)
