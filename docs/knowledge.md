# Knowledge Base

The [ecosystem](ecosystem.md) page is the narrative, human-facing introduction. This page points instead at the **machine-readable knowledge base**: a structured tree of markdown files in the [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), one concept per file with typed front-matter, designed to be consumed by coding agents and tooling (though people are welcome to read it too). It captures the *why* and the *how-it-fits-together* of `aind_behavior_services` and the ecosystem it anchors, and lives under [docs/knowledge/](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/tree/main/docs/knowledge).

If you are reading as a human and want the guided tour, start with [ecosystem](ecosystem.md). If you want the structured reference, start with the [overview](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/overview.md) below and open only the concepts you need.

## Concepts

The ideas the framework standardizes:

- [The Rig / Task / Session triad](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/concepts/rig-task-session.md)
- [Schema-first code generation](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/concepts/schema-first.md)
- [Schema versioning](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/concepts/versioning.md)
- [Data contracts and dataset standards](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/concepts/data-contracts-and-standards.md)
- [Scientific domain glossary](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/concepts/domain-glossary.md)

## Ecosystem

The tools brought together:

- [aind-behavior-services (the framework package)](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/ecosystem/aind-behavior-services.md)
- [clabe (the launcher)](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/ecosystem/clabe.md)
- [contraqctor (data contracts + QC)](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/ecosystem/contraqctor.md)
- [The curriculum stack (training)](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/ecosystem/curriculum.md)
- [Bonsai and Harp (runtime + hardware)](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/ecosystem/bonsai-harp.md)

## Experiments

How concrete experiments materialize:

- [Anatomy of an experiment repository](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/experiments/anatomy-of-an-experiment-repo.md)
- [Aind.Behavior.* vs Aind.Experiment.* repositories](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/experiments/behavior-vs-experiment-repos.md)
- [VR Foraging — the flagship paradigm](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/experiments/vr-foraging.md)
- [Experiment repository catalog](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/experiments/catalog.md)

## Workflows

End-to-end playbooks:

- [Authoring or changing a schema](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/workflows/authoring-a-schema.md)
- [Running an experiment](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/blob/main/docs/knowledge/workflows/running-an-experiment.md)
