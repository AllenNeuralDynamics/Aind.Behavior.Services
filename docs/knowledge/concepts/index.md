# Concepts

The ideas `aind-behavior-services` standardizes across every experiment. These are the load-bearing abstractions; the [ecosystem](../ecosystem/index.md) tools and [experiment repos](../experiments/index.md) are all built on them.

## Contents

- [rig-task-session.md](rig-task-session.md) — the three-schema decomposition of an experiment's parameters (the central organizing pattern).
- [schema-first.md](schema-first.md) — how one Pydantic definition compiles to JSON Schema and then to C#/Bonsai operators, keeping Python and the runtime in lockstep.
- [versioning.md](versioning.md) — `SchemaVersionedModel`, the two version fields stamped on every model, semver policy, and version coercion.
- [data-contracts-and-standards.md](data-contracts-and-standards.md) — the on-disk data contract: `SoftwareEvent`, Harp logging, dataset directory structure, and filename/datetime conventions.
- [domain-glossary.md](domain-glossary.md) — the scientific vocabulary (patch, virtual site, choice, reward dynamics…) that the software models.
