import unittest
from datetime import datetime, timezone

from aind_behavior_services.session import Session


class TestSession(unittest.TestCase):
    def test_session_name_generation(self):
        session = Session(subject="mouse001")
        self.assertIsNotNone(session.session_name)
        self.assertIn("mouse001", session.session_name)
        self.assertIsNotNone(session.session_name)

    def test_custom_session_name(self):
        session = Session(subject="mouse001", session_name="custom_session")
        self.assertEqual(session.session_name, "custom_session")

    def test_custom_date(self):
        custom_date = datetime(2024, 1, 15, 10, 30, 0, tzinfo=timezone.utc)
        session = Session(subject="mouse001", date=custom_date)
        self.assertEqual(session.date, custom_date)

    def test_serialization(self):
        session = Session(
            subject="mouse001",
            experiment="Test Experiment",
            experimenter=["Alice"],
            notes="Test notes",
        )
        json_str = session.model_dump_json()
        deserialized = Session.model_validate_json(json_str)
        self.assertEqual(session.subject, deserialized.subject)
        self.assertEqual(session.experiment, deserialized.experiment)
        self.assertEqual(session.experimenter, deserialized.experimenter)
        self.assertEqual(session.notes, deserialized.notes)


if __name__ == "__main__":
    unittest.main()
