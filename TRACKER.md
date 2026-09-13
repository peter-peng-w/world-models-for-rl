# World-model learning tracker

A working notebook for understanding action-conditioned dynamics, planning, and policy learning. **Reading priority, reading progress, and demonstrated understanding are separate fields.**

[Reading path](READING_PATH.md) · [Conceptual guide](docs/01-mental-model.md) · [Equations](docs/02-key-equations.md) · [Paper-note template](notes/TEMPLATE.md) · [Home](README.md)

## What Core, Next, and Optional mean

| Priority | Meaning for this curriculum | How to use it |
| --- | --- | --- |
| **Core** | Main learning recommendations for the RL, latent dynamics, and planning focus. | Start with the relevant foundations; give these resources your main attention. A Core workshop means select relevant talks, not watch everything. |
| **Next** | Follow-up depth, extensions, or recent research after the relevant concepts are familiar. | Choose by your current question. You do not need to finish every Core item first. |
| **Optional** | Historical context, adjacent approaches, or specialized depth. | Read when useful; skipping it does not block the main path. |

These are editorial learning priorities, **not** completion states, difficulty scores, publication-quality ratings, or a ranking of methods. A recent preprint can be Core because it matches your interests; that does not imply its claims are established. Priorities can be personalized. The original 25 priorities are preserved here so the catalog and tracker remain consistent.

## How to use this tracker in your browser

1. Use GitHub's **Edit this file** button, update the relevant row, and save with **Commit changes**.
2. Keep a small active queue below. Pick a concrete output, such as explaining a loss or comparing two planners.
3. Update **Status** after reading, and **Understanding** only after checking what you can explain without the source open.
4. Use the resource ID in your notes and session log. Replace the dash in Notes with a link to a file you actually created using the [note template](notes/TEMPLATE.md).
5. Record completion and review dates in YYYY-MM-DD format. Review dates are your own choices; this Markdown file does not send reminders or calculate progress automatically.

All 25 existing entries were unread with no notes or completion dates when this version was created on **2026-09-13**. They remain unread below. This update does not infer your actual reading progress. Catalog generation preserves this file.

### Progress and understanding vocabulary

| Field | Values and meaning |
| --- | --- |
| **Status** | Unread; Skimmed (orientation only); Reading; Read (finished your declared scope); Revisit (needs another pass); Paused; Skipped (record why). |
| **Understanding** | — = unassessed; U1 = explain the idea and prediction/decision loop; U2 = derive or trace the key equations and algorithm; U3 = compare alternatives, identify assumptions, and critique the evidence. |
| **Notes** | Link to your own notes. Record selected sections or talks when the resource is a collection. |
| **Finished / Review** | Date you finished the declared scope / date you plan to revisit it. A dash means unset. |

Implementation or reproduction is optional and tracked separately in the session log. Reading a paper does not mean reproducing its results. For blogs and talks, use the understanding levels that fit the material.

## Active queue

Suggested starting choices, not recorded progress or deadlines. Replace freely; keep at most three active items.

| Order | Resource | Concrete output | Target date |
| --- | --- | --- | --- |
| 1 | S01: model-based RL survey | Draw a map of model learning versus model usage. | — |
| 2 | P01: Dreamer | Explain actor training in imagination versus planning at deployment. | — |
| 3 | J02: V-JEPA 2 | Explain precisely what makes V-JEPA 2-AC action-conditioned. | — |

## Resource register

Years follow the existing catalog's labels; initial preprint and publication years can differ. Full titles, publication context, and verification metadata remain in the [bibliography](data/resources.json) and the [category reading lists](papers/README.md). This update reorganizes the existing resources; it is not a new literature search. Workshop links may be programs rather than complete recording archives.

### Foundations

