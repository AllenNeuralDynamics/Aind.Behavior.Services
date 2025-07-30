import glob
import importlib.util
import logging
import os
from pathlib import Path
from types import ModuleType

# Set up test environment variables
os.environ.setdefault("COMPUTERNAME", "UNIT_TEST_PC")

EXAMPLES_DIR = Path(__file__).parents[1] / "examples"

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def build_example(script_path: str) -> ModuleType:
    module_name = Path(script_path).stem
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    if spec is None:
        raise ImportError(f"Can't find {script_path}")
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise ImportError(f"Can't load {script_path}")
    spec.loader.exec_module(module)
    return module


def build_examples(examples_dir: Path = EXAMPLES_DIR):
    for script_path in glob.glob(str(examples_dir / "*.py")):
        _ = build_example(script_path)
