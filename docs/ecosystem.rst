The Ecosystem
##############

``aind_behavior_services`` is rarely used on its own. It sits at the centre of a small ecosystem of tools that together take a behavior experiment from *an idea* to *reproducible, quality-controlled, cloud-archived data*. This page is a tour of that ecosystem: what each piece does, how they fit together, what a real paradigm looks like when built on top, and what happens across the life of a session.

New here? Start with :doc:`getting_started`. Want the design rationale? See :doc:`architecture`. Want the structured, machine-readable reference? See :doc:`knowledge`.

.. contents::
   :local:
   :depth: 2


The big picture
==================================================================

The framework's job is to define a **contract** — a shared vocabulary of strongly-typed schemas — that every other tool reads and writes. Because everything speaks the same schema *language*, the pieces compose cleanly. Dependencies point in one direction: each layer builds on the one above it, and never the reverse.

.. code-block:: text

    aind-behavior-curriculum      upstream: base Task / Curriculum
            │
    aind-behavior-services        THIS LIBRARY — the schema contract + codegen
            │   Rig / Task / Session, the device & calibration library,
            │   data-record standards, and the Pydantic → JSON Schema → C#
            │   code-generation pipeline
            ├───────────────┬──────────────────────────────┐
            ▼               ▼                               ▼
        clabe         experiment repos                 contraqctor
      (launcher)    (Aind.Behavior.*,                (downstream: reads the
                     Aind.Experiment.*)               acquired data back in,
                     subclass Rig / Task,             validates it against a
                     own a Bonsai workflow)           data contract, runs QC)

Read the diagram as "*is used by*": the framework is used by ``clabe`` and by the concrete experiment repositories; the data those experiments produce is later consumed by ``contraqctor``.

.. note::
   The framework does **not** impose a single, universal schema that every experiment must fit. There is no one "behavior experiment" schema — different paradigms have different ``Rig`` and ``Task`` shapes. What ``aind-behavior-services`` standardizes is a *vocabulary* of composable building blocks (base models, device and calibration models, distribution primitives, and data-record types) that each experiment assembles to its own needs. That vocabulary is partial by design and grows as new paradigms require new elements — see :doc:`architecture`.

At a glance:

.. list-table::
   :header-rows: 1
   :widths: 22 18 60

   * - Component
     - Role
     - What it owns
   * - ``aind-behavior-services``
     - Contract
     - Rig / Task / Session base models, the device & calibration library, data-record standards, and the codegen pipeline.
   * - ``clabe``
     - Launcher
     - Running a session on a rig: validation, config picking, Bonsai launch, metadata mapping, data transfer.
   * - experiment repos
     - Paradigm
     - A concrete ``Rig`` + ``Task``, a Bonsai workflow, and the generated C#.
   * - ``contraqctor``
     - Data & QC
     - Reading a finished dataset against a typed contract and running quality-control suites.
   * - ``aind-behavior-curriculum``
     - Training
     - The stage/transition machinery for automated shaping.
   * - Bonsai / Harp
     - Runtime / hardware
     - The reactive acquisition engine and the clock-synchronized hardware.


The pieces
==================================================================

aind-behavior-services (this library)
-----------------------------------------------------

Provides the vocabulary everything else shares: the :doc:`Rig / Task / Session <architecture>` base models, a library of hardware devices and their calibrations, standards for the data records an experiment emits, and the code-generation tooling that turns a Pydantic model into a JSON Schema and then into the C# operators the acquisition engine runs. It deliberately does **not** launch experiments — that is delegated to ``clabe``. See the :doc:`examples` for how a repo subclasses ``Rig``/``Task``, calibrates a device, and regenerates its schemas.

clabe — launching experiments
-----------------------------------------------------

`clabe <https://github.com/AllenNeuralDynamics/clabe>`_ (the "Command-Line interface Launcher for AIND Behavior Experiments", installed as ``aind-clabe``) is the framework that actually *runs* a session on a rig. It walks a linear, modular workflow: validate the environment, pick the rig/task/session configuration, launch the Bonsai workflow, map the run to standardized metadata, and transfer/register the data to the cloud. Every prompt and message flows through a pluggable front-end (console, terminal UI, or a browser), so the same launcher can run interactively on a rig or headless over RPC. See the launcher example in the :doc:`examples`.

The experiment repositories
-----------------------------------------------------

Each behavior paradigm lives in its own repository (for example `VR Foraging <https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging>`_ or `Telekinesis <https://github.com/AllenNeuralDynamics/Aind.Behavior.Telekinesis>`_). A repository **subclasses** this library's ``Rig`` and ``Task`` to describe its own hardware and behavior logic, ships a Bonsai workflow (``src/main.bonsai``) that runs the closed loop, and regenerates its C# from its Pydantic models. It inherits ``Session`` and the shared device/calibration/distribution library unchanged. See `How an experiment materializes`_ below.

contraqctor — data contracts and quality control
-----------------------------------------------------

