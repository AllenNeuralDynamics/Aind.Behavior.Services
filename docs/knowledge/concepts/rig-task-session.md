---
type: Data Model
title: The Rig / Task / Session triad
description: The central pattern that decomposes an experiment's parameters into three strongly-typed schemas — Rig (hardware), Task (behavior logic), Session (per-run metadata) — and how experiment repos subclass them.
resource: src/aind_behavior_services
tags: [schema, rig, task, session, data-model, core]
timestamp: 2026-07-27T00:00:00Z
---

# The Rig / Task / Session triad

Rather than one monolithic "all parameters" object, the framework splits an experiment's full specification into **three independent, strongly-typed schemas**. This is the central organizing pattern of the whole ecosystem (`docs/architecture.rst`). The three together are the *only* inputs a Bonsai acquisition workflow requires.

| Schema | Answers | Base class | Subclassed per experiment? |
|--------|---------|------------|----------------------------|
| **Rig** | *What is the physical apparatus?* | `rig.Rig` | **Yes** — each repo defines its own |
| **Task** | *What does the animal experience?* | `task.Task` | **Yes** — each repo defines its own |
| **Session** | *What is this one run?* | `session.Session` | No — used as-is |

## Rig — hardware configuration

Defined in `src/aind_behavior_services/rig/_base.py`. `Rig` is a [versioned model](versioning.md) carrying `computer_name`, `rig_name`, and `data_directory`. It is composed from a **device + calibration library** the framework ships:

- `Device` base (has `device_type` and an optional polymorphic `calibration`) and `DatedCalibration` base.
- Auto-generated Harp device classes (`rig/_harp_gen.py`, one class per Harp board keyed by `who_am_i`) re-exported through `rig/harp.py`, plus `validate_harp_clock_output`.
- Device+calibration modules: `water_valve.py` (with `calibrate_water_valves` linear regression), `load_cells.py`, `treadmill.py`, `olfactometer.py`, `aind_manipulator.py`, `cameras.py` (FLIR/Spinnaker + FFMPEG presets), `visual_stimulation.py`.

An experiment repo declares `class AindFooRig(Rig)` and populates it with the devices its rig actually has. See [anatomy-of-an-experiment-repo](../experiments/anatomy-of-an-experiment-repo.md).

## Task — behavioral/software logic

Defined in `src/aind_behavior_services/task/__init__.py`. `Task` subclasses `aind_behavior_curriculum.task.Task` (see [curriculum](../ecosystem/curriculum.md)) and holds `task_parameters` plus a schema `version`. `TaskParameters` adds an `rng_seed` and a package-version pin. The task tree is abstracted away from hardware — it describes *what the animal experiences*, not *which board drives it*. The framework provides reusable building blocks, notably the `task/distributions.py` library of samplable probability-distribution schemas (`DistributionFamily`, `TruncationParameters`, `ScalingParameters`, …) used to parameterize stochastic task variables.

## Session — per-run metadata

Defined in `src/aind_behavior_services/session/__init__.py`. Captures `subject`, `experimenter`, `date`, `notes`, `commit_hash`, `allow_dirty_repo`, `skip_hardware_validation`, and auto-generates `session_name` as `{subject}_{datetime}`. Unlike Rig and Task it is used directly, not subclassed. Its reproducibility fields (`commit_hash`, `allow_dirty_repo`) are populated at launch time by [clabe](../ecosystem/clabe.md).

## Why three, not one

The split lets the pieces vary independently and be reused: a rig is calibrated once and paired with many tasks; a task definition is hardware-agnostic and can run on any conforming rig; a session is the only thing that changes run to run. It also mirrors how the work is divided — a rig engineer owns the `Rig`, a scientist owns the `Task`, and the launcher owns the `Session`.

# Examples

A concrete experiment materializes the triad like this (paraphrased from the experiment repos; see [catalog](../experiments/catalog.md)):

```python
# in an experiment repo, e.g. src/aind_behavior_telekinesis/
from aind_behavior_services.rig import Rig
from aind_behavior_services.task import Task, TaskParameters

class AindBehaviorTelekinesisRig(Rig):          # subclass Rig, add devices
    ...

class AindTelekinesisTaskParameters(TaskParameters):
    ...

class AindBehaviorTelekinesisTaskLogic(Task):   # subclass Task
    task_parameters: AindTelekinesisTaskParameters
```

At launch, instances of these three are serialized to `rig_input.json`, `task_input.json`, and `session_input.json` and handed to the Bonsai workflow.
