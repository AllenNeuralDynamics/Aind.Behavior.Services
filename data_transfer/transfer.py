import argparse
import os
import shutil
from os import PathLike
from typing import Dict, Optional

import aind_behavior_services as abs
from aind_data_schema.models.modalities import Modality
from session_schema import generate_schema

MODALITY_DIR_MAP: Dict[str, Optional[Modality]] = {
    "Lickometer.harp": Modality.BEHAVIOR,
    "Olfactometer.harp": Modality.BEHAVIOR,
    "OperationControl": Modality.BEHAVIOR,
    "Renderer": Modality.BEHAVIOR,
    "SideBodyCamera": Modality.BEHAVIOR_VIDEOS,
    "SoftwareEvents": Modality.BEHAVIOR,
    "TopBodyCamera": Modality.BEHAVIOR_VIDEOS,
    "UpdaterEvents": Modality.BEHAVIOR,
    "Behavior.harp": Modality.BEHAVIOR,
    "ClockGenerator.harp": Modality.BEHAVIOR,
    "Config": None,
    "FaceCamera": Modality.BEHAVIOR_VIDEOS,
}


def copy_directories(ROOT: PathLike, target: PathLike):
    for root, dirs, files in os.walk(ROOT):
        for directory in dirs:
            if directory in MODALITY_DIR_MAP.keys():
                if MODALITY_DIR_MAP[directory] is None:
                    print(f"Copying {directory} to target root.")
                    shutil.copytree(os.path.join(root, directory), os.path.join(target, directory), dirs_exist_ok=True)
                else:
                    print(f"Copying {directory} to {MODALITY_DIR_MAP[directory].name}")
                    shutil.copytree(
                        os.path.join(root, directory),
                        os.path.join(target, MODALITY_DIR_MAP[directory].name, directory),
                        dirs_exist_ok=True,
                    )


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Copy directories based on modality mapping')
    # parser.add_argument('root', type=str, help='Root folder path')
    # parser.add_argument('target', type=str, help='Target folder path')
    # args = parser.parse_args()

    # root = args.root
    # target = args.target
    root = r"C:\Users\bruno.cruz\OneDrive - Allen Institute\Desktop\20240304T143745"
    target = r"C:\Users\bruno.cruz\OneDrive - Allen Institute\Desktop\20240304T143745_AIND"

    session: abs.AindBehaviorSessionModel
    with open(os.path.join(root, r"Config/RawSubject.json"), "r", encoding="utf-8") as f:
        session = abs.AindBehaviorSessionModel.model_validate_json(f.read())

    aind_session = generate_schema(save_schema=False)
    aind_session.subject_id = session.subject
    aind_session.session_start_time = session.date
    aind_session.session_end_time = session.date
    aind_session.session_type = session.experiment
    aind_session.notes = session.notes

    # copy_directories(root, target)
