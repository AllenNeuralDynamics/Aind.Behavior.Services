import unittest

from pydantic import Field, ValidationError

from aind_behavior_services.task import Task, TaskParameters


class ConcreteTaskParameters(TaskParameters):
    """Example task parameters for testing"""

    test_parameter: int = Field(default=42, description="A test parameter")


class ConcreteTask(Task):
    """Example task for testing"""

    version: str = "0.1.0"
    task_parameters: ConcreteTaskParameters = Field(default_factory=ConcreteTaskParameters)


class TestTaskParameters(unittest.TestCase):
    def test_custom_rng_seed(self):
        params = ConcreteTaskParameters(rng_seed=12345.0)
        self.assertEqual(params.rng_seed, 12345.0)

    def test_custom_parameter(self):
        params = ConcreteTaskParameters(test_parameter=100)
        self.assertEqual(params.test_parameter, 100)

    def test_serialization(self):
        params = ConcreteTaskParameters(rng_seed=999.0, test_parameter=50)
        json_str = params.model_dump_json()
        deserialized = ConcreteTaskParameters.model_validate_json(json_str)
        self.assertEqual(params.rng_seed, deserialized.rng_seed)
        self.assertEqual(params.test_parameter, deserialized.test_parameter)

    def test_package_version_frozen(self):
        params = ConcreteTaskParameters()
        with self.assertRaises(ValidationError):
            params.aind_behavior_services_pkg_version = "0.0.0"


class TestTask(unittest.TestCase):
    def test_with_custom_parameters(self):
        params = ConcreteTaskParameters(rng_seed=555.0, test_parameter=75)
        task = ConcreteTask(name="CustomTask", task_parameters=params)
        self.assertEqual(task.task_parameters.rng_seed, 555.0)
        self.assertEqual(task.task_parameters.test_parameter, 75)

    def test_serialization(self):
        params = ConcreteTaskParameters(rng_seed=123.0, test_parameter=99)
        task = ConcreteTask(name="SerializationTest", task_parameters=params)
        json_str = task.model_dump_json()
        deserialized = ConcreteTask.model_validate_json(json_str)
        self.assertEqual(task.version, deserialized.version)
        self.assertEqual(task.name, deserialized.name)
        self.assertEqual(task.task_parameters.rng_seed, deserialized.task_parameters.rng_seed)
        self.assertEqual(task.task_parameters.test_parameter, deserialized.task_parameters.test_parameter)


if __name__ == "__main__":
    unittest.main()
