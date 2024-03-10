import argparse
import os
import shutil
from os import PathLike
from typing import Dict, Optional

import aind_behavior_services as abs
from aind_data_schema.models.modalities import Modality
from session_schema import generate_schema
import sys

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


def copy_directories(src: PathLike, dst: PathLike):
    """
    Copy directories from the source path to the destination path.

    Args:
        src (PathLike): The source path containing the directories to be copied.
        dst (PathLike): The destination path where the directories will be copied to.

    Returns:
        None
    """
    for root, dirs, files in os.walk(src):
        for directory in dirs:
            if directory in MODALITY_DIR_MAP.keys():
                if MODALITY_DIR_MAP[directory] is None:
                    print(f"Copying {directory} to target root.")
                    shutil.copytree(os.path.join(root, directory), os.path.join(dst, directory), dirs_exist_ok=True)
                else:
                    print(f"Copying {directory} to {MODALITY_DIR_MAP[directory].name}")
                    shutil.copytree(
                        os.path.join(root, directory),
                        os.path.join(dst, MODALITY_DIR_MAP[directory].name, directory),
                        dirs_exist_ok=True,
                    )
    return True


def make_session_schema(src: PathLike, dst: PathLike):
    """
    Generate the session schema for the target path.

    Args:
        src (PathLike): The source path containing the directories to be copied.
        dst (PathLike): The destination path where the directories will be copied to.

    Returns:
        None
    """
    session: abs.AindBehaviorSessionModel
    with open(os.path.join(src, r"Config/RawSubject.json"), "r", encoding="utf-8") as f:
        session = abs.AindBehaviorSessionModel.model_validate_json(f.read())

    aind_session = generate_schema(save_schema=False)
    aind_session.subject_id = session.subject
    aind_session.session_start_time = session.date
    aind_session.session_end_time = session.date
    aind_session.session_type = session.experiment
    aind_session.notes = session.notes

    with open(os.path.join(dst, 'Config', "AindSession.json"), "w", encoding="utf-8") as f:
        f.write(aind_session.model_dump_json(indent=3))
    return aind_session


def main(root: PathLike, target: PathLike):
    success: bool = copy_directories(root, target)
    aind_session = make_session_schema(root, target)
    return (success, aind_session)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copy directories based on modality mapping')
    parser.add_argument('root', type=str, help='Root folder path')
    parser.add_argument('target', type=str, help='Target folder path')
    args = parser.parse_args()

    src = args.root
    target = args.target
    _, _ = main(src, target)

