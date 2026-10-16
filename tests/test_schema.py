import json
import tempfile
import unittest
from pathlib import Path

from bonsai.sgen.cli import main as sgen_main

EXPECTED_NAMESPACES = {
    "AllenNeuralDynamics.AindBehaviorServices",
    "AllenNeuralDynamics.AindBehaviorServices.DataTypes",
    "AllenNeuralDynamics.AindBehaviorServices.Distributions",
    "AllenNeuralDynamics.AindBehaviorServices.MessageProtocol",
    "AllenNeuralDynamics.AindBehaviorServices.Rig",
    "AllenNeuralDynamics.AindBehaviorServices.Rig.Harp",
    "AllenNeuralDynamics.AindBehaviorServices.Session",
    "AllenNeuralDynamics.AindManipulator",
}


class TestSchemaExport(unittest.TestCase):
    def test_package_exports_every_namespace(self):
        with tempfile.TemporaryDirectory() as output:
            self.assertEqual(sgen_main(["export", "aind_behavior_services", "--allow-local-types", "-o", output]), 0)
            files = {path.stem: path for path in Path(output).glob("*.json")}
            self.assertEqual(set(files), EXPECTED_NAMESPACES)
            for namespace, path in files.items():
                definitions = json.loads(path.read_text(encoding="utf-8"))["$defs"]
                typenames = {d["x-sgen-typename"] for d in definitions.values() if "x-sgen-typename" in d}
                self.assertTrue(any(t.rpartition(".")[0] == namespace for t in typenames))


if __name__ == "__main__":
    unittest.main()
