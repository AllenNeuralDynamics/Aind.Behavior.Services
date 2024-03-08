import datetime
from typing import Any, Dict, List, Tuple, Union

from aind_data_schema.core.session import (
    RelativePosition,
    RewardSolution,
    Session,
    SpoutSide,
    Stream,
    RewardDeliveryConfig,
    RewardSolution,
    RewardSpoutConfig,
    SpoutSide,
)
from aind_data_schema.models.devices import LightEmittingDiode, RewardDelivery, RewardSpout
from aind_data_schema.models.modalities import Modality
from aind_data_schema.models.stimulus import BehaviorStimulation, StimulusEpoch
from aind_data_schema.models.organizations import Organization
from aind_data_schema.models.coordinates import Translation3dTransform, Axis, AxisName
from aind_data_schema.models.devices import Device
from aind_data_schema.models.stimulus import Software


def generate_schema(save_schema: bool = False):

    placeholder_time = datetime.datetime.now()

    # Streams
    streams: List[Stream] = []  # names of Devices must match to the rig schema

    streams.append(
        Stream(
            stream_end_time=placeholder_time,
            stream_start_time=placeholder_time,
            stream_modalities=[Modality.BEHAVIOR, Modality.BEHAVIOR_VIDEOS],
            daq_names=["Harp.Behavior", "Harp.ClockSynchronizer", "Harp.Lickometer", "Harp.Olfactometer"],
            camera_names=["MainCamera"],
            light_sources=[],
            stimulus_device_names=[
                "Speaker",
                "LeftMonitor",
                "CenterMonitor",
                "RightMonitor",
                "Olfactometer",
                "RewardDelivery",
            ],
            notes="This is a stream",
            mouse_platform_name="Wheel",
            active_mouse_platform=True,
        )
    )

    reward = RewardDelivery(
        reward_spouts=[
            RewardSpout(
                name="RandomSpout",
                side=SpoutSide.CENTER,
                spout_position=RelativePosition(
                    device_position_transformations=[Translation3dTransform(translation=[0, 0, 0])],
                    device_origin="Wheel",
                    device_axes=[
                        Axis(name=AxisName.X, direction="idk..."),
                        Axis(name=AxisName.X, direction="idk..."),
                        Axis(name=AxisName.X, direction="idk..."),
                    ],  # and this is why it should be a dictionary....
                ),
                spout_diameter=2,
                solenoid_valve=Device(name="SolenoidValve", device_type="SolenoidValve"),
            )
        ],
    )  # Why is this a duplicate from reward_spout_config?

    reward_spout_config = RewardSpoutConfig(
        side=SpoutSide.CENTER,
        starting_position=RelativePosition(
            device_position_transformations=[Translation3dTransform(translation=[0, 0, 0])],
            device_origin="Wheel",
            device_axes=[
                Axis(name=AxisName.X, direction="idk..."),
                Axis(name=AxisName.X, direction="idk..."),
                Axis(name=AxisName.X, direction="idk..."),
            ],  # and this is why it should be a dictionary....
        ),
        variable_position=True,
    )

    reward_config = RewardDeliveryConfig(reward_solution=RewardSolution.WATER, reward_spouts=[reward_spout_config])

    bonsai_software = Software(
        name="bonsai",
        version="https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging/blob/b613a620a75c4a92caba1307eb6f2ed5c3db1308/bonsai/Bonsai.config",
        url="https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging",
    )
    vr_foraging_script = Software(
        name="vr_foraging_script",
        version="b613a620a75c4a92caba1307eb6f2ed5c3db1308",
        url="https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging",
    )

    behavior_stim = BehaviorStimulation(
        behavior_name="vr-foraging",
        session_number=1,
        behavior_software=[bonsai_software],
        behavior_script=vr_foraging_script,
        output_parameters={},  # outcome of the session
        reward_consumed_during_epoch=0,
        trials_total=-1,
        trials_finished=-1,
        trials_rewarded=-1,
    )

    stimulus_epochs: List[StimulusEpoch] = []
    stimulus_epochs.append(StimulusEpoch(stimulus_start_time=0, stimulus_end_time=0, stimulus=behavior_stim))

    session = Session(
        experimenter_full_name=["Jane Doe"],
        session_end_time=placeholder_time,
        session_start_time=placeholder_time,
        rig_id="Rig1",
        session_type="foraging-vr",
        subject_id="123132",
        animal_weight_post=0,
        animal_weight_prior=0,
        data_streams=streams,
        stimulus_epochs=stimulus_epochs,
        reward_delivery=reward_config,
        notes="This is a session",
    )

    if save_schema is True:
        with open("session.json", "w") as f:
            f.write(session.model_dump_json(indent=3))

    return session


if __name__ == "__main__":
    generate_schema(save_schema=False)
