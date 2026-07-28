---
type: Convention
title: Anatomy of an experiment repository
description: The canonical repository skeleton every Aind.Behavior.* leaf repo shares — Python schema package (rig/task_logic/regenerate/cli), a Bonsai workflow with generated C#, versioned data_contract + data_qc, a clabe launcher, and examples/tests — plus the launcher pattern.
resource: https://github.com/AllenNeuralDynamics/Aind.Behavior.Telekinesis
tags: [repo-structure, skeleton, launcher, convention, template]
timestamp: 2026-07-27T00:00:00Z
---

# Anatomy of an experiment repository

Every single-purpose experiment repo (`Aind.Behavior.*` and `Aind.Physiology.Fip`) shares one skeleton, most cleanly exemplified by `Aind.Behavior.Telekinesis` (which is copier-templated — it carries a `.copier-answers.yml`). A repo owns only its **task-specific rig and task_logic models**; everything else it inherits from [aind-behavior-services](../ecosystem/aind-behavior-services.md).

New repos are scaffolded from the [`Aind.Behavior.CopierTemplate`](https://github.com/AllenNeuralDynamics/Aind.Behavior.CopierTemplate) [copier](https://copier.readthedocs.io/) template (`copier copy gh:AllenNeuralDynamics/Aind.Behavior.CopierTemplate <dest>`), which emits this skeleton. The template is a deliberately generic *starting point* and is expected to be adapted per experiment; the layout below describes what it produces once filled in.

## The canonical skeleton

```
<repo>/
  pyproject.toml            # uv-managed; declares aind_behavior_services + a [project.scripts] launcher
  uv.lock  .python-version
  .bonsai/ (or bonsai/)     # Bonsai environment / bootstrapper config
  schema/ (or src/DataSchemas/)   # GENERATED JSON schemas (+ example instances)
  src/
    <python_pkg>/           # e.g. src/aind_behavior_telekinesis/
      __init__.py           # __version__ + pep440_to_semver -> __semver__
      rig.py                # class AindFooRig(Rig)                 -- subclasses the framework
      task_logic.py         # class AindFooTaskLogic(Task) + TaskParameters
      regenerate.py         # codegen driver: pydantic -> JSON schema + C#
      cli.py                # console-script entrypoint
      data_contract/        # contraqctor Dataset definition (raw files -> typed streams)
      data_qc/              # QC suites run against the data_contract
    main.bonsai             # the acquisition workflow
    Extensions/             # *.bonsai sub-workflows + *.cs operators + <Name>.Generated.cs
    Extensions.csproj       # compiles Extensions into a Bonsai-loadable assembly
  scripts/
    deploy.cmd / deploy.ps1 # bootstrap the pinned Bonsai environment
    aind_launcher.py        # clabe-based launcher (name/location varies)
  examples/                 # clabe.yml + scripts that instantiate & serialize models
  tests/  docs/
```

Names vary but **roles are constant**. The Bonsai config dir is `.bonsai/` or `bonsai/`; generated JSON schema is in `schema/` or `src/DataSchemas/`; the launcher lives in `scripts/aind_launcher.py`, `scripts/aind.py`, or is exposed through `cli.py` + the `[project.scripts]` console command.

## What is inherited vs defined

- **Inherited from the framework**: `Session` (used wholesale, not subclassed), the `Rig`/`Device` and `Task`/`TaskParameters` bases, the shared device + calibration + distribution models, and `convert_pydantic_to_bonsai` codegen.
- **Defined by the repo**: its `rig.py` and `task_logic.py` model trees, its `main.bonsai` + `Extensions/`, and its `data_contract`/`data_qc`.

Common dependency conventions: a `data` extra pulls [`contraqctor`](../ecosystem/contraqctor.md); a `launcher` extra pulls `aind-clabe[aind-services]`; a `docs` group pulls Sphinx (VR Foraging uses MkDocs). All pin `aind_behavior_services` to the same `0.13.x` line.

## The Python ↔ Bonsai bridge

`regenerate.py` collects the repo's models into a `RootModel` and calls [`convert_pydantic_to_bonsai`](../concepts/schema-first.md), writing JSON Schema to `schema/` and C# to `src/Extensions/<Name>.Generated.cs` (namespace e.g. `AindBehaviorTelekinesisDataSchema`). `main.bonsai` references the generated types via `clr-namespace:...;assembly=Extensions`.

## The launcher pattern

All launchers are built on [clabe](../ecosystem/clabe.md) and share a shape:

```python
from clabe.launcher import Launcher, LauncherCliArgs
from clabe.apps import AindBehaviorServicesBonsaiApp
from clabe.pickers import DefaultBehaviorPicker, DefaultBehaviorPickerSettings

async def experiment(launcher):
    picker  = DefaultBehaviorPicker(launcher=..., settings=DefaultBehaviorPickerSettings(
        config_library_dir=r"\\allen\...\AindBehavior.db\<Task>"))
    session = picker.pick_session(Session)
    task    = picker.pick_task(AindFooTaskLogic)     # or pick_trainer_state(...) if curriculum-driven
    rig     = picker.pick_rig(AindFooRig)
    launcher.register_session(session, rig.data_directory)
    ResourceMonitor(...).run()
    bonsai_app = AindBehaviorServicesBonsaiApp(workflow=Path("./src/main.bonsai"),
                                               rig=rig, session=session, task=task)
    await bonsai_app.run_async()
    # optional: CurriculumApp, data mappers, contraqctor QC (HtmlReporter), copy_logs / transfer

class ClabeCli(LauncherCliArgs):
    def cli_cmd(self): Launcher(settings=self).run_experiment(experiment)
```

**Common** across all: `Launcher` + a `Picker` reading a config-library DB + `AindBehaviorServicesBonsaiApp` + `ResourceMonitor` + optional QC. **Custom per repo**: which picker, whether a [curriculum](../ecosystem/curriculum.md) runs, `ByAnimalModifier` subclasses for stateful rig fields (e.g. manipulator position), and the data-mapper/QC steps. See [running-an-experiment](../workflows/running-an-experiment.md).

# Citations
1. Aind.Behavior.Telekinesis (`src/aind_behavior_telekinesis/`, `scripts/aind_launcher.py`)
2. Aind.Behavior.IsoForce, Aind.Behavior.JustFrames, Aind.Physiology.Fip
