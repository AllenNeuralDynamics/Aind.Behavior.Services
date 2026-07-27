Examples & Cookbook
####################

This page collects concrete, copy-pasteable examples drawn from the framework and the experiment repositories. They are deliberately trimmed to the illustrative essence — follow the referenced source files for the complete, authoritative version. For the guided walk-through that ties these together, see :doc:`getting_started`; for the conceptual map, see :doc:`ecosystem`.

.. contents::
   :local:
   :depth: 1


Defining a ``Rig``
==================================================================

A concrete experiment subclasses :py:class:`~aind_behavior_services.rig.Rig`, pins ``version`` to the package's semantic version, and declares each piece of hardware as a typed device model from the framework's device library. Adapted from ``Aind.Behavior.Telekinesis`` (``src/aind_behavior_telekinesis/rig.py``):

.. code-block:: python

    from typing import Literal, Optional

    import aind_behavior_services.rig.load_cells as lcc
    import aind_behavior_services.rig.water_valve as wvc
    from aind_behavior_services.rig import Rig, cameras, harp
    from aind_behavior_services.rig import aind_manipulator as man
    from pydantic import BaseModel, Field

    from aind_behavior_telekinesis import __semver__


    class AindManipulatorDevice(man.AindManipulator):
        """Append a task-specific field to the base manipulator device."""

        spout_axis: man.Axis = Field(default=man.Axis.Y1, description="Spout axis")


    class RigCalibration(BaseModel):
        water_valve: wvc.WaterValveCalibration = Field(description="Water valve calibration")


    class AindBehaviorTelekinesisRig(Rig):
        version: Literal[__semver__] = __semver__
        triggered_camera_controller: cameras.CameraController[cameras.SpinnakerCamera] = Field(
            description="Required camera controller for triggered cameras."
        )
        harp_behavior: harp.HarpBehavior = Field(description="Harp behavior board")
        harp_lickometer: harp.HarpLicketySplit = Field(description="Harp lickometer")
        harp_load_cells: Optional[lcc.LoadCells] = Field(default=None, description="Harp load cells")
        harp_clock_generator: harp.HarpWhiteRabbit = Field(description="Harp clock generator")
        manipulator: AindManipulatorDevice = Field(description="Manipulator")
        calibration: RigCalibration = Field(description="General rig calibration")

Device models can themselves be subclassed (as ``AindManipulatorDevice`` does) to attach rig-specific fields to a framework device.


Defining a ``Task``
==================================================================

Behavior parameters live in a :py:class:`~aind_behavior_services.task.TaskParameters` subclass; the concrete task subclasses :py:class:`~aind_behavior_services.task.Task`, pins ``version`` / ``name``, and points ``task_parameters`` at it. Stochastic values are expressed with the :py:mod:`~aind_behavior_services.task.distributions` library. Adapted from ``Aind.Behavior.Telekinesis`` (``src/aind_behavior_telekinesis/task_logic.py``):

.. code-block:: python

    from typing import Literal

    import aind_behavior_services.task.distributions as distributions
    from aind_behavior_services.task import Task, TaskParameters
    from pydantic import BaseModel, Field

    from aind_behavior_telekinesis import __semver__


    def scalar_value(value: float) -> distributions.Scalar:
        """Build a fixed (scalar) distribution."""
        return distributions.Scalar(
            distribution_parameters=distributions.ScalarDistributionParameter(value=value)
        )


    class Action(BaseModel):
        reward_probability: distributions.Distribution = Field(
            default=scalar_value(1), description="Probability of reward", validate_default=True
        )
        reward_amount: distributions.Distribution = Field(
            default=scalar_value(1), description="Amount of reward (µL)", validate_default=True
        )


    class AindTelekinesisTaskParameters(TaskParameters):
        environment: "Environment" = Field(description="Environment settings")
        operation_control: "OperationControl" = Field(validate_default=True, description="Operation control")


    class AindBehaviorTelekinesisTaskLogic(Task):
        version: Literal[__semver__] = __semver__
        name: Literal["AindTelekinesis"] = Field(default="AindTelekinesis", description="Task name")
        task_parameters: AindTelekinesisTaskParameters = Field(description="Parameters of the task logic")


