# A focused reading path

Use checkpoints instead of a deadline. If a topic is already familiar, answer its checkpoint and move on.

| Stage | Read / watch | Question to answer in your own words |
|---|---|---|
| 1. Orientation | [Mental model](docs/01-mental-model.md), [equations](docs/02-key-equations.md), CS285 lectures 10–12 | What separates a forward model from a planner and a policy? |
| 2. Latent dynamics | PlaNet; skim Moerland survey | What is inferred from real observations, and what is predicted during imagination? |
| 3. Two uses of one model | Original Dreamer, then TD-MPC | How would you replace online trajectory optimization with actor training? What changes in the model? |
| 4. Model reliability | MBPO blog; 2026 uncertainty-and-control survey | Why can a planner prefer trajectories on which its model is wrong? |
| 5. Your JEPA focus | DINO-WM, V-JEPA 2-AC, LeWorldModel | What prevents collapse, preserves dynamics information, and makes goal distance useful? |
| 6. Task-aware abstraction | MuZero; Value Equivalence Principle | What does a model need to preserve for the particular decision algorithm? |
| 7. Current research | Bohg's 2026 talk; TD-JEPA; Reinforced Planning | Should progress estimation, search, or the representation be learned differently? |

## A compact first pass

Read the local introduction → PlaNet → Dreamer → TD-MPC → DINO-WM → LeWorldModel. Keep [the method map](docs/03-method-map.md) open and write one note per method.

## A current-research pass

Read [the recent control survey](https://link.springer.com/article/10.1007/s44163-026-02122-1), then select the Bohg/Hafner/LeCun sessions from [WM@Booth](https://wm-booth.org/). Follow with [TD-JEPA](https://arxiv.org/abs/2607.25337) and [Reinforced Planning](https://arxiv.org/abs/2608.18669). These recent preprints are leads for understanding open questions, not established replacements for all prior methods.

## Optional practical exercise

Use a small known control environment with vector observations. Fit a one-step dynamics model from random-policy data, compare real and predicted trajectories, then run short-horizon MPC. Compare its performance with different horizons and different data coverage. Only after the transition–planning loop is clear, replace the observed state with learned features.

Keep the task, real-data budget, and objective fixed when comparing methods. A toy experiment can explain a mechanism; it cannot establish a general benchmark claim.

[Reading tracker](TRACKER.md) · [Resource catalog](data/resources.json) · [Home](README.md)
