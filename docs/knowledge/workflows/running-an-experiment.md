---
type: Playbook
title: Running an experiment
description: The end-to-end procedure for running a session — configure the rig/task/session, launch via clabe into Bonsai, acquire under the standardized dataset layout, QC with contraqctor, and standardize/upload via aind-data-schema.
resource: https://github.com/AllenNeuralDynamics/clabe
tags: [playbook, launch, acquisition, qc, upload, workflow]
timestamp: 2026-07-27T00:00:00Z
---

# Running an experiment

The runtime counterpart to [authoring a schema](authoring-a-schema.md). This is what happens (and what a rig operator does) to turn a configured paradigm into a reproducible, QC'd, uploaded dataset. Orchestrated by [clabe](../ecosystem/clabe.md).

## 1. Configure

The run's inputs are the three [rig/task/session](../concepts/rig-task-session.md) JSON documents. In practice a [picker](../ecosystem/clabe.md) loads them from a config-library directory:

- `pick_rig(AindFooRig)` — the calibrated rig for this machine.
- `pick_task(AindFooTaskLogic)` — **or** `pick_trainer_state(...)` when a [curriculum](../ecosystem/curriculum.md) drives the task (the picker loads the animal's current stage).
- `pick_session(Session)` — subject, experimenter, notes; clabe stamps `commit_hash` / `allow_dirty_repo` for reproducibility.

## 2. Launch

Run the repo's launcher (`clabe run …`, or the repo's `[project.scripts]` console command). The `Launcher`:

1. `validate()` — checks the git repo is clean (offers reset), sets up temp/log/session directories.
2. `register_session(session, rig.data_directory)` — establishes the session directory.
3. `ResourceMonitor` pre-flight (e.g. free disk on the data drive).
4. `AindBehaviorServicesBonsaiApp` serializes rig/session/task to temp JSON and launches `src/main.bonsai` with them as externalized `-p:RigPath=…` properties. In a [composition repo](../experiments/behavior-vs-experiment-repos.md) multiple apps run concurrently via `asyncio.gather`.

## 3. Acquire

[Bonsai](../ecosystem/bonsai-harp.md) deserializes the JSON into the generated C# types, instantiates hardware, and runs the closed loop, logging to the [standardized dataset layout](../concepts/data-contracts-and-standards.md) under `<AnimalId>_<Datetime>/behavior/`: Harp `*.harp` streams, `SoftwareEvents/`, `OperationControl/` CSVs, `Logs/` (launcher log + the three `*_input.json` config snapshots), and videos. The config snapshots make the dataset self-describing.

## 4. QC

Load the dataset against a versioned [contraqctor](../ecosystem/contraqctor.md) `Dataset` (auto-selected by the session `version`), `load_all()` to capture per-stream load errors, assert the contract with `ContractTestSuite`, and run QC suites via `Runner().run_all_with_progress(HtmlReporter(...))`. This runs in-repo so the operator gets an immediate integrity check (optional HTML report). Wired via the repo's `data_contract/` + `data_qc/` packages.

## 5. Standardize & upload

A `AindDataSchemaSessionDataMapper` subclass re-hydrates the `*_input.json` files and maps them to the `aind-data-schema` standard (`Acquisition` + `Instrument`), snapshotting the Bonsai/Python environment. Then `WatchdogDataTransferService` submits a job to the aind-data-transfer-service endpoint scheduling cloud upload + registration (`RobocopyService` is the local-copy alternative). `copy_logs()` archives the launcher logs into `<session>/Behavior/Logs/.launcher`. Allen Institute sessions become AWS S3 data assets within ~24 h.

## 6. Analyze

Downstream review tools (e.g. the `Aind.Behavior.VrForaging.Dashboard`) load the dataset via contraqctor and build analysis views. Post-session, a `CurriculumApp` can compute the animal's next [curriculum](../ecosystem/curriculum.md) stage from performance metrics.

## Variations

- **Frontend**: console, TUI, or TUI-over-web (`clabe serve`); or remote via `clabe xml-rpc-server`.
- **Per-animal state**: a `ByAnimalModifier` injects/persists stateful rig fields (e.g. manipulator start position).
- **Compositions**: see [behavior-vs-experiment](../experiments/behavior-vs-experiment-repos.md).

# Citations
1. clabe `examples/behavior_launcher.py`
2. Aind.Behavior.VrForaging `scripts/aind.py`; Aind.Experiment.VrForaging-Fip `main.py`
