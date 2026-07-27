---
type: Component
title: contraqctor — data contracts and quality control
description: The downstream library that reads acquired behavior data back in — a declarative typed data contract (DataStream/Dataset tree) describing what files a dataset should contain and how to load each, plus a lightweight QC test-suite framework (Suite/Runner/Result).
resource: https://github.com/AllenNeuralDynamics/contraqctor
tags: [data-contract, qc, quality-control, contraqctor, downstream]
timestamp: 2026-07-27T00:00:00Z
---

# contraqctor — data contracts and quality control

**contraqctor** (a portmanteau of "contract" + "QC") is the downstream data layer (PyPI `contraqctor`, v0.6.0, MIT). It **depends on** [aind-behavior-services](aind-behavior-services.md) (its first hard dependency), not the reverse: it knows how to parse the [`SoftwareEvent`](../concepts/data-contracts-and-standards.md) records and the rig/session/task JSON a run produces, reads them back in, validates them against a contract, and QCs them. It also depends on `harp-python`, OpenCV, pandas/numpy/scipy, pydantic, and `rich`.

It provides two cooperating capabilities.

## 1. Data contracts (`src/contraqctor/contract/`)

A **declarative, typed description of what a dataset should contain and how to load each piece.**

- **`DataStream[TData, TReaderParams]`** (`contract/base.py`) — a named node that knows how to load one piece of data. `make_params(...)` builds typed reader params; `load()` reads and caches into `.data`; flags `has_data` / `has_error`; children accessed via `__getitem__` / `at`.
- **`DataStreamCollection`** — a `DataStream` whose data is *other* streams (a tree). **`Dataset`** extends it with a semver `version` and is the top-level contract object. `load_all(strict=False)` recursively loads the tree and *captures* per-stream load errors (`collect_errors()` returns `ErrorOnLoad` tuples) rather than raising; `strict=True` re-raises.
- Concrete stream types: `Csv`, `Text`, `Json`/`MultiLineJson`/`PydanticModel`/ `ManyPydanticModel`/**`SoftwareEvents`**, `HarpRegister`/`HarpDevice`, `Camera`, and `MapFromPaths` (fans a glob of paths into many inner streams).
- **Versioned contracts**: an experiment repo ships several contract versions (e.g. VR Foraging `data_contract/v0_4_0.py … v1.py`) and auto-selects the one matching the session's [`version`](../concepts/versioning.md).

> Note: there is no dedicated `ContractError` type. Misuse raises plain
> `ValueError`/`KeyError`; load-time failures are captured as `ErrorOnLoad`
> entries and asserted by `ContractTestSuite` (below).

## 2. Quality control (`src/contraqctor/qc/`)

A lightweight test-suite framework over the loaded data.

- **`Suite`** (`qc/base.py`) — subclass it; any method named `test_*` is discovered and run. Inside a test, call `pass_test` / `fail_test` / `warn_test` / `skip_test` to build `Result`s (a test may return one, `yield` several, or return a bare value auto-wrapped as PASS). Lifecycle hooks: `setup_suite`/`teardown_suite`, `setup`/`teardown`.
- **`Result` / `Status`** — `Status` ∈ {PASSED, FAILED, ERROR, SKIPPED, WARNING}; `Result` carries status, payload, references, message, and context (tests can attach assets like plots via `ContextExportableObj`).
- **`Runner`** — `add_suite(suite, group=None)` registers suites; `run_all_with_progress(reporter=…)` runs them with a progress bar and dispatches to a `Reporter` (`ConsoleReporter` default, or `HtmlReporter`). `ResultsStatistics` aggregates counts / pass-rate.
- **`ContractTestSuite`** (`qc/contract.py`) — the bridge: turns the contract's captured load-errors into QC results (fail on non-excluded errored streams, downgrade excluded ones to warnings).
- Ready-made domain suites: `CsvTestSuite`, `Camera`, and a `harp/` family (device, environment sensor, sniff detector, treadmill, lickety-split).

## The workflow

1. Declare a `Dataset(name, version, description, data_streams=[...])` tree.
2. `dataset.load_all()` — load everything, capturing per-stream errors.
3. Feed load errors into `ContractTestSuite` to assert the contract held.
4. `Runner().add_suite(...).run_all_with_progress()` — run QC.
5. Render results via `ConsoleReporter` / `HtmlReporter`.

The canonical end-to-end example is contraqctor's own `examples/contract.py` (a full multi-modality VR-Foraging-style dataset). Experiment repos wire this into their launcher via a `data_contract/` + `data_qc/` package pair; see [running-an-experiment](../workflows/running-an-experiment.md).

# Citations
1. https://github.com/AllenNeuralDynamics/contraqctor
2. contraqctor `src/contraqctor/contract/base.py`, `src/contraqctor/qc/base.py`
