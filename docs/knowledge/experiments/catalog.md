---
type: Reference
title: Experiment repository catalog
description: The surveyed experiment repositories built on aind-behavior-services, what each declares, whether it has task logic, and its relative maturity — a map for finding the right reference implementation.
resource: https://github.com/AllenNeuralDynamics
tags: [catalog, repos, maturity, reference]
timestamp: 2026-07-27T00:00:00Z
---

# Experiment repository catalog

The repositories built on [aind-behavior-services](../ecosystem/aind-behavior-services.md), surveyed on `main`. All pin the framework to the same `0.13.x` line. Use this to pick the right reference implementation. See [repo anatomy](anatomy-of-an-experiment-repo.md) and [behavior-vs-experiment](behavior-vs-experiment-repos.md) for the patterns.

## Single-unit repos (`Aind.Behavior.*`, `Aind.Physiology.*`)

| Repo | PyPI / package | Services pin | Task logic? | Maturity |
|------|----------------|--------------|-------------|----------|
| **Aind.Behavior.VrForaging** | `aind-behavior-vr-foraging` | via workspace | Yes | **Most mature / reference.** `uv` workspace with a separate curricula package, data mappers, MkDocs, curriculum + RPC, richest `Extensions/`. |
| **Aind.Behavior.Telekinesis** | `aind-behavior-telekinesis` | `>=0.13.5,<0.14` | Yes | Mature, clean, copier-templated. Best example of the *current* canonical single-task repo; uses the newer `@experiment()` decorator + `clabe.ui`. |
| **Aind.Behavior.DynamicForaging** | `aind-behavior-dynamic-foraging` | `>=0.13.5` | Yes | Rich but structurally divergent: `task_logic/` split into `interventions/`, `trial_generators/`, `trial_models.py`; uses scikit-learn; Sphinx docs. `main` checked out in a worktree. |
| **Aind.Behavior.IsoForce** | `aind-behavior-iso-force` | `>=0.13.5` | Yes | Solid mid-tier; single package, versioned `data_contract/v0_1_0.py`. Version `0.1.0rc0` (earlier stage). |
| **Aind.Behavior.JustFrames** | `aind-behavior-just_frames` | `>=0.13.6` | No (rig-only-ish) | Leaner, benchmark-oriented (online video acquisition/encoding). Defines `AindJustFramesRig` + `SatelliteRig`; schema under `src/DataSchemas/`. |
| **Aind.Physiology.Fip** | `aind-physiology-fip` | `>=0.13.0` | **No** (physiology) | Mature physiology repo; rig-only, rich C# FIP operators + data mappers; schema under `src/DataSchemas/`. |

## Composition repos (`Aind.Experiment.*`)

| Repo | Version | Composes (submodules) | Maturity |
|------|---------|-----------------------|----------|
| **Aind.Experiment.VrForaging-Fip** | 0.2.0 | Aind.Behavior.VrForaging + Aind.Physiology.Fip | More developed: dual-Bonsai concurrent launch, FIP mapper, curriculum, QC. |
| **Aind.Experiment.VrForaging-OpenEphys** | 0.1.0 | + Aind.Physiology.OpenEphys | Earlier: single-Bonsai launch, RPC client stubbed, third submodule declared but not yet wired; clabe pinned to a feature branch. |

## How to read the "task logic?" column

A repo with **both** `rig.py` and `task_logic.py` is a behavior task. A repo with a `Rig` but **no** `task_logic.py` is *usually* a physiology/acquisition unit — a common indicator, **not a requirement**, as described in [behavior-vs-experiment](behavior-vs-experiment-repos.md).

## VR Foraging leads; the rest follow

[VR Foraging](vr-foraging.md) is the **reference implementation**: the most mature repo and the one where the framework's patterns are worked out first. The other behavior repos are **expected to converge on the same conventions** over time (workspace layout, curricula, data mappers, the newer clabe launcher API). Divergences noted in the table above are generally *maturity gaps*, not deliberate alternatives — when in doubt, follow what VR Foraging does.

## Recommended references

- **Learning the canonical pattern** → `Aind.Behavior.Telekinesis` (cleanest current single-task repo).
- **Seeing the full-power version / where the rest are heading** → `Aind.Behavior.VrForaging`.
- **Seeing composition** → `Aind.Experiment.VrForaging-Fip`.
