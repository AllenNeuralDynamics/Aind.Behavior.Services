---
type: Convention
title: Aind.Behavior.* vs Aind.Experiment.* repositories
description: The distinction between a single self-contained acquisition unit (Aind.Behavior.<Task> / Aind.Physiology.Fip) and a thin composition wrapper (Aind.Experiment.<...>) that combines several units into one coordinated session via git submodules and concurrent Bonsai launches.
resource: https://github.com/AllenNeuralDynamics/Aind.Experiment.VrForaging-Fip
tags: [repo-structure, composition, submodules, physiology, convention]
timestamp: 2026-07-27T00:00:00Z
---

# Aind.Behavior.* vs Aind.Experiment.* repositories

There are two repository *kinds*, and telling them apart explains the whole "experiments materialize here" picture.

## `Aind.Behavior.<Task>` (and `Aind.Physiology.<Modality>`) — one acquisition unit

A self-contained acquisition unit: its own [schema package](anatomy-of-an-experiment-repo.md), its own `src/main.bonsai`, its own Bonsai executable. It follows the [canonical skeleton](anatomy-of-an-experiment-repo.md).

- **Behavior repos** define *both* `rig.py` and `task_logic.py` (there is a behavioral task).
- **Physiology repos** (`Aind.Physiology.Fip`) define a `Rig` but typically have **no `task_logic.py`** — physiology acquisition has hardware to configure but no behavioral task. A missing `task_logic` is a *common indicator* of a physiology (vs behavior) repo, **not a hard requirement** — it reflects that there is no task to model, not a rule the framework enforces. (`Aind.Behavior.JustFrames`, a video-acquisition benchmark, is similarly task-logic-light.)

## `Aind.Experiment.<...>` — a composition of units

A **thin composition wrapper** that combines multiple acquisition units into one coordinated session. Its layout is deliberately minimal and *different*:

- **No `src/`, `schema/`, or Bonsai of its own.**
- Component repos are pulled in as **git submodules** (`.gitmodules`) and wired as local path dependencies in `pyproject.toml`, e.g. `aind-behavior-vr-foraging = { path = "./Aind.Behavior.VrForaging" }`, `aind-physiology-fip = { path = "./Aind.Physiology.Fip" }` (with `[launcher, data]` extras), plus `aind-clabe`.
- A top-level `main.py` is the composed experiment.

### What a composition does

`Aind.Experiment.VrForaging-Fip/main.py` picks a **single shared** `AindBehaviorSessionModel`, picks the VR Foraging rig+task_logic (via `DataversePicker`) and the FIP rig (via a second `DefaultBehaviorPicker` pointed at the FIP config library), then launches **two `AindBehaviorServicesBonsaiApp` instances concurrently** — one per submodule's `src/main.bonsai` — with `await asyncio.gather(bonsai_app.run_async(), fip_app.run_async())`. Afterward it runs the VR Foraging [curriculum](../ecosystem/curriculum.md), behavior + FIP data mappers, and QC.

So: **an experiment = one shared session + N rigs + N Bonsai workflows run in parallel + combined post-processing.**

## The two composition repos surveyed

- `Aind.Experiment.VrForaging-Fip` (v0.2.0) — the more developed: dual-Bonsai concurrent launch, FIP `ProtoAcquisitionMapper`, curriculum, QC.
- `Aind.Experiment.VrForaging-OpenEphys` (v0.1.0) — earlier: single-Bonsai launch with an RPC client stubbed (`# TODO`), a third submodule (`Aind.Physiology.OpenEphys`) declared but not yet wired into `main.py`, and clabe pinned to a feature branch.

See the [catalog](catalog.md) for the full list and maturity notes.

# Citations
1. Aind.Experiment.VrForaging-Fip (`main.py`, `.gitmodules`, `pyproject.toml`)
2. Aind.Experiment.VrForaging-OpenEphys (`main.py`, `.gitmodules`)