Instantiating and serializing to JSON
==================================================================

The three models are ordinary Pydantic objects; a run's input files are just their ``model_dump_json`` output. Adapted from ``Aind.Behavior.Telekinesis`` (``examples/example.py``):

.. code-block:: python

    import datetime
    import os

    from aind_behavior_services.session import Session

    def mock_session() -> Session:
        return Session(
            date=datetime.datetime.now(tz=datetime.timezone.utc),
            experiment="Telekinesis",
            subject="test",
            experimenter=["Foo", "Bar"],
            allow_dirty_repo=True,
            skip_hardware_validation=False,
        )

    def main(path_seed: str = "./local/{schema}.json"):
        models = [mock_task_logic(), mock_session(), mock_rig()]
        os.makedirs(os.path.dirname(path_seed), exist_ok=True)
        for model in models:
            with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
                f.write(model.model_dump_json(indent=2))

These ``*.json`` files are exactly what the launcher hands to Bonsai and what is snapshotted into a session's ``Logs/`` folder (see :doc:`articles`).


Calibrating a device
==================================================================

Calibrations are models too. :py:func:`~aind_behavior_services.rig.water_valve.calibrate_water_valves` fits a linear regression over measurements and returns a populated :py:class:`~aind_behavior_services.rig.water_valve.WaterValveCalibration` (``src/aind_behavior_services/rig/water_valve.py``; usage in ``examples/water_valve.py``):

.. code-block:: python

    from aind_behavior_services.rig import water_valve as wv

    delta_times = [0.1, 0.2, 0.3, 0.4, 0.5]
    water_weights = [10.1 * t - 0.3 for t in delta_times]

    measurements = [
        wv.Measurement(valve_open_interval=0.5, valve_open_time=t, water_weight=[w], repeat_count=1)
        for t, w in zip(delta_times, water_weights)
    ]

    calibration = wv.calibrate_water_valves(measurements)
    # -> WaterValveCalibration(slope=..., offset=..., r2=..., valid_domain=[...])

The resulting calibration slots into the rig model's ``calibration`` field (see `Defining a Rig`_).


Regenerating schemas and C#
==================================================================

Each repo ships a ``regenerate.py`` that unions its models into a ``pydantic.RootModel`` and calls :py:func:`~aind_behavior_services.schema.convert_pydantic_to_bonsai`, which writes both the JSON Schema and the C# Bonsai serializers. This is the step that keeps Python and the Bonsai runtime in lockstep (see :doc:`architecture`). Adapted from ``Aind.Behavior.Telekinesis`` (``src/aind_behavior_telekinesis/regenerate.py``):

.. code-block:: python

    from pathlib import Path
    from typing import Union

    import pydantic
    from aind_behavior_services.schema import BonsaiSgenSerializers, convert_pydantic_to_bonsai
    from aind_behavior_services.session import Session

    import aind_behavior_telekinesis.rig
    import aind_behavior_telekinesis.task_logic

    def main():
        models = [
            aind_behavior_telekinesis.task_logic.AindBehaviorTelekinesisTaskLogic,
            aind_behavior_telekinesis.rig.AindBehaviorTelekinesisRig,
            Session,
        ]
        model = pydantic.RootModel[Union[tuple(models)]]

        convert_pydantic_to_bonsai(
            model,
            model_name="aind_behavior_telekinesis",
            root_element="Root",
            cs_namespace="AindBehaviorTelekinesisDataSchema",
            json_schema_output_dir=Path("./schema/"),
            cs_output_dir=Path("./src/Extensions/"),
            cs_serializer=[BonsaiSgenSerializers.JSON],
        )


Launching an experiment with ``clabe``
==================================================================

A launcher is an ``@experiment()``-decorated async function that receives a ``Launcher``, uses a ``DefaultBehaviorPicker`` to load the rig/session/task from a config library, and runs the Bonsai workflow through ``AindBehaviorServicesBonsaiApp``. Adapted from ``Aind.Behavior.Telekinesis`` (``scripts/aind_launcher.py``):

