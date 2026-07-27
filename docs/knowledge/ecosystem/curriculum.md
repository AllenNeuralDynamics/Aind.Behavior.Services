---
type: Component
title: The curriculum stack — automated training
description: aind-behavior-curriculum (upstream base for Task) and the per-experiment curricula packages, which model training as a directed graph of stages where each stage is a complete task config and transitions are predicates over performance metrics.
resource: https://github.com/AllenNeuralDynamics/aind-behavior-curriculum
tags: [curriculum, training, curriculum-graph, shaping]
timestamp: 2026-07-27T00:00:00Z
---

# The curriculum stack — automated training

Curriculum handles **automated shaping/training**: moving an animal through increasingly demanding versions of a task based on its measured performance. Two roles:

- **`aind-behavior-curriculum`** — an *upstream* dependency of [aind-behavior-services](aind-behavior-services.md). The framework's `Task` / `TaskParameters` subclass this package's base `Task` / `Curriculum` and reuse its `SEMVER_REGEX`. So the dependency order is `aind-behavior-curriculum` → `aind-behavior-services`.
- **Per-experiment curricula** — e.g. `aind-behavior-vr-foraging-curricula`, which define the concrete training graphs for a paradigm.

## The model

A **curriculum is a directed graph of stages**:

- **Stage** — each stage *is* a complete task config (an [`AindFooTaskLogic`](../concepts/rig-task-session.md) instance). Progressing the curriculum means swapping in a different, fully-specified task config — not running different code.
- **Transition** — a predicate over performance metrics (rewards, choices, patch/site events) computed from the acquired dataset; when it evaluates true, the animal advances.
- **Policy** — refines stages within or across sessions.

Curricula are semver'd and changed only via reviewed PRs, making training **auditable**: the exact stage graph that trained an animal is recorded and versioned.

## Example: the VR Foraging `depletion` ladder

learn-to-run → learn-to-stop → stochastic reward → multiple odors with depletion → graduation. Other VR Foraging curricula include `depletion_stops_offset/rate`, `deterministic_reversals(_reward_capped)`, `learning_sets`, `replenishment_depletion_offset`, `single_site`, and `template`.

## How it plugs into a run

At launch, [clabe](clabe.md)'s `DefaultBehaviorPicker.pick_trainer_state(...)` loads the animal's current curriculum `TrainerState` instead of a fixed task, and a `CurriculumApp` can compute the next-stage suggestion after the session using metrics derived from the acquired data. See [running-an-experiment](../workflows/running-an-experiment.md).

# Citations
1. https://github.com/AllenNeuralDynamics/aind-behavior-curriculum
2. vr-foraging-white-paper `WHITEPAPER_DRAFT.md` §7 (training)
