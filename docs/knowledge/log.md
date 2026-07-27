# Change Log

## 2026-07-27
* **Initialization**: Created the OKF knowledge bundle for `aind-behavior-services` at `docs/knowledge/`.
* **Overview**: Authored [overview.md](overview.md) with the black-box model and the layered ecosystem (framework → clabe → experiment repos; contraqctor downstream).
* **Concepts**: Documented the [rig/task/session triad](concepts/rig-task-session.md), [schema-first codegen](concepts/schema-first.md), [versioning](concepts/versioning.md), [data contracts & standards](concepts/data-contracts-and-standards.md), and the [domain glossary](concepts/domain-glossary.md).
* **Ecosystem**: Documented [aind-behavior-services](ecosystem/aind-behavior-services.md), [clabe](ecosystem/clabe.md), [contraqctor](ecosystem/contraqctor.md), [curriculum](ecosystem/curriculum.md), and [Bonsai/Harp](ecosystem/bonsai-harp.md).
* **Experiments**: Documented the [repo anatomy](experiments/anatomy-of-an-experiment-repo.md), [behavior-vs-experiment repos](experiments/behavior-vs-experiment-repos.md), [VR Foraging](experiments/vr-foraging.md), and the [catalog](experiments/catalog.md).
* **Workflows**: Documented [authoring a schema](workflows/authoring-a-schema.md) and [running an experiment](workflows/running-an-experiment.md).
* **Refinement**: Clarified that the framework standardizes a *composable vocabulary* (base models, device/calibration models, distribution primitives, data-record types) rather than a single universal schema, and that this vocabulary grows additively as new paradigms need it ([overview](overview.md), [schema-first](concepts/schema-first.md)).
* **Standards**: Updated [data contracts & standards](concepts/data-contracts-and-standards.md) for the `SoftwareEvents` `.jsonl` extension ([#230](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/issues/230)) and UTC start/end markers ([#207](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/issues/207)).
* **Note**: Bundle authored against `aind-behavior-services` v0.13.7. Sibling repos surveyed on their `main` branch.
