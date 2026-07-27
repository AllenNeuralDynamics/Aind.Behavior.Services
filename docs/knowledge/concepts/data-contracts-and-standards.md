---
type: Convention
title: Data-record contracts and dataset standards
description: The on-disk contract a session produces — the SoftwareEvent record standard, Harp binary logging, the dataset directory layout, and filename/datetime conventions — and how these become the input to contraqctor's data contract.
resource: docs/articles
tags: [data-contract, software-events, harp, dataset-structure, conventions, standards]
timestamp: 2026-07-27T00:00:00Z
---

# Data-record contracts and dataset standards

The framework standardizes not just experiment *inputs* (the [triad](rig-task-session.md)) but the *outputs* — the shape of the data a session writes to disk. These standards are what [contraqctor](../ecosystem/contraqctor.md) later reads against a [data contract](../ecosystem/contraqctor.md) and QCs.

## Data-record schemas

Defined in `src/aind_behavior_services/data_types.py`:

- **`SoftwareEvent`** — the universal, generic (`T`-payload) software-event wrapper. It is the standard record for anything the task logic emits at runtime (choices, reward deliveries, state changes). It is mirrored isomorphically by the C# `AllenNeuralDynamics.AindBehaviorServices` Bonsai NuGet package, and `contraqctor` parses it via `SoftwareEvents(ManyPydanticModel[SoftwareEvent])`. On disk, events are demultiplexed by name into per-event **`.jsonl`** files ([JSON Lines](https://jsonlines.org/) — one JSON object per line; changed from `.json` per [issue #230](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/issues/230)). Experiment start/end are recorded as `StartExperimentPayload` / `EndExperimentPayload` events (with UTC OS-derived timestamps recommended; [#207](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/issues/207)).
- `RenderSynchState`, `StartExperimentPayload`, `EndExperimentPayload`, and the `DataTypes` aggregate, plus `DataType` / `TimestampSource` enums.

A separate versioned **`message_protocol.py`** (`PROTOCOL_VERSION = 0`) defines an inter-process message protocol (request/reply/event `MessageType`, `LogPayload`/`HeartbeatPayload`) used for logging and heartbeat between processes — e.g. Bonsai ↔ launcher.

## Harp binary logging

`docs/articles/data_formats/harp.rst` standardizes how Harp device data is logged: a per-device de-multiplexed binary directory (`<Device>.harp`) and the clock-synchronization model (`Standalone` vs `Synchronized`). Harp devices share a common hardware clock, giving sub-millisecond, drift-corrected alignment across streams. See [Bonsai/Harp](../ecosystem/bonsai-harp.md).

## Dataset structure and filename conventions

Two draft standards under `docs/articles/core/`:

- **`dataset_structure.rst`** — the on-disk layout: `<AnimalId>_<Datetime>/<Modality>/...`, with the config snapshots (`session_input.json`, `rig_input.json`, `task_input.json`) written into a Logs/Metadata folder so the dataset is self-describing and can be re-hydrated.
- **`conventions.rst`** — ISO-8601 timezone-aware datetimes (`YYYY-MM-DDTHHMMSS[Z]`), underscore separators, and tabular/CSV rules. The `DefaultAwareDatetime` type and the `utils.py` datetime helpers (`format_datetime`, `utcnow`, `tznow`) enforce this in code.

## What a VR-Foraging-style session writes

A concrete session (see [VR Foraging](../experiments/vr-foraging.md)) produces, under `behavior/`: Harp device streams (`*.harp`) + `HarpCommands/`, `SoftwareEvents/` (JSON task-logic events), `OperationControl/` CSVs (position, is-stopped, torque, renderer sync), `Logs/` (launcher log + the three `*_input.json` config snapshots), and `behavior-videos/`. This directory *is* the input to a [contraqctor `Dataset`](../ecosystem/contraqctor.md).

## Status

The data-standard articles (`conventions`, `dataset_structure`, `harp`, `software_events`) are all marked `0.1.0-draft` — a natural target for the planned documentation refactor. The framework is also designed to interoperate with `aind-data-schema` (the `harp.rst` article documents the relationship); [clabe](../ecosystem/clabe.md) does the mapping to that standard at upload time.

# Citations
1. src/aind_behavior_services/data_types.py
2. src/aind_behavior_services/message_protocol.py
3. docs/articles/data_formats/harp.rst
4. docs/articles/core/dataset_structure.rst
5. docs/articles/core/conventions.rst
6. docs/articles/data_formats/software_events.rst
