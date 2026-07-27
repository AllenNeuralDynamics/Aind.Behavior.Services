---
type: Component
title: clabe — the experiment launcher framework
description: The Command-Line-interface Launcher for AIND Behavior Experiments — a downstream consumer of aind-behavior-services that picks rig/task/session configs, runs Bonsai and other apps, maps metadata to aind-data-schema, and transfers/registers data.
resource: https://github.com/AllenNeuralDynamics/clabe
tags: [launcher, clabe, orchestration, data-transfer]
timestamp: 2026-07-27T00:00:00Z
---

# clabe — the experiment launcher framework

**clabe = "Command-Line-interface Launcher for AIND Behavior Experiments"** (PyPI `aind-clabe`, import name `clabe`; the renamed successor of the old `Aind.Behavior.ExperimentLauncher`). It is a **downstream consumer** of [aind-behavior-services](aind-behavior-services.md) — it depends on it (`aind_behavior_services>=0.13.0`) and passes `Rig`/`Session`/`Task` models around as its currency; the framework knows nothing about clabe. The [experiment repos](../experiments/index.md) import clabe to build their launcher scripts, so the layering is: **framework (schemas) → clabe (launcher) → experiment repos**.

## What it does

clabe orchestrates a linear, modular, UI-agnostic workflow for running an experiment on a rig: **validate environment → pick configs → run apps (Bonsai) → map metadata → transfer/register data.** Every prompt and notification flows through a `Frontend` (console, TUI, or TUI-over-web), and it can also be driven remotely over XML-RPC.

## Key modules and abstractions (`src/clabe/`)

| Module | Provides |
|--------|----------|
| `launcher/` | `Launcher` (the orchestration core: session registration, directories, logging, git validation, `run_experiment()`), `LauncherCliArgs`, and the `@experiment` decorator for discoverable experiment functions. |
| `apps/` | `BonsaiApp` and **`AindBehaviorServicesBonsaiApp`** (serializes the picked rig/session/task to temp JSON and launches the Bonsai workflow with them as `-p:RigPath=…` externalized properties), `PythonScriptApp`, `CurriculumApp`, and a `Command`/`Executor` model. |
| `pickers/` | `DefaultBehaviorPicker` (picks rig/session/task/trainer-state from a config-library directory), `ByAnimalModifier` (per-animal stateful fields), `DataversePicker`. |
| `data_mapper/` | `AindDataSchemaSessionDataMapper` / `AindDataSchemaRigDataMapper` (abstract — experiment repos subclass) that convert models into `aind-data-schema` metadata, snapshotting the Bonsai/Python environment. |
| `data_transfer/` | `RobocopyService` (local copy) and `WatchdogDataTransferService` (submits a job to aind-data-transfer-service via aind-watchdog). |
| `resource_monitor/` | Pre-flight checks (e.g. free-disk constraint from the rig's data drive). |
| `ui/` | The `Frontend` abstraction: `ConsoleFrontend`, `TextualFrontend`, `notify()`, and typed prompt requests. |
| `runnable/`, `services.py`, `git_manager/`, `xml_rpc/`, `web.py` | The `@runnable` decorator (spinner/logging/report tiers), YAML-backed `ServiceSettings`, git wrapper, remote RPC, and TUI-over-web. |

## The end-to-end run

`clabe run my_experiment.py [--frontend tui|console] [--allow-dirty]` → `Launcher.validate()` (git clean, temp/log dirs) → a `Picker` loads `Rig`/`Session`/`Task` (+ curriculum `TrainerState`) from a config library and `register_session()` establishes the session directory → `ResourceMonitor` pre-flight → `AindBehaviorServicesBonsaiApp` serializes the models and launches Bonsai (multiple apps can run concurrently via `asyncio.gather`) → a data mapper produces `aind-data-schema` metadata → `WatchdogDataTransferService` schedules cloud upload/registration → `copy_logs()` archives launcher logs into `<session>/Behavior/Logs/.launcher`.

AIND-cloud integrations (`aind-data-schema`, `aind-data-transfer-service`, `aind-watchdog-service`, auth) are quarantined behind the optional `aind-services` extra so core clabe stays lean.

## Where to look

- `examples/behavior_launcher.py` — the canonical full demo.
- `docs/articles/` — conceptual guides: `frontends.md`, `runnables.md`, `service_settings.md`, `logging.md`.
- A real launcher: `Aind.Behavior.VrForaging/scripts/aind.py`. See the [launcher pattern](../experiments/anatomy-of-an-experiment-repo.md).

# Citations
1. https://github.com/AllenNeuralDynamics/clabe
2. clabe `src/clabe/launcher/_base.py`, `src/clabe/apps/_bonsai.py`