.. code-block:: python

    from pathlib import Path

    from clabe.apps import AindBehaviorServicesBonsaiApp
    from clabe.launcher import Launcher, LauncherCliArgs, experiment
    from clabe.pickers import DefaultBehaviorPicker, DefaultBehaviorPickerSettings
    from pydantic_settings import CliApp


    @experiment()
    async def telekinesis_experiment(launcher: Launcher) -> None:
        picker = DefaultBehaviorPicker(
            launcher=launcher,
            settings=DefaultBehaviorPickerSettings(
                config_library_dir=r"\\allen\aind\scratch\AindBehavior.db\AindTelekinesis"
            ),
        )
        session = picker.pick_session(Session)
        task_logic = picker.pick_task(AindBehaviorTelekinesisTaskLogic)
        rig = picker.pick_rig(AindBehaviorTelekinesisRig)
        launcher.register_session(session, rig.data_directory)

        bonsai_app = AindBehaviorServicesBonsaiApp(
            workflow=Path(r"./src/main.bonsai"),
            temp_directory=launcher.temp_dir,
            rig=rig, session=session, task=task_logic,
        )
        await bonsai_app.run_async()
        launcher.copy_logs()


    class ClabeCli(LauncherCliArgs):
        def cli_cmd(self):
            Launcher(settings=self).run_experiment(telekinesis_experiment)


    def main() -> None:
        CliApp().run(ClabeCli)

Launcher settings can be supplied on the command line or from a ``clabe.yml`` in the project root or ``./local``:

.. code-block:: yaml

    # examples/clabe.yml
    data_dir: C:/Data
    allow_dirty: true
    default_behavior_picker:
      config_library_dir: './local/TelekinesisDatabase'
    robocopy:
      destination: 'C:/DataAfterTransfer'


Validating a dataset with ``contraqctor``
==================================================================

Downstream, ``contraqctor`` declares a **data contract** — a typed tree of streams describing what a dataset should contain — and runs **QC** suites over it. Adapted from ``contraqctor`` (``examples/contract.py``):

.. code-block:: python

    from pathlib import Path

    from contraqctor.contract import Dataset, DataStreamCollection
    from contraqctor.contract.harp import DeviceYmlByFile, HarpDevice
    from contraqctor.contract.json import PydanticModel, SoftwareEvents
    from contraqctor.contract.csv import Csv

    root = Path(r"path_to_data")
    my_dataset = Dataset(
        name="my_dataset", version="1.0.0", description="My dataset",
        data_streams=[
            DataStreamCollection(
                name="Behavior",
                data_streams=[
                    HarpDevice(
                        name="HarpBehavior",
                        reader_params=HarpDevice.make_params(
                            path=root / "behavior/Behavior.harp", device_yml_hint=DeviceYmlByFile(),
                        ),
                    ),
                    SoftwareEvents(
                        name="Block",
                        reader_params=SoftwareEvents.make_params(root / "behavior/SoftwareEvents/Block.jsonl"),
                    ),
                    Csv(
                        "CurrentPosition",
                        reader_params=Csv.make_params(path=root / "behavior/OperationControl/CurrentPosition.csv"),
                    ),
                ],
            ),
        ],
    )

    exceptions = my_dataset.load_all()  # load every stream; returns (stream, exception) tuples
    value = my_dataset["Behavior"]["HarpBehavior"].at("WhoAmI").read()

.. note::
    ``SoftwareEvent`` files use the ``.jsonl`` extension (`#230 <https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/issues/230>`_); ``contraqctor`` abstracts the extension for consumers, so older ``.json`` datasets keep loading.

Then run QC suites through a ``Runner`` (adapted from ``examples/qc.py``):

.. code-block:: python

    import contraqctor.qc as qc

    harp_behavior = my_dataset["Behavior"]["HarpBehavior"]
    harp_behavior.load_all()

    runner = qc.Runner()
    runner.add_suite(qc.harp.HarpDeviceTestSuite(harp_behavior))
    runner.add_suite(qc.contract.ContractTestSuite(exceptions))
    results = runner.run_all_with_progress()

``ContractTestSuite`` folds the load-time exceptions into the QC report, so a missing or malformed stream shows up as a failed check rather than a crash. An ``HtmlReporter`` can be passed to ``run_all_with_progress(reporter=...)`` to emit a shareable report.