| ID | Resource | Priority | Status | Understanding | Notes | Finished / Review |
| --- | --- | --- | --- | --- | --- | --- |
| F01 | [World Models](https://worldmodels.github.io/) (2018) | Optional | Unread | — | — | — / — |
| F02 | [PlaNet](https://planetrl.github.io/) (2019) | Core | Unread | — | — | — / — |
| F03 | [MBPO](https://arxiv.org/abs/1906.08253) (2019) | Core | Unread | — | — | — / — |

### Planning and imagination

| ID | Resource | Priority | Status | Understanding | Notes | Finished / Review |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | [Dreamer](https://danijar.com/project/dreamer/) (2020) | Core | Unread | — | — | — / — |
| P02 | [DreamerV3](https://doi.org/10.1038/s41586-025-08744-2) (2025) | Next | Unread | — | — | — / — |
| P03 | [TD-MPC](https://www.nicklashansen.com/td-mpc/) (2022) | Core | Unread | — | — | — / — |
| P04 | [TD-MPC2](https://www.tdmpc2.com/) (2024) | Core | Unread | — | — | — / — |
| P05 | [MuZero](https://arxiv.org/abs/1911.08265) (2020) | Core | Unread | — | — | — / — |
| P06 | [Value Equivalence Principle](https://arxiv.org/abs/2011.03506) (2020) | Next | Unread | — | — | — / — |

### JEPA and goal planning

| ID | Resource | Priority | Status | Understanding | Notes | Finished / Review |
| --- | --- | --- | --- | --- | --- | --- |
| J01 | [DINO-WM](https://dino-wm.github.io/) (2024) | Core | Unread | — | — | — / — |
| J02 | [V-JEPA 2](https://arxiv.org/abs/2506.09985) (2025) | Core | Unread | — | — | — / — |
| J03 | [LeWorldModel](https://arxiv.org/abs/2603.19312) (2026) | Core | Unread | — | — | — / — |

### Recent research

| ID | Resource | Priority | Status | Understanding | Notes | Finished / Review |
| --- | --- | --- | --- | --- | --- | --- |
| R01 | [Dreamer 4](https://arxiv.org/abs/2509.24527) (2025) | Next | Unread | — | — | — / — |
| R02 | [Temporal-Distance JEPA](https://arxiv.org/abs/2607.25337) (2026) | Next | Unread | — | — | — / — |
| R03 | [Reinforced Planning with Latent World Models](https://arxiv.org/abs/2608.18669) (2026) | Next | Unread | — | — | — / — |

### Surveys

| ID | Resource | Priority | Status | Understanding | Notes | Finished / Review |
| --- | --- | --- | --- | --- | --- | --- |
| S01 | [Model-based Reinforcement Learning: A Survey](https://arxiv.org/abs/2006.16712) (2023) | Core | Unread | — | — | — / — |
| S02 | [World models for physical AI with uncertainty representation and control](https://link.springer.com/article/10.1007/s44163-026-02122-1) (2026) | Core | Unread | — | — | — / — |
| S03 | [From World Models to World Action Models](https://arxiv.org/abs/2607.00836) (2026) | Next | Unread | — | — | — / — |

### Tutorials and talks

| ID | Resource | Priority | Status | Understanding | Notes | Finished / Review |
| --- | --- | --- | --- | --- | --- | --- |
| T01 | [CS285: planning and model-based RL lectures](https://rail.eecs.berkeley.edu/deeprlcourse-fa23/) (2023) | Core | Unread | — | — | — / — |
| T02 | [Model-Based RL: Theory and Practice (MBPO blog)](https://bair.berkeley.edu/blog/2019/12/12/mbpo/) (2019) | Core | Unread | — | — | — / — |
| T03 | [Meta: Introducing V-JEPA 2](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/) (2025) | Next | Unread | — | — | — / — |
| T04 | [Chef Robotics: World Models and World-Action Models](https://www.chefrobotics.ai/post/world-models-and-world-action-models-an-accessible-and-comprehensive-survey) (2026) | Next | Unread | — | — | — / — |
| T05 | [ICLR 2026 World Models workshop](https://sites.google.com/view/iclr-2026-workshop-world-model/schedule-speaker) (2026) | Next | Unread | — | — | — / — |
| T06 | [World Models at Chicago Booth](https://wm-booth.org/) (2026) | Core | Unread | — | — | — / — |
| T07 | [Code as World Model: ICLR 2026 slides](https://www.cs.ubc.ca/~murphyk/CWM-ICLR26.pdf) (2026) | Optional | Unread | — | — | — / — |

## What to extract from each resource

These are reading prompts, not statements that a result has been verified. Use them to give each reading session a purpose.

| ID | Evidence of understanding to put in your notes |
| --- | --- |
| F01 | Explain the separation of representation, dynamics, and controller. |
| F02 | Explain latent state inference and receding-horizon planning. |
| F03 | Explain why short model rollouts can limit model bias. |
| P01 | Trace how imagined trajectories improve the actor and critic. |
| P02 | Separate the basic Dreamer loop from robustness and scaling choices. |
| P03 | Explain how latent consistency, reward, and value support MPC. |
| P04 | Identify what changes from TD-MPC and what remains the same. |
| P05 | Explain how search works without observation reconstruction. |
| P06 | State which value predictions a model must preserve. |
| J01 | Explain feature prediction and goal scoring; identify reachability assumptions. |
| J02 | Distinguish action-free pretraining from action-conditioned control. |
| J03 | Identify the anti-collapse mechanism and evaluate evidence for control. |
| R01 | Separate world-model scaling from the procedure for training an agent. |
| R02 | Check how temporal distance shapes representations for planning. |
| R03 | Identify what RL optimizes and what the planner does at deployment. |
| S01 | Place each method on model-learning and model-usage axes. |
| S02 | Read control and uncertainty sections; distinguish uncertainty types. |
| S03 | Map the tutorial terminology to forward models, policies, and planners. |
| T01 | Connect optimal control, model learning, and model-based policy learning. |
| T02 | Explain the intuition behind trusting a learned model locally. |
| T03 | Use the overview to formulate questions for the technical paper. |
| T04 | Separate terminology and broad claims from control evidence. |
| T05 | Select relevant talks and record exact titles and available recording links. |
| T06 | Select talks about action-conditioned dynamics and decision making. |
| T07 | Compare executable models with learned latent transition models. |

## Concept mastery checkpoints

Check a box only after explaining it from memory and recording supporting notes or a worked example. These checkpoints track understanding across papers.

- [ ] Distinguish forward dynamics, inverse dynamics, and a goal-conditioned policy.
- [ ] Explain why partial observability requires history or a belief/latent state.
- [ ] Write an action-conditioned transition model and identify its learning targets.
- [ ] Derive an MPC objective with a terminal value and explain replanning.
- [ ] Trace Dreamer's model, actor, and critic updates and its deployment loop.
- [ ] Explain how TD-MPC combines latent consistency with reward and value learning.
- [ ] Explain the distinction between JEPA pretraining and action-conditioned control.
- [ ] Explain representation collapse and why prediction loss alone can be insufficient.
- [ ] Explain when feature distance can fail as a goal-reaching objective.
- [ ] Explain reward/value/policy prediction in MuZero and the idea of value equivalence.
- [ ] Distinguish one-step prediction quality from long-horizon control quality.
- [ ] Compare model bias, distribution shift, and uncertainty handling across methods.
- [ ] Compare real-data cost, training compute, and decision-time compute fairly.

## Synthesis matrix

Fill this in from the papers, with section/equation references in your notes. Blank cells are intentional learning tasks.

| Method family | State and prediction target | Learning losses | How actions are chosen | Main failure mode / evidence |
| --- | --- | --- | --- | --- |
| PlaNet | — | — | — | — |
| Dreamer / V3 / 4 | — | — | — | — |
| TD-MPC / TD-MPC2 | — | — | — | — |
| DINO-WM / JEPA control | — | — | — | — |
| MuZero / value equivalence | — | — | — | — |

## Reading and experiment log

Add one row per meaningful session. For a partial read, record sections/pages; for a video, record the talk title and timestamps. If implementing, record the experiment, result, and limitations separately from author-reported claims.

| Date | Resource ID | Scope / time spent | Takeaway or derivation | Open question / next action | Notes or experiment link |
| --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — |

## Open questions to resolve

Starter questions; replace or expand as your understanding develops. No answer or mastery is assumed.

| Question | Candidate readings | Current answer / evidence | Status |
| --- | --- | --- | --- |
| What must a latent representation retain for useful control? | P03, P06, J01–J03 | — | Open |
| When should an agent plan online versus learn an actor in imagination? | F02, P01, P03, P05 | — | Open |
| How can a planner exploit model errors, and what limits this? | F03, P03, J01 | — | Open |
| How should stochasticity and uncertainty affect action selection? | S01, S02 | — | Open |
| What evidence distinguishes better representations from more compute or data? | P02, P04, R01–R03 | — | Open |

## Review routine

After a few sessions, revisit one concept from memory, update the synthesis matrix, resolve or refine one open question, and choose the next three readings. Move an item to Revisit when you cannot explain its decision loop or key assumption; keep its earlier completion date as reading history.

For field updates, add promising resources to the inbox first, check their relevance and primary source, then add them to the [catalog](data/resources.json) and a category list. Keep research discovery separate from your learning progress.

| Date found | Candidate / primary link | Why it fits action-conditioned control | Publication / version checked | Decision and next action |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

No automated monitoring, reminders, or summary counters are enabled. This tracker is designed for direct editing in GitHub.
