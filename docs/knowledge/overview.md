---
type: System Overview
title: The AIND Behavior Services framework and ecosystem
description: What aind-behavior-services is, the schema-first "black box" model of an experiment, and the layered ecosystem (framework → launcher → experiment repos; contraqctor downstream) that turns a paradigm into reproducible data.
resource: https://github.com/AllenNeuralDynamics/Aind.Behavior.Services
tags: [overview, architecture, ecosystem, schema-first]
timestamp: 2026-07-27T00:00:00Z
---

# The AIND Behavior Services framework and ecosystem

`aind-behavior-services` is a Python library for **defining and maintaining head-fixed mouse behavior experiments** at the Allen Institute for Neural Dynamics (AIND). It does not run experiments itself — it establishes the *contract* (the strongly-typed schemas) that every other tool in the stack reads and writes, and it brings a set of otherwise-independent tools (Pydantic, JSON Schema, Bonsai, Harp, aind-data-schema) into one coherent, reproducible pipeline.

## The core idea: an experiment is a black box `data = f(parameters)`

The framework's founding thesis (`docs/architecture.rst`) is that a single experiment run is a reproducible function: given a fully-specified set of parameters, it produces data. To make that function reproducible and verifiable, **every parameter is represented as a strongly-typed schema rather than an ad-hoc config file.** Schemas are authored once in Pydantic, compiled to JSON Schema (the language-neutral ground truth), and from there to C# operators that the Bonsai acquisition engine runs. The *same* schema drives Python-side metadata handling and the C#/Bonsai runtime, so the two can never silently drift. See [schema-first](concepts/schema-first.md).

The parameter space is deliberately decomposed into a **triad** — [rig / task / session](concepts/rig-task-session.md):

- **Rig** — the physical apparatus (devices, COM ports, calibrations).
- **Task** — what the animal experiences (the behavioral/software logic).
- **Session** — metadata for this one run (subject, experimenter, date, paths).

Every top-level model is [versioned](concepts/versioning.md) so a dataset carries the exact schema and package version that produced it.

Crucially, the framework does **not** define one universal schema that all experiments share. There is no single "behavior experiment" schema, and two paradigms are not expected to have the same `Rig` or `Task` shape. What is standardized is a *composable vocabulary* — the base models, device/calibration models, distribution primitives, and data-record types — that each experiment assembles into the schema it needs. That vocabulary is intentionally partial and **grows as needed**: a paradigm that needs a new device, distribution, or data type adds it to the shared library rather than forcing itself into an ill-fitting existing shape. See [schema-first](concepts/schema-first.md).

## The layered ecosystem

The framework sits deliberately in the middle of a stack. Dependencies point **downward** (each layer imports the one above; the reverse is never true):

```
aind-behavior-curriculum        (upstream: base Task / Curriculum)
        │
aind-behavior-services          THIS REPO — the schema contract + codegen
        │  defines Rig / Task / Session, device+calibration library,
        │  data-record standards, and the Pydantic→JSON-Schema→C# pipeline
        ├──────────────┬───────────────────────────────┐
        ▼              ▼                                ▼
     clabe        experiment repos                 contraqctor
   (launcher)   (Aind.Behavior.*,                (downstream: reads the
                 Aind.Experiment.*)               acquired data back in,
                 subclass Rig/Task,               validates against a data
                 own a Bonsai workflow            contract, runs QC)
```

- **[clabe](ecosystem/clabe.md)** — the launcher framework. Picks the rig/task/session configs, serializes them to JSON, shells out to Bonsai, then maps metadata to `aind-data-schema` and transfers/registers the data.
- **[Experiment repos](experiments/index.md)** — one repo per paradigm (VR Foraging, IsoForce, Telekinesis, …). Each subclasses `Rig` and `Task`, owns a `src/main.bonsai` acquisition workflow, and regenerates its C# from its Pydantic models. See the [repo anatomy](experiments/anatomy-of-an-experiment-repo.md).
- **[contraqctor](ecosystem/contraqctor.md)** — the downstream data layer: a declarative [data contract](concepts/data-contracts-and-standards.md) that describes what files a dataset should contain and how to load each, plus a lightweight QC test-suite framework to validate the loaded data.
- **[curriculum](ecosystem/curriculum.md)** — automated training. A curriculum is a graph of stages, each stage *is* a complete task config; transitions are predicates over performance metrics.
- **[Bonsai / Harp](ecosystem/bonsai-harp.md)** — the acquisition runtime and the hardware ecosystem the schemas ultimately configure.

## The end-to-end flow

1. **Author** the Pydantic models for a paradigm (subclass `Rig`, `Task`) and [regenerate](workflows/authoring-a-schema.md) the JSON Schema + C#.
2. **Configure** a run by instantiating/serializing rig + task + session to three JSON documents (optionally suggested by a [curriculum](ecosystem/curriculum.md)).
3. **Launch** via [clabe](ecosystem/clabe.md), which feeds those JSON files to the Bonsai workflow.
4. **Acquire** — Bonsai runs the closed loop, logging Harp binary streams, `SoftwareEvents`, videos, and config snapshots under a [standardized dataset layout](concepts/data-contracts-and-standards.md).
5. **QC** — [contraqctor](ecosystem/contraqctor.md) loads the data against a versioned contract and runs QC suites.
6. **Standardize & upload** — clabe maps metadata to `aind-data-schema` and transfers to cloud storage.

See [running-an-experiment](workflows/running-an-experiment.md) for the concrete playbook, and [VR Foraging](experiments/vr-foraging.md) for a fully worked example of a real paradigm.

## Why it exists (the through-line)

The framework amortizes engineering cost across paradigms: a new experiment is a new *configuration* of a composable grammar, not new code; every run is fully-specified, version-pinned data (reproducibility by construction); the same metadata that *describes* an experiment is what *instantiates* it (correct-by-construction metadata); and new devices/modalities are cheap to add via Bonsai's reactive model and Harp's sub-millisecond hardware synchronization.
