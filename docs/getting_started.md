# Getting Started

This page is a practical, end-to-end orientation: the mental model behind the framework, and a walk through the lifecycle of an experiment — authoring the models, serializing a configuration, regenerating the Bonsai code, launching a session, and quality-controlling the result. Each step links to a full, runnable snippet in the [examples](examples.md).

If you want the design rationale, read [architecture](architecture.md); for the map of how all the tools relate, read [ecosystem](ecosystem.md).


## The mental model: an experiment is three documents

The one idea to internalize first: **an experiment is fully described by three strongly-typed documents**, and those documents are the only inputs the acquisition workflow needs.

- **Rig** — the physical apparatus (devices, COM ports, calibrations).
- **Task** — what the animal experiences (the behavior logic), abstracted from hardware.
- **Session** — metadata for this one run (subject, experimenter, date, paths).

Because the three are decoupled, the same task can run on any calibrated rig, and the same rig can run any task, with no code changes. See [architecture](architecture.md) for why the space is split this way.

Three design principles motivate the whole framework (and explain the steps below):

1. **Composable** — a new paradigm is generally a new *arrangement of existing building blocks*, authored as data and validated before it reaches a rig, rather than new acquisition code. The framework does not impose one fixed schema on all experiments; it offers a vocabulary of elements to assemble, and that vocabulary grows as new paradigms need new pieces.
1. **Schema-first** — every experiment is specified as validated, version-pinned data, and the whole software/hardware stack is pinned, so a session runs identically anywhere.
1. **Correct-by-construction metadata** — the same documents that *run* a session are what *describe* it afterwards, so the metadata is guaranteed to match what actually happened.


## Prerequisites & installation

The Python package is on PyPI:

```bash
pip install aind-behavior-services
```

To *run* experiments (not just author schemas) you also need the Windows-side tooling — the Bonsai runtime, `dotnet` with `Bonsai.Sgen`, `Harp.Toolkit`, and device drivers. See the [requirements](articles/requirements.md) article and the `Prerequisites` / `Deployment` sections of the project `README` (an experiment repo typically bootstraps everything with `scripts/deploy.ps1`, which provisions a `uv`-managed Python environment and a fully version-pinned Bonsai runtime).


## Step 1 — Author the rig and task

!!! tip
    You don't have to assemble a new experiment repository by hand. The [Aind.Behavior.CopierTemplate](https://github.com/AllenNeuralDynamics/Aind.Behavior.CopierTemplate) [copier](https://copier.readthedocs.io/) template scaffolds the whole skeleton — `rig.py` / `task_logic.py` stubs, the `regenerate.py` codegen driver, a Bonsai workflow, `examples/`, and CI — so you start from a working layout and fill in the paradigm. Generate one with `copier copy gh:AllenNeuralDynamics/Aind.Behavior.CopierTemplate <destination>`. This is a *starting point*: it is intentionally generic and expected to be adapted to each experiment's needs.

A concrete paradigm lives in its own repository that subclasses `Rig` and `Task`. Populate the rig with the framework's typed device models, and the task with parameters (stochastic values come from the `distributions` library).

See the "Defining a `Rig`" and "Defining a `Task`" sections of the [examples](examples.md) for the full pattern. In short, you write `class AindFooRig(Rig): ...` and `class AindFooTaskLogic(Task): ...`, pinning `version` to your package's semantic version.

Calibrations are models too — for example `calibrate_water_valves()` fits a regression over measurements and returns a `WaterValveCalibration` you drop into the rig (see [examples](examples.md)).


## Step 2 — Produce a configuration (serialize to JSON)

Instantiate the three models and serialize them with Pydantic. These `*.json` files are exactly what the launcher hands to Bonsai and what gets snapshotted into the session's `Logs/` folder:

```python
with open("session_input.json", "w", encoding="utf-8") as f:
    f.write(session.model_dump_json(indent=2))
```

Validation happens here, *before* a rig is ever touched — an invalid configuration fails fast. See the full instantiate-and-serialize example in the [examples](examples.md).


## Step 3 — Regenerate schemas and Bonsai code

Whenever the models change, regenerate the derived artifacts so the Python source of truth and the Bonsai runtime stay in lockstep. Each experiment repo ships a `regenerate.py` that unions its models into a `pydantic.RootModel` and calls `convert_pydantic_to_bonsai()`, emitting the JSON Schema and the C# serializers. The framework's own schemas are regenerated with the `generate` console script. This step is enforced in CI so the models can never silently drift from the running acquisition code — see [examples](examples.md) and [architecture](architecture.md).


## Step 4 — Launch a session

Launching is handled by [clabe](https://github.com/AllenNeuralDynamics/clabe), the experiment launcher. A launcher script is a small `@experiment()` function that picks the rig/task/session from a config library and runs the Bonsai workflow. `clabe` validates the environment (clean git repo, disk space), serializes the picked models, launches `src/main.bonsai`, and — after acquisition — can map metadata and transfer data to the cloud. See the full launcher in the [examples](examples.md) and the tool tour in [ecosystem](ecosystem.md).


## Step 5 — Quality-control the data

After acquisition, [contraqctor](https://github.com/AllenNeuralDynamics/contraqctor) loads the dataset against a **versioned data contract** (a typed description of what files should be present and how to read them) and runs **QC suites** over it, optionally emitting an HTML report. Because the contract is selected automatically from the session's schema `version`, old and new datasets both load correctly. See the contract + QC example in the [examples](examples.md).


## Where to go next

- [ecosystem](ecosystem.md) — the full tour of the tools and how a real paradigm (VR Foraging) is built on the framework.
- [examples](examples.md) — the complete, copy-pasteable snippets referenced above.
- [architecture](architecture.md) — the reasoning behind the schema-first, Rig/Task/Session design.
- [articles](articles/index.md) — the concrete data standards (dataset layout, filenames, Harp logging, software events).
- [knowledge](knowledge.md) — the machine-readable knowledge base for deeper reference.
