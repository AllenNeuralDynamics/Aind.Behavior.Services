import unittest

from aind_behavior_services.data_types import (
    DataType,
    SoftwareEvent,
    TimestampSource,
)


class TestSoftwareEvent(unittest.TestCase):
    def test_basic_event_creation(self):
        event = SoftwareEvent(name="test_event")
        self.assertEqual(event.name, "test_event")
        self.assertIsNone(event.timestamp)
        self.assertEqual(event.timestamp_source, TimestampSource.NULL)
        self.assertIsNone(event.data)

    def test_event_with_string_data(self):
        event = SoftwareEvent[str](
            name="message_event",
            timestamp=123.45,
            timestamp_source=TimestampSource.HARP,
            data="Hello World",
            data_type=DataType.STRING,
        )
        self.assertEqual(event.data, "Hello World")
        self.assertEqual(event.timestamp, 123.45)

    def test_event_with_numeric_data(self):
        event = SoftwareEvent[float](name="value_changed", timestamp=100.0, data=42.5, data_type=DataType.NUMBER)
        self.assertEqual(event.data, 42.5)

    def test_event_with_dict_data(self):
        test_data = {"key1": "value1", "key2": 123}
        event = SoftwareEvent[dict](name="config_update", timestamp=200.0, data=test_data, data_type=DataType.OBJECT)
        self.assertEqual(event.data, test_data)

    def test_event_with_frame_info(self):
        event = SoftwareEvent(
            name="frame_event", frame_index=10, frame_timestamp=16.67, timestamp_source=TimestampSource.RENDER
        )
        self.assertEqual(event.frame_index, 10)
        self.assertEqual(event.frame_timestamp, 16.67)
        self.assertEqual(event.timestamp_source, TimestampSource.RENDER)

    def test_event_serialization(self):
        event = SoftwareEvent[str](
            name="serialization_test",
            timestamp=300.0,
            timestamp_source=TimestampSource.HARP,
            data="test_data",
            data_type=DataType.STRING,
        )
        json_str = event.model_dump_json()
        deserialized = SoftwareEvent[str].model_validate_json(json_str)

        self.assertEqual(event.name, deserialized.name)
        self.assertEqual(event.timestamp, deserialized.timestamp)
        self.assertEqual(event.data, deserialized.data)
        self.assertEqual(event.timestamp_source, deserialized.timestamp_source)


if __name__ == "__main__":
    unittest.main()
