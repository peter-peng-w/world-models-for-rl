[Read the paper takeaways before starting](#paper-takeaways) — key ideas, reading focus, and questions for all 18 papers and surveys.

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


## Paper takeaways

Pre-reading briefs for all **15 research papers and 3 survey/tutorial papers** in the register. The seven T-series entries are blogs, lectures, workshops, or slides; their existing reading prompts remain above. Checked against the linked primary abstracts and author/project summaries on **2026-09-13**; these are orientation notes, not full-paper reviews or independent replications. “Focus” and “Question” are suggested reading tasks. Recent preprint summaries describe the authors' proposals, not established general conclusions.

### F01 — World Models

**Takeaway:** A large predictive model can supply compact visual and memory features to a small controller. The paper also demonstrates training a controller inside a learned latent environment and transferring it to the real task. [Author article](https://worldmodels.github.io/)

**Focus:** The vision–memory–controller split; action-conditioned recurrent prediction; which experiment trains the controller in the real environment versus the learned one. **Question:** How can a controller exploit an imperfect model, and what does adding stochasticity address?

### F02 — PlaNet

**Takeaway:** Learn dynamics from images, then choose actions by online planning in latent space. Its recurrent state-space model combines deterministic memory and stochastic state; multi-step training is intended to make predictions useful beyond one step. [Author project](https://planetrl.github.io/)

**Focus:** State inference versus imagined prediction; reward prediction; latent overshooting; the loop of optimize an action sequence, execute the first action, observe, and replan. **Question:** Why does a good image reconstruction not guarantee a good plan?

### F03 — MBPO

**Takeaway:** The way you use a model can matter as much as its accuracy. Short synthetic rollouts starting from real replay states can improve policy learning while limiting the damage from compounding model error. [Paper](https://arxiv.org/abs/1906.08253)

**Focus:** Branched rollout construction, rollout length, mixing real and synthetic data, and the gap between theoretical bounds and practical model usage. **Question:** Why can short model rollouts still help solve a long-horizon task? This is primarily model-generated data for policy optimization, not an online trajectory planner.

### P01 — Dreamer

**Takeaway:** Use latent imagination to train an actor and value function. The original Dreamer propagates gradients of imagined returns through learned dynamics; value estimates account for outcomes beyond the finite imagination horizon. [Paper](https://arxiv.org/pdf/1912.01603.pdf)

**Focus:** Separate model learning, behavior learning, and real interaction. Trace the actor objective and value targets, and distinguish finite rollouts from long-term return estimation. **Question:** What computation happens during training versus when the trained actor selects an action? Compare this directly with PlaNet.

### P02 — DreamerV3

**Takeaway:** The central contribution is making imagination-based RL work robustly across diverse domains with a shared configuration. Normalization, balancing, and target transformations stabilize the learning system; the model–actor–critic structure remains central. [Author preprint](https://arxiv.org/abs/2301.04104) · [2025 publication](https://www.nature.com/articles/s41586-025-08744-2)

**Focus:** Which stabilization choices handle varying observation, reward, and return scales; which ablations support them. **Question:** Does “one configuration across tasks” mean one jointly trained agent, or separate task training with shared hyperparameters? Do not conflate those claims. The preprint began in 2023; the tracker uses the 2025 publication year.

### P03 — TD-MPC

**Takeaway:** Combine short-horizon planning with a learned terminal value to estimate longer-term return. The latent dynamics model is task-oriented: useful predictions for reward and control matter more than reconstructing every visual detail. [Author project](https://www.nicklashansen.com/td-mpc/)

**Focus:** The joint model/value learning objective, latent consistency, and how the terminal value enters trajectory scoring. **Question:** How is work divided between the model, value function, policy, and trajectory optimizer? Compare online planning here with Dreamer's deployment actor.

### P04 — TD-MPC2

**Takeaway:** A series of improvements makes decoder-free latent MPC more robust and scalable, including broad continuous-control evaluation and multi-task agents. Treat it as a refinement and scaling of the TD-MPC recipe, not a completely different meaning of world model. [Author project](https://www.tdmpc2.com/)

**Focus:** Changes relative to TD-MPC, their ablations, and how tasks with different embodiments and action spaces are handled. **Question:** Which gains come from algorithm changes, model size, or more data? Separate single-task evaluation from the multi-task setting.

### P05 — MuZero

**Takeaway:** A planning model need not recreate observations. MuZero learns recurrent predictions of reward, value, and policy that support tree search, showing a powerful alternative to training a general observation predictor. [Paper](https://arxiv.org/abs/1911.08265)

**Focus:** Representation, recurrent dynamics, and prediction components; how search uses their outputs and supplies policy-training targets. **Question:** Which information can the hidden state discard while still supporting useful search? Avoid assuming its hidden states are a faithful simulator of the entire environment.

### P06 — Value Equivalence Principle

**Takeaway:** Two models can be equally useful for a specified planning problem even when their transition predictions differ. The formal criterion is matching Bellman updates for chosen sets of policies and value functions. [Paper](https://arxiv.org/abs/2011.03506)

**Focus:** The precise definition and its quantifiers. Increasing the policy/function sets makes equivalence more demanding. **Question:** What new tasks or policies could break an equivalence learned for a restricted set? This is stronger and more precise than saying two models have the same value under one policy.

### J01 — DINO-WM

**Takeaway:** Predict future pretrained DINOv2 patch features from offline action trajectories, then optimize action sequences toward the features of a goal image. This connects representation prediction directly to goal-directed control without requiring pixel reconstruction or a learned reward model. [Author project](https://dino-wm.github.io/)

**Focus:** What the pretrained encoder provides, what dynamics training learns, and how predicted features score candidate actions. **Question:** When might feature similarity disagree with reachability or task completion? “Zero-shot” refers to the described test-time behavior setting, not learning dynamics with no data.

### J02 — V-JEPA 2

**Takeaway:** Large-scale action-free video pretraining supplies representations, while a separate action-conditioned post-training stage produces V-JEPA 2-AC for robotic planning with image goals. Those stages answer different questions. [Paper](https://arxiv.org/abs/2506.09985)

**Focus:** Prioritize the action-conditioned model, robot trajectory data, planning objective, and deployment experiments over video recognition or question-answering benchmarks. **Question:** What can web video pretraining teach, and what still requires action-labeled interaction? Self-supervised representation learning alone is not an RL policy-learning algorithm.

### J03 — LeWorldModel

**Takeaway:** The authors propose end-to-end JEPA training from pixels using next-embedding prediction plus a regularizer encouraging Gaussian-distributed embeddings. The key issue is learning useful latent dynamics while avoiding collapsed representations, without relying on a large pretrained encoder. [Paper, v3](https://arxiv.org/abs/2603.19312v3)

**Focus:** The two losses, the role of the regularizer, and evidence connecting representation quality to actual planning. **Question:** Does preventing collapse also preserve every distinction needed for your task? Inspect control ablations rather than treating latent probes as sufficient evidence. This is a recent research proposal.

### R01 — Dreamer 4

**Takeaway:** The paper scales world-model-based behavior learning toward training an agent from offline data. It combines a fast predictive model with RL in imagination and reports long-horizon Minecraft behavior learned without additional environment interaction. [Paper](https://arxiv.org/abs/2509.24527)

**Focus:** Separate world-model training, action conditioning, and policy training. Read how shortcut forcing and the transformer design make repeated imagination practical. **Question:** What offline data and task supervision are available, and how is policy exploitation of model errors evaluated? For your interests, the imagined RL loop matters more than video appearance alone.

### R02 — Temporal-Distance JEPA

**Takeaway:** Accurate short-horizon feature prediction does not automatically give a useful measure of goal progress. The authors mine a directed temporal cost from offline trajectories, using it either as a planning cost or as a representation-training signal. [Paper, v2](https://arxiv.org/abs/2607.25337v2)

**Focus:** Same-trajectory temporal targets, heuristic cross-trajectory negatives, rollout consistency, and the distinction between deploying the learned cost and retaining Euclidean goal scoring. **Question:** Could trajectory order or missing transitions bias the inferred notion of progress? Treat the reported benchmark gains as preliminary evidence, not a universal planning advantage.

### R03 — Reinforced Planning with Latent World Models

**Takeaway:** Rather than only learning a policy or an evaluator, the authors train a neural optimizer to improve multi-step candidate plans. RP1 learns plan evaluation and plan revision offline using imagined rollouts from a pretrained latent world model. [Paper](https://arxiv.org/abs/2608.18669)

**Focus:** What the planner observes, what a plan-update action means, its reinforcement signal, and how it is coupled to the fixed world model. **Question:** Are comparisons fair after accounting for planner-training cost, model calls, and inference parallelism? Distinguish a learned search procedure from a policy that directly outputs environment actions. This is a recent preprint.

### S01 — Model-based Reinforcement Learning: A Survey

**Takeaway:** Model-based RL has two major design problems: learning a dynamics model and deciding how to use it. The survey organizes uncertainty, partial observability, abstraction, planning budgets, and integration with learning and acting. [Survey](https://arxiv.org/abs/2006.16712)

**Focus:** Use the taxonomy to classify PlaNet, Dreamer, TD-MPC, and MuZero. **Question:** If you hold the world model fixed and change its usage, which algorithmic properties change? Read it as the conceptual map for this collection, not as a source covering the latest 2026 methods.

### S02 — World models for physical AI with uncertainty representation and control

**Takeaway:** This survey organizes world models around six design dimensions and emphasizes their role in closed-loop decisions. It connects uncertainty treatment to compounding error, planner exploitation, rollout horizons, and calibration. [Survey](https://link.springer.com/article/10.1007/s44163-026-02122-1)

**Focus:** Prioritize state abstraction, temporal dynamics, uncertainty, and decision coupling. **Question:** Is a method modeling randomness in the environment, uncertainty from limited knowledge, or both—and how does that change the action? Skim broader physical-AI material unless it answers your control questions.

### S03 — From World Models to World Action Models

**Takeaway:** This tutorial clarifies terminology and compares approaches by representation, prediction, and interaction mechanisms. Its scope includes JEPA as well as spatial and simulation-oriented systems, so only part directly matches this repository's focus. [Tutorial, v8](https://arxiv.org/abs/2607.00836v8)

**Focus:** Translate each definition into familiar RL objects: state representation, forward dynamics, objective, policy, and planner. **Question:** Does “action” mean conditioning a prediction on controls, generating actions, or executing a planning loop? Avoid assuming every author's “world action model” denotes the same algorithm.

[Back to resource register](#resource-register) · [Back to top](#world-model-learning-tracker)
