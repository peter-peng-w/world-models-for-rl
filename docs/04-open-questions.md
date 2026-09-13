# 4. What to watch in new papers

## Prediction loss versus control utility

A low average prediction error can hide mistakes precisely where the planner needs accuracy. Ask whether the model ranks candidate actions correctly, not just whether it predicts a held-out logged trajectory. The [2026 uncertainty-and-control survey](https://link.springer.com/article/10.1007/s44163-026-02122-1) discusses planner exploitation, calibration, and compounding error.

## Representation and the planning objective

Embedding prediction must preserve controllable factors and relevant memory. A representation useful for classification may omit small changes crucial for control. A goal distance also needs useful geometry: a nearby embedding is not necessarily reachable in a few actions. [Temporal-Distance JEPA](https://arxiv.org/abs/2607.25337) is a recent preprint studying this train–plan mismatch.

## Planning horizon and uncertainty

Longer rollouts increase computational cost and expose model error. Shorter rollouts rely more on terminal values or frequent replanning. Stochastic transition uncertainty and uncertainty from missing data require different treatment. Inspect whether confidence predicts control failure, not only whether an ensemble disagrees.

## Learned search versus a learned actor

An actor selects actions directly. A learned optimizer revises candidate action sequences. A policy may also propose candidates to a hand-designed optimizer. These are different ways to allocate computation. [Reinforced Planning](https://arxiv.org/abs/2608.18669) investigates learning plan revision from imagined rollouts; its results are preliminary research evidence, not a settled ranking.

## Evaluation questions

For any claimed improvement record:

1. Real interaction budget; offline dataset size and behavior coverage.
2. Same-environment evaluation versus new goals, layouts, dynamics, or embodiments.
3. Observation modality and privileged state access, at both training and test time.
4. Training cost, planner latency, model calls per decision, and hardware.
5. Return or success, variability across seeds, and failure cases.
6. Whether baselines receive comparable data and planning compute.
7. Whether uncertainty, robustness, and closed-loop performance are actually measured.

## Suggested research questions

- Which representation distinctions are necessary for policy evaluation across many rewards?
- Can reward-free pretraining retain all the controllable information needed by downstream tasks?
- When does an actor outperform online search at a fixed total compute budget?
- What stops the planner from exploiting errors in a frozen world model?
- How should latent goal distance incorporate reachability and uncertainty?
- Can the same model support both transferable goal planning and task-specific value learning?

[Home](../README.md)
