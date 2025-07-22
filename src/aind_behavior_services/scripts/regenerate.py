import logging
from pathlib import Path

from aind_behavior_services.calibration import aind_manipulator
from aind_behavior_services.data_types import DataTypes
from aind_behavior_services.session import AindBehaviorSessionModel
from aind_behavior_services.utils import (
    convert_pydantic_to_bonsai,
)

logger = logging.getLogger(__name__)

SCHEMA_ROOT = Path("./src/schemas")
EXTENSIONS_ROOT = Path("./src/Extensions/")
NAMESPACE_PREFIX = "AindBehaviorServices"


def main():
    convert_pydantic_to_bonsai(
        aind_manipulator.CalibrationRig,
        model_name="aind_manipulator",
        json_schema_output_dir=SCHEMA_ROOT,
        cs_output_dir=EXTENSIONS_ROOT,
        cs_namespace=f"{NAMESPACE_PREFIX}.AindManipulator",
        json_schema_export_kwargs={"remove_root": True},
    )

    convert_pydantic_to_bonsai(
        AindBehaviorSessionModel,
        model_name="aind_behavior_session",
        json_schema_output_dir=SCHEMA_ROOT,
        cs_output_dir=EXTENSIONS_ROOT,
        cs_namespace=f"{NAMESPACE_PREFIX}.AindBehaviorSession",
        json_schema_export_kwargs={"remove_root": False},
    )

    convert_pydantic_to_bonsai(
        DataTypes, model_name="aind_behavior_data_types", json_schema_output_dir=SCHEMA_ROOT, cs_output_dir=None
    )


if __name__ == "__main__":
    main()