`contraqctor <https://github.com/AllenNeuralDynamics/contraqctor>`_ is the downstream half of the story. It lets you declare, as typed Python objects, a **data contract** — what files a dataset should contain and how to load each — and then run lightweight **quality-control** suites over the loaded data. Because it understands this library's data records (such as the ``SoftwareEvent`` log format) and the rig/task/session JSON, it can read a finished session back in, confirm the contract held, and produce a QC report. It is also self-versioning: the contract is selected from the session's schema ``version``, so old and new datasets both load. See the contract + QC example in the :doc:`examples`.

Analysis & packaging (downstream)
-----------------------------------------------------

Beyond primary QC, dedicated *packaging* (or *processing*) packages turn the raw acquired data into standard, analysis-ready structures — normalized tables, `NWB <https://www.nwb.org/>`_ files, and other derived layouts — so that analysis does not have to start from the raw session. `Aind.Behavior.VrForaging.Packaging <https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging.Packaging/>`_ is an example for the VR Foraging paradigm. These packages sit downstream of the framework: they consume standardized datasets (loaded via ``contraqctor``) and emit reproducible, analysis-ready products that people can analyze efficiently.

Curriculum — automated training
-----------------------------------------------------

Training an animal is modelled as a **curriculum**: a directed graph of stages where each stage *is* a complete task configuration, and the transitions between stages are predicates over measured performance metrics (computed directly from the acquired dataset — rewards, choices, patch/site events). The base machinery lives in `aind-behavior-curriculum <https://github.com/AllenNeuralDynamics/aind-behavior-curriculum>`_ (the upstream package this library's ``Task`` builds on); each paradigm ships its own concrete curricula as a separate, independently-versioned package. Because curricula carry a semver and change only through reviewed pull requests, the exact training path an animal took is auditable. A curriculum also doubles as an experiment specification — distinct scientific paradigms are encoded as distinct curricula. See `Training with a curriculum`_ for a worked ladder.

Bonsai and Harp — acquisition and hardware
-----------------------------------------------------

`Bonsai <https://bonsai-rx.org>`_ is the reactive dataflow environment that runs the acquisition workflow; `Harp <https://harp-tech.org>`_ is the open hardware standard the rig is built from. Harp devices share a common hardware clock, giving sub-millisecond alignment across every data stream. The framework's schema-first pipeline targets Bonsai (the generated C# classes are the strongly-typed, in-Bonsai view of the Python schemas), and the ``Rig`` model describes the Harp devices by COM port. At runtime the workflow deserializes the three JSON documents, instantiates the hardware, and runs a closed loop over a message bus, separating a hard-real-time hardware tier from a soft-real-time tier (rendering and task logic).

Beyond AIND
-----------------------------------------------------

Several pieces of the stack are external, community projects the framework builds on rather than owns: **Bonsai** and **Harp** (above), **Pydantic** / **JSON Schema** (the schema layer), and **uv** (the Python environment and workspace manager). The framework's contribution is to bind these into one reproducible pipeline.


How an experiment materializes
==================================================================

Every experiment is fully described by three JSON documents — a **Rig** (the apparatus), a **Task** (what the animal experiences), and a **Session** (this one run). These three documents are the *only* input the Bonsai acquisition workflow needs.

A concrete paradigm becomes software like this:

#. Subclass ``Rig`` and ``Task`` in a new repository and populate them with the devices and parameters the paradigm needs (see :doc:`examples`).
#. Regenerate the derived artifacts — the JSON Schemas and the C# operators — from those Pydantic models. This keeps the Python side and the Bonsai runtime in lockstep; regeneration is enforced in continuous integration.
#. Build the Bonsai workflow (``src/main.bonsai``) that consumes those three documents and runs the closed loop.

There are two kinds of repository:

- **Single-unit repos** (``Aind.Behavior.<Task>`` and ``Aind.Physiology.<Modality>``) are one self-contained acquisition unit with their own schema, workflow, and Bonsai executable. Behavior repos define both a rig and a task; physiology repos typically define only a rig (there is no behavioral task to model).
- **Composition repos** (``Aind.Experiment.<...>``) are thin wrappers that combine several single-unit repos (pulled in as git submodules) into one coordinated session — for example, running a behavior task and fiber photometry concurrently against a single shared ``Session``. We will progressively move more and more in this direction as experiments require more coordination across modalities and platforms.


A concrete paradigm: composing a foraging task
==================================================================

The `VR Foraging <https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging>`_ platform is the most mature paradigm built on the framework and the clearest illustration of the *composable* principle. It is worth walking through, because it shows how far a paradigm can go using only configuration of the shared grammar.

In VR Foraging a head-fixed mouse runs on a treadmill; its locomotion drives forward motion through a rendered virtual corridor. The corridor is **tiled into typed virtual sites**:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Site type
     - Role
   * - ``InterPatch``
     - Travel segment between patches — the "travel cost".
   * - ``InterSite``
     - Spacing between reward sites within a patch.
   * - ``RewardSite``
     - Where harvest attempts happen; odor-cued.
   * - ``PostPatch``
     - Optional segment after a patch (e.g. added friction).

Site lengths are drawn from parameterized distributions (typically truncated exponentials), so no two traversals are identical — using the same :py:mod:`~aind_behavior_services.task.distributions` library any task can reach for.

Each **patch** is then composed from orthogonal pieces:

- an **odor specification** — a mixture vector of up to three odor-channel concentrations, acting as the patch's identity cue;
- a **reward specification** — base ``amount``, ``probability``, and ``available`` count (each a distribution), plus optional **operant logic** (the animal must stop — velocity below a threshold, held for a ``stop_duration`` — to register a choice);
- a **visual stimuli specification** (e.g. contrast);
- a per-site **friction** coefficient that the treadmill brake renders;
- **reward dynamics** — chained *reward functions* that compose to implement depletion, replenishment, or custom kinetics; and
- **patch terminators** — conditions that end a patch (on rejection, choice, reward, time, distance, or reward-site count).

Finally, sequences of patches are produced by an **environment model** (a Markov environment — patches plus a transition matrix — or an explicit sequence), and environments are grouped into **blocks** with end-conditions, enabling within-session contingency changes.

The point is the last one: the primitives — patches, virtual sites, odor mixtures, reward functions, patch-update kinetics, terminators, environments, blocks — are orthogonal building blocks that can be combined freely. A new paradigm is generally a **new arrangement of existing primitives**, authored as data and validated before it ever reaches a rig, rather than new acquisition code. VR Foraging uses exactly this grammar to express several distinct paradigms (multi-site patch foraging, single-site bandit-like tasks, and memory-driven rule learning) with no change to the acquisition engine.


Training with a curriculum
==================================================================

An animal rarely starts on the final task; it is shaped there. A curriculum encodes that shaping as a directed graph of stages, each stage a complete task configuration, with transitions gated on performance metrics. The canonical VR Foraging shaping ladder, the ``depletion`` curriculum, reads:

.. code-block:: text

    learn to run → learn to stop → stochastic reward → multiple odors + depletion → graduation

with updaters that progressively shrink the stop-velocity threshold and grow the stop-duration and reward-delay offsets from session to session. Metrics that drive the transitions (rewards, choices, active patch/site events) are computed directly from the acquired dataset, so training advances automatically as the animal's behavior meets each criterion. Because the curriculum is versioned and changed only by review, the training path is fully auditable.


The lifecycle of a session
==================================================================

Putting it together, a session flows through the ecosystem in five stages (this is the pipeline a rig scientist actually follows):

#. **Task design** — define or update the paradigm's Pydantic models and regenerate the schemas and C# (``aind-behavior-services``); the animal's current curriculum stage supplies a validated task configuration.
#. **Acquisition & control** — ``clabe`` validates the environment, picks the configuration, and hands the three JSON documents to Bonsai, which runs the closed loop on the Harp hardware. Live ImGui/ImPlot panels show state during the session.
#. **Primary QC** — ``contraqctor`` loads the dataset against the versioned data contract and runs quality-control suites, emitting a report — a first-line integrity check immediately after acquisition, using exactly the checks that match the task version that ran.
#. **Standardization & upload** — the run is mapped to the institute-wide ``aind-data-schema`` standard (an ``Acquisition`` and an ``Instrument``) from the very same ``*_input.json`` documents that ran it, then transferred and registered as a cloud data asset.
#. **Visualization & analysis** — the standardized, QC'd dataset feeds downstream tooling. Dedicated *packaging* packages (see `Analysis & packaging (downstream)`_) process the raw data into standard, analysis-ready structures, and review tools such as a Plotly/Dash session dashboard load them for per-session and cohort-level analysis.

An experiment repo commonly exposes stages 1, 3, and 4 as subcommands of its own CLI (for example VR Foraging's ``regenerate``, ``data-qc``, and ``data-mapper``), all built on the tools described above.

For the exact on-disk layout a session produces — Harp streams, ``SoftwareEvents``, ``OperationControl`` CSVs, ``Logs`` (the config snapshots), and videos — see the :doc:`dataset structure <articles/core/dataset_structure>` and :doc:`software events <articles/data_formats/software_events>` standards.


Where to go next
==================================================================

- :doc:`getting_started` — the hands-on quickstart.
- :doc:`examples` — copy-pasteable snippets for every step.
- :doc:`architecture` — the reasoning behind the schema-first design and the Rig / Task / Session decomposition.
- :doc:`articles` — the concrete data standards (dataset structure, filenames, Harp logging, software events).
- :doc:`knowledge` — the machine-readable knowledge base, with a concept file per idea and per tool for deeper, structured reference.
- The source: `aind-behavior-services <https://github.com/AllenNeuralDynamics/Aind.Behavior.Services>`_, `clabe <https://github.com/AllenNeuralDynamics/clabe>`_, and `contraqctor <https://github.com/AllenNeuralDynamics/contraqctor>`_.
