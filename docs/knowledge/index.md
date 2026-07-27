# AIND Behavior Services — Knowledge Bundle

This bundle captures the *why* and the *how it fits together* of `aind-behavior-services` and the ecosystem it anchors: a schema-first framework for defining, launching, acquiring, and validating head-fixed mouse behavior experiments at the Allen Institute for Neural Dynamics (AIND).

Start with [overview.md](overview.md) for the end-to-end mental model, then open only the concepts you need. It is written for both humans and agents working across `aind-behavior-services` and its sibling repositories.

## Contents

- [overview.md](overview.md) — what the framework is, the black-box model, and the layered ecosystem it sits in. **Read this first.**
- [concepts/](concepts/index.md) — the ideas the framework standardizes: the rig/task/session triad, schema-first codegen, versioning, data contracts & standards, and the scientific glossary.
- [ecosystem/](ecosystem/index.md) — the tools brought together: the framework itself, `clabe` (launcher), `contraqctor` (data contract + QC), the curriculum stack (training), and Bonsai/Harp (acquisition + hardware).
- [experiments/](experiments/index.md) — how concrete experiments materialize: the canonical repo skeleton, `Aind.Behavior.*` vs `Aind.Experiment.*`, the flagship VR Foraging paradigm, and the repo catalog.
- [workflows/](workflows/index.md) — end-to-end playbooks: authoring a schema and running an experiment.
- [log.md](log.md) — change history for this bundle.
