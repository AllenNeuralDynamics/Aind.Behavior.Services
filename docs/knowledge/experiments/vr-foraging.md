---
type: Reference
title: VR Foraging — the flagship paradigm
description: The reference experiment built on the framework — a schema-first, closed-loop system for olfactory-cued virtual patch foraging in head-fixed mice. Covers the paradigm, its composable task families, the full task-design-to-analysis pipeline, and the repos involved.
resource: https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging
tags: [vr-foraging, flagship, reference, paradigm, pipeline]
timestamp: 2026-07-27T00:00:00Z
---

# VR Foraging — the flagship paradigm

VR Foraging is the most mature experiment on the framework and its reference implementation. Its white paper describes it as *"a schema-first, closed-loop system for olfactory-cued virtual patch foraging in head-fixed mice."* It is the paradigm that most sharply exercises every framework concept, and the two [`Aind.Experiment.*` composition repos](behavior-vs-experiment-repos.md) build on it. For the vocabulary, see the [domain glossary](../concepts/domain-glossary.md).

## The paradigm

A thirsty, head-fixed mouse runs on a treadmill; its locomotion drives forward motion through a rendered linear virtual corridor tiled into typed [virtual sites](../concepts/domain-glossary.md). Odor-cued patches deplete as they are harvested, so the animal must decide *when to leave* a patch and pay a *travel cost* to reach a fresher one. Two headline scientific claims motivate it: sensitivity to reward statistics, and cognition via stimulus–action dissociation (see the [glossary](../concepts/domain-glossary.md)).

## Not one task but a composable platform

The same grammar expresses several validated task families — new paradigms are new *configurations*, not new code:

- **Patch foraging** — multi-site odor-cued patches, reward depletes (and optionally replenishes); the animal decides when to leave.
- **Single-site, bandit-like** — each patch is one reward site; two reward odors with block-switching probabilities (matching-law / multi-armed bandit).
- **Memory-driven (rule learning)** — learning sets (Harlow "learning-to-learn", fresh daily odor pairs, win-stay/lose-shift) and deterministic reversals.

## How it materializes as software

The tripartite [rig/task/session](../concepts/rig-task-session.md) model is the only input to `src/main.bonsai`. The DSL is defined once in Pydantic (`task_logic.py` ≈ 1,200 lines, `rig.py`), compiled to JSON Schema, then to C# Bonsai operators via Bonsai.SGen (namespace `AindVrForagingDataSchema`) — [schema-first](../concepts/schema-first.md), with regeneration enforced in CI.

Hardware is the [Harp ecosystem](../ecosystem/bonsai-harp.md) on a shared clock: Behavior board, olfactometer(s), lickometer, treadmill with a controllable brake (programmable friction), sniff detector, White Rabbit clock generator, AIND motorized manipulator, triggered Spinnaker cameras. The [Bonsai](../ecosystem/bonsai-harp.md) runtime separates a hard-real-time hardware tier from a soft-real-time tier (VR rendering via BonVision/OpenGL + task logic) over a message bus, with live ImGui/ImPlot introspection.

Notably, `Aind.Behavior.VrForaging` is the **outlier in structure**: a `uv` *workspace* with separate `aind_behavior_vr_foraging` and `aind_behavior_vr_foraging_curricula` packages, rather than the single-package [canonical skeleton](anatomy-of-an-experiment-repo.md).

## The full pipeline (scientist's view)

1. **Configure** — author the three JSON documents via the Python authoring API (`examples/`). Validation happens before a session runs.
2. **Train** — automated shaping via `aind-behavior-vr-foraging-curricula` on the [curriculum](../ecosystem/curriculum.md) stack (the `depletion` ladder, etc.).
3. **Run** — launched via [clabe](../ecosystem/clabe.md) into `src/main.bonsai`.
4. **Data written** — under `behavior/`: Harp `*.harp` streams + `HarpCommands/`, `SoftwareEvents/`, `OperationControl/` CSVs, `Logs/` (launcher log + the three `*_input.json` snapshots), `behavior-videos/`. See [data contracts & standards](../concepts/data-contracts-and-standards.md).
5. **QC** — `vr-foraging data-qc <dataset>` runs [contraqctor](../ecosystem/contraqctor.md) suites against a versioned, self-describing data contract (`data_contract/v0_4_0.py … v1.py`, auto-selected by the session `version`).
6. **Standardize & upload** — `vr-foraging data-mapper` maps to `aind-data-schema` (`Acquisition` + `Instrument`), tagging stimulus epochs and summing consumed water; Allen sessions become AWS S3 assets within ~24h.
7. **Analyze** — the `Aind.Behavior.VrForaging.Dashboard` (Plotly/Dash, loads via contraqctor, builds trial tables via an NWB `TrialTableProcessor`).

## Repos in the VR Foraging family

- `Aind.Behavior.VrForaging` — core (PyPI `aind-behavior-vr-foraging`).
- `aind-behavior-vr-foraging-curricula` — training curricula.
- `Aind.Behavior.VrForaging.Dashboard` — session-review web app.
- `Aind.Behavior.VrForaging.Nwb` — NWB conversion.
- `Aind.Experiment.VrForaging-Fip`, `Aind.Experiment.VrForaging-OpenEphys` — [compositions](behavior-vs-experiment-repos.md) adding physiology.

# Citations
1. vr-foraging-white-paper `WHITEPAPER_DRAFT.md`
2. vr-foraging-white-paper `docs/context/repos-and-tools.md`
3. https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging
