---
type: Convention
title: Schema versioning and version coercion
description: How SchemaVersionedModel stamps every top-level model with a schema version and a package version, the SemVer policy, and how coerce_schema_version reconciles deserialized data with the model's declared version.
resource: src/aind_behavior_services/base.py
tags: [versioning, semver, reproducibility, schema]
timestamp: 2026-07-27T00:00:00Z
---

# Schema versioning and version coercion

Reproducibility requires that a dataset carry the exact schema that produced it. The framework enforces this with **`SchemaVersionedModel`** (`src/aind_behavior_services/base.py`), the base class every top-level model ([Rig, Task, Session](rig-task-session.md), and the data-record models) inherits.

## The two version fields

Every versioned model is stamped with two frozen, SemVer-validated fields:

- **`version`** — the schema version of *this model* (its declared `Literal` default). Bumped by the schema author when the model's shape changes.
- **`aind_behavior_services_pkg_version`** — pinned to the installed framework's `__semver__`, recording which framework version was in play.

`Task` / `TaskParameters` carry the same package-version pin. The version strings are validated against `SEMVER_REGEX` (imported from `aind-behavior-curriculum`). Semantic Versioning is the stated policy for both the package and its schemas.

## Version coercion on load

When a previously-serialized document is deserialized, its stored `version` may not match the model's current declared default. `coerce_schema_version` (`base.py`) best-effort-coerces the deserialized version to the model's `Literal` default and emits a **warning** on mismatch rather than failing hard. This lets older config files still load while making drift visible.

## Why it matters downstream

- **[contraqctor](../ecosystem/contraqctor.md)** uses the `version` field on a dataset to auto-select the matching [data contract](data-contracts-and-standards.md) (e.g. VR Foraging ships `data_contract/v0_4_0.py … v1.py` and picks by the session's version).
- **Datasets are self-describing**: the config snapshots written into a session's `Logs/` folder record both versions, so any dataset can be re-hydrated with the exact schema that generated it.
- A related helper, `DefaultAwareDatetime` (`base.py`), auto-attaches the local timezone to naive datetimes, supporting the timezone-aware datetime [convention](data-contracts-and-standards.md).

# Citations
1. src/aind_behavior_services/base.py
2. src/aind_behavior_services/__init__.py
