# Editable diagrams

## Learn and act

```mermaid
flowchart LR
  E[Environment] --> D[Observed action trajectories]
  D --> M[Learn action-conditioned dynamics]
  M --> P[Plan candidate actions]
  M --> I[Imagine policy-training rollouts]
  I --> A[Learn actor and critic]
  P --> E
  A --> E
```

## State estimation versus imagination

```mermaid
flowchart LR
  H[Real observation and action history] --> Z[Infer current latent state]
  Z --> F[Learned transition]
  A[Candidate action] --> F
  F --> N[Predicted next latent state]
  N --> R[Reward, value, or goal evaluation]
  N --> F2[Next imagined transition]
  A2[Next candidate action] --> F2
```

## A reading route

```mermaid
flowchart TD
  B[MBRL foundations] --> P[PlaNet: latent dynamics and MPC]
  P --> D[Dreamer: actor learning in imagination]
  P --> T[TD-MPC: short planning and terminal value]
  P --> J[DINO-WM and V-JEPA 2-AC: feature prediction]
  J --> L[LeWorldModel: end-to-end JEPA]
  L --> TD[TD-JEPA: planning-aware goal cost]
  T --> RP[Reinforced Planning: learn plan revision]
  B --> M[MuZero: recurrent model for search]
  M --> V[Value equivalence: what decisions require]
```

Arrows indicate a suggested learning sequence or conceptual connection, not a complete historical lineage.

[Figure index](README.md) · [Home](../README.md)
