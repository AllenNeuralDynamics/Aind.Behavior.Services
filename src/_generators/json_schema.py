from dataclasses import dataclass
import logging
import os
from pathlib import Path

from pydantic import BaseModel

from aind_behavior_services.calibration import aind_manipulator
from aind_behavior_services.data_types import DataTypes
from aind_behavior_services.message_protocol import MessageProtocol
from aind_behavior_services.session import AindBehaviorSessionModel
from aind_behavior_services.utils import export_schema, pascal_to_snake_case

logger = logging.getLogger(__name__)

SCHEMA_ROOT = Path("./src/schemas")


def _write_json(schema_path: os.PathLike, output_model_name: str, model: BaseModel, **extra_kwargs) -> None:
    with open(os.path.join(schema_path, f"{output_model_name}.json"), "w", encoding="utf-8") as f:
        json_model = export_schema(model, **extra_kwargs)
        f.write(json_model)


@dataclass
class ToGenerateJsonSchema:
    model_name: str
    model: BaseModel
    remove_root: bool = True

def main():
    models = (
        ToGenerateJsonSchema(model_name="AindBehaviorSessionModel", model=AindBehaviorSessionModel, remove_root=False),
        ToGenerateJsonSchema(model_name="DataTypes", model=DataTypes, remove_root=True),
        ToGenerateJsonSchema(model_name="MessageProtocol", model=MessageProtocol, remove_root=True),
        ToGenerateJsonSchema(model_name="AindManipulator", model=aind_manipulator.CalibrationRig, remove_root=False),
    )

    for m in models:
        _write_json(SCHEMA_ROOT, pascal_to_snake_case(m.model_name), m.model, remove_root=m.remove_root)


if __name__ == "__main__":
    main()
