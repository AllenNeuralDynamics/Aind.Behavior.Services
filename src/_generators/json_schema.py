import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Type

from pydantic import BaseModel

from aind_behavior_services.data_types import DataTypes
from aind_behavior_services.message_protocol import MessageProtocol
from aind_behavior_services.rig.aind_manipulator import AindManipulator
from aind_behavior_services.schema import export_schema
from aind_behavior_services.session import Session
from aind_behavior_services.utils import pascal_to_snake_case

SCHEMA_ROOT = Path("./schema")


def _write_json(schema_path: os.PathLike, output_model_name: str, model: Type[BaseModel], **extra_kwargs) -> None:
    with open(os.path.join(schema_path, f"{output_model_name}.json"), "w", encoding="utf-8") as f:
        json_model = export_schema(model, **extra_kwargs)
        f.write(json_model)


@dataclass
class ToGenerateJsonSchema:
    model_name: str
    model: Type[BaseModel]
    remove_root: bool = True


def main():
    models = (
        ToGenerateJsonSchema(model_name="Session", model=Session, remove_root=False),
        ToGenerateJsonSchema(model_name="DataTypes", model=DataTypes, remove_root=True),
        ToGenerateJsonSchema(model_name="MessageProtocol", model=MessageProtocol, remove_root=True),
        ToGenerateJsonSchema(model_name="AindManipulator", model=AindManipulator, remove_root=False),
    )

    if not SCHEMA_ROOT.exists():
        logging.info(f"Creating schema root directory at {SCHEMA_ROOT}")
        SCHEMA_ROOT.mkdir(parents=True, exist_ok=True)
    for m in models:
        _write_json(SCHEMA_ROOT, pascal_to_snake_case(m.model_name), m.model, remove_root=m.remove_root)


if __name__ == "__main__":
    main()
