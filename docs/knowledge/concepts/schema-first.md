---
type: Convention
title: Schema-first — one Pydantic definition, three artifacts
description: How a single Pydantic model compiles to JSON Schema (the language-neutral ground truth) and then to C#/Bonsai operators via Bonsai.SGen, so Python metadata handling and the Bonsai acquisition runtime can never drift.
resource: src/aind_behavior_services/schema/__init__.py
tags: [schema, codegen, bonsai, json-schema, sgen, core]
timestamp: 2026-07-27T00:00:00Z
---

# Schema-first — one Pydantic definition, three artifacts

Schema-first is the design decision that makes the whole framework cohere: **Pydantic is the single source of truth**, and everything else is a derived artifact regenerated from it. A model authored once in Python produces:

1. the **Python** classes used for validation and metadata handling,
2. a **JSON Schema** — the language-neutral data contract, and
3. **C# Bonsai operators** — the strongly-typed representation the acquisition runtime uses.

Because (2) and (3) are *generated*, the Python model and the running Bonsai workflow are two views of the same schema and cannot silently diverge. Regeneration is a maintenance step enforced in CI.

## What is standardized (and what isn't)

Schema-first standardizes the *process and the vocabulary*, not a single universal document. The framework does not ship one fixed schema that every experiment must match — each paradigm defines its own `Rig` and `Task` shapes (see [the triad](rig-task-session.md)). What is shared is the authoring pattern (Pydantic → JSON Schema → C#) and a library of reusable building blocks: base models, device/calibration models, distribution primitives, common value types, and data-record types. This vocabulary is partial by design and grows additively — a paradigm that needs a new element adds it to the shared library for others to reuse, rather than forcing itself into an ill-fitting existing shape.

## The pipeline

```
Pydantic model  ──►  JSON Schema  ──►  C# *.Generated.cs  ──►  Bonsai workflow
   (author)          (ground truth)     (Bonsai.SGen)          (acquisition)
```

The engine lives in `src/aind_behavior_services/schema/__init__.py`:

- **`convert_pydantic_to_bonsai(model, ...)`** writes the JSON schema (default `./src/DataSchemas/`) and then invokes `bonsai_sgen(...)`, which shells out to `dotnet tool run bonsai.sgen` to emit `*.Generated.cs` (default `./src/Extensions/`). Requires `Bonsai.Sgen >= 0.6.0`.
- **`CustomGenerateJsonSchema`** tailors Pydantic's JSON Schema output for downstream C#/NJsonSchema interoperability. Key customizations:
  - nullable → `oneOf` (not `anyOf`); unions flattened to `oneOf`;
  - enums emit `x-enumNames` (PascalCase) for C# name generation; single-member enums become `const`;
  - `x-sgen-typename` injection via the `sgen_typename` decorator and the `SgenNamespace` helper — stamps a model with the fully-qualified C# type name Bonsai.SGen should use. Three mechanisms cover regular BaseModels (via `create_model` + a metaclass that strips the typename from subclasses so each must re-opt-in), plain classes/enums (an attribute), and frozen types like `TypeAliasType` (an annotation marker).
  - `export_schema()` can drop the root wrapper (`remove_root`); `x-abstract` marks aggregate/abstract models.

## The build-time generators

Two entry points under the build-only `src/_generators/` package (exposed as the `generate` console script in `pyproject.toml`):

- `src/_generators/rig_harp.py` — fetches the harp-tech `whoami.yml` device registry over HTTP and code-generates `rig/_harp_gen.py` (one Pydantic class per Harp board) from a Jinja2 template. This keeps the Harp device library in sync with the upstream community registry.
- `src/_generators/json_schema.py` — writes JSON Schemas to `./schema/` for `Session`, `DataTypes`, `MessageProtocol`, and `AindManipulator`. (Confirmed outputs: `schema/session.json`, `schema/data_types.json`, `schema/message_protocol.json`, `schema/aind_manipulator.json`.)

## How experiment repos use it

Each experiment repo has its own `regenerate.py` that collects its models (`task_logic`, `rig`, `Session`, plus extras) into a `RootModel` and calls `convert_pydantic_to_bonsai(...)`, emitting JSON Schema to `schema/` (or `src/DataSchemas/`) and C# to `src/Extensions/<Name>.Generated.cs` with a `cs_namespace` like `AindBehaviorTelekinesisDataSchema`. The Bonsai workflow references the generated types via `clr-namespace:...;assembly=Extensions`. See [authoring-a-schema](../workflows/authoring-a-schema.md) for the step-by-step.

## Gotchas

- `*.Generated.cs` is machine-generated (excluded from codespell in every repo). Never hand-edit it — change the Pydantic model and regenerate.
- There is a known path inconsistency in this repo's docs build between `./schema/`, `src/schemas`, and `src/DataSchemas/` defaults — worth reconciling when the docs are refactored.

# Citations
1. src/aind_behavior_services/schema/__init__.py
2. src/_generators/rig_harp.py
3. src/_generators/json_schema.py
