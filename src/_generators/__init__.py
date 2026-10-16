from pathlib import Path

from bonsai.sgen.cli import main as sgen_main

from _generators import rig_harp

SCHEMA_ROOT = Path("./schema")

SCHEMA_MODULES = (
    "aind_behavior_services.data_types",
    "aind_behavior_services.message_protocol",
    "aind_behavior_services.rig.aind_manipulator",
    "aind_behavior_services.session",
)
# bonsai-sgen names each file after its namespace; map to the historical file names.
SCHEMA_FILENAMES = {
    "AllenNeuralDynamics.AindBehaviorServices.DataTypes": "data_types",
    "AllenNeuralDynamics.AindBehaviorServices.MessageProtocol": "message_protocol",
    "AllenNeuralDynamics.AindManipulator": "aind_manipulator",
    "AllenNeuralDynamics.AindBehaviorServices.Session": "session",
}


def export_schemas() -> None:
    SCHEMA_ROOT.mkdir(parents=True, exist_ok=True)
    sgen_main(["export", *SCHEMA_MODULES, "-o", str(SCHEMA_ROOT)])
    for namespace, name in SCHEMA_FILENAMES.items():
        (SCHEMA_ROOT / f"{namespace}.json").replace(SCHEMA_ROOT / f"{name}.json")


def main():
    rig_harp.main()
    export_schemas()
