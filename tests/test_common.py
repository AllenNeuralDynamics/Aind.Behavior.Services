import unittest

from pydantic import BaseModel, ValidationError

from aind_behavior_services.common import LookUpTable


class Container(BaseModel):
    lut: LookUpTable


class TestLookUpTable(unittest.TestCase):
    def test_insufficient_length_validation(self):
        with self.assertRaises(ValidationError):
            Container(lut=[[0.0, 0.0]])

    def test_pair_validation(self):
        with self.assertRaises(ValidationError):
            Container(lut=[[0.0], [1.0, 1.0]])
        with self.assertRaises(ValidationError):
            Container(lut=[[0.0, 0.0, 0.0], [1.0, 1.0]])


if __name__ == "__main__":
    unittest.main()
