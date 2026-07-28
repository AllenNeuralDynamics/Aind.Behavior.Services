---
type: Component
title: aind-behavior-services (the framework package)
description: Package layout and public API of the framework itself — the base models (Rig/Task/Session), the device+calibration library, data-record standards, the schema-generation engine, and the build-time generators.
resource: src/aind_behavior_services
tags: [framework, package, api, pydantic]
timestamp: 2026-07-27T00:00:00Z
---

# aind-behavior-services (the framework package)

The framework package itself (PyPI `aind-behavior-services`, v0.13.7, MIT-licensed, Windows-focused, Python ≥3.11). It provides the schema contract and codegen but deliberately does **not** launch experiments — that is [clabe](clabe.md)'s job. See [schema-first](../concepts/schema-first.md) for the codegen story and [the triad](../concepts/rig-task-session.md) for the core models.

## Public API surface

`src/aind_behavior_services/__init__.py` re-exports: `Rig`, `Session`, `Task`, `SchemaVersionedModel`, `DefaultAwareDatetime`, `BonsaiSgenSerializers`, `convert_pydantic_to_bonsai`, and version constants.

## Package layout (`src/aind_behavior_services/`)

| Module | Responsibility |
|--------|----------------|
| `base.py` | `SchemaVersionedModel` ([versioning](../concepts/versioning.md)), `coerce_schema_version`, `DefaultAwareDatetime`. |
| `session/` | The `Session` model (per-run metadata). |
| `rig/` | Hardware config: `Rig`/`Device`/`DatedCalibration` bases, generated Harp devices (`_harp_gen.py`), and device+calibration modules (water valve, load cells, treadmill, olfactometer, manipulator, cameras, visual stimulation). |
| `task/` | `Task`/`TaskParameters` bases + the `distributions.py` samplable-distribution library. |
| `data_types.py` | Runtime data-record standards: `SoftwareEvent`, `RenderSynchState`, start/end payloads, `DataTypes`. See [data contracts](../concepts/data-contracts-and-standards.md). |
| `message_protocol.py` | Versioned inter-process message protocol (log/heartbeat) for Bonsai ↔ launcher. |
| `common.py` | Reusable geometric/primitive value types (`Point2f`, `Rect`, `Size`, `Circle`, `Vector2/3`, `LookUpTable`). |
| `schema/__init__.py` | The schema-generation engine (`CustomGenerateJsonSchema`, `convert_pydantic_to_bonsai`, `sgen_typename`/`SgenNamespace`). |
| `utils.py` | Case converters, Bonsai process launching (`run_bonsai_process`, `open_bonsai_process`), datetime helpers, `model_from_json_file`, `get_commit_hash`. |
| `_version.py` | `__version__` / `__semver__`. |

A separate build-only package `src/_generators/` holds the code generators (exposed as the `generate` console script). See [schema-first](../concepts/schema-first.md).

## Dependencies it brings together

Runtime: `pydantic` (schema authoring), `harp-python` (Harp data models), `aind-behavior-curriculum` (upstream `Task`/`TaskParameters`/`SEMVER_REGEX`), `gitpython` (commit-hash capture), `semver`. Build/codegen: `jinja2`, `requests`, `pyyaml`. It bridges to non-Python tooling: **Bonsai**, **Bonsai.SGen** (`dotnet` tool), **Harp** + the harp-tech whoami registry, FFMPEG, FLIR Spinnaker, and `aind-data-schema`.

## The one entry point

The only console script is `generate` → `_generators:main`, a build/maintenance CLI that regenerates schemas + C#. There is **no** experiment-running CLI here — launching is delegated to [clabe](clabe.md). What the package does provide toward launching are the low-level Bonsai process helpers in `utils.py` and the reproducibility fields on `Session`.

## Documentation

Docs are **Sphinx/RST** (`docs/`, furo theme, `autodoc_pydantic` + `sphinx-jsonschema`), published to GitHub Pages. Notable gaps at time of writing: the data-standard articles are all `0.1.0-draft`; there is no narrative doc for `message_protocol`, `common`, `task/distributions`, or the calibration models; and there is no in-repo end-to-end tutorial (the README points to the external experiment repos). These are the targets for the planned documentation refactor.
