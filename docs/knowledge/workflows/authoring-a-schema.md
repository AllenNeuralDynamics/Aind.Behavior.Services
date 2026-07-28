---
type: Playbook
title: Authoring or changing a schema
description: The procedure for defining or modifying the Pydantic models of a paradigm and regenerating the derived artifacts (JSON Schema + C#/Bonsai operators), keeping Python and the acquisition runtime in lockstep.
resource: src/aind_behavior_services/schema/__init__.py
tags: [playbook, schema, codegen, regenerate, workflow]
timestamp: 2026-07-27T00:00:00Z
---

# Authoring or changing a schema

This is the loop you run whenever a paradigm's parameters change. The golden rule of [schema-first](../concepts/schema-first.md): **edit the Pydantic model, never the generated artifacts.** JSON Schema and C# are always regenerated.

## When

Any time you add/remove/rename a field, add a device to a [`Rig`](../concepts/rig-task-session.md), or extend the task logic — in the framework repo *or* an [experiment repo](../experiments/anatomy-of-an-experiment-repo.md).

## Steps (in an experiment repo)

1. **Edit the model.** Change `src/<pkg>/rig.py` or `src/<pkg>/task_logic.py` (subclasses of the framework's `Rig` / `Task`). Reuse framework building blocks — the device+calibration library and `task.distributions`.
2. **Bump the version if the shape changed.** Update the model's `version` `Literal` default per SemVer ([versioning](../concepts/versioning.md)). This is what lets [contraqctor](../ecosystem/contraqctor.md) select the right data contract later.
3. **Regenerate.** Run the repo's `regenerate.py` (it collects the models into a `RootModel` and calls [`convert_pydantic_to_bonsai`](../concepts/schema-first.md)). This rewrites:
   - JSON Schema → `schema/` (or `src/DataSchemas/`)
   - C# → `src/Extensions/<Name>.Generated.cs`
4. **Rebuild the Bonsai `Extensions` assembly** so `main.bonsai` sees the new generated types (they are referenced via `clr-namespace:...;assembly=Extensions`). Update the workflow if you added new operators.
5. **Update the [data contract](../ecosystem/contraqctor.md)** in `data_contract/` if new output streams appear, and its `data_qc/` suites.
6. **Test & commit.** Run the repo's tests; CI enforces that regeneration is up to date (generated files must not drift from the models).

## Steps (in the framework repo itself)

The framework's own generators live under `src/_generators/` (the `generate` console script):

- `rig_harp.py` regenerates `rig/_harp_gen.py` from the harp-tech `whoami.yml` registry — run this when new Harp devices are published.
- `json_schema.py` writes `./schema/` for `Session`, `DataTypes`, `MessageProtocol`, `AindManipulator`.

## Prerequisites

`dotnet`, `Bonsai.Sgen` (`>= 0.6.0`), and `Harp.Toolkit` must be installed (Windows). See `docs/articles/requirements.rst`.

## Gotchas

- Never hand-edit `*.Generated.cs` — it is excluded from linting because it is machine output.
- Watch the known `schema/` vs `src/schemas` vs `src/DataSchemas/` path inconsistency in this repo's docs config when wiring generation output.

# Citations
1. src/aind_behavior_services/schema/__init__.py
2. src/_generators/ (rig_harp.py, json_schema.py)
3. Aind.Behavior.Telekinesis `src/aind_behavior_telekinesis/regenerate.py`
