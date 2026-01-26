import datetime
import unittest

from aind_behavior_services.message_protocol import (
    HeartbeatPayload,
    HeartbeatStatus,
    LogLevel,
    LogPayload,
    MessageType,
    RegisteredMessages,
)


class TestLogPayload(unittest.TestCase):
    def test_basic_log_payload(self):
        payload = LogPayload(message="Test message")
        self.assertEqual(payload.message, "Test message")
        self.assertEqual(payload.level, LogLevel.DEBUG)
        self.assertIsNone(payload.context)
        self.assertIsNone(payload.application_version)

    def test_log_payload_with_all_fields(self):
        context = {"user": "test_user", "action": "login"}
        payload = LogPayload(
            message="User logged in",
            level=LogLevel.INFO,
            context=context,
            application_version="1.2.3",
        )
        self.assertEqual(payload.message, "User logged in")
        self.assertEqual(payload.level, LogLevel.INFO)
        self.assertEqual(payload.context, context)
        self.assertEqual(payload.application_version, "1.2.3")

    def test_log_payload_serialization(self):
        payload = LogPayload(message="Error occurred", level=LogLevel.ERROR, context={"error_code": 500})
        json_str = payload.model_dump_json()
        deserialized = LogPayload.model_validate_json(json_str)

        self.assertEqual(payload.message, deserialized.message)
        self.assertEqual(payload.level, deserialized.level)
        self.assertEqual(payload.context, deserialized.context)


class TestHeartbeatStatus(unittest.TestCase):
    def test_heartbeat_status_values(self):
        self.assertEqual(HeartbeatStatus.OK, 0)
        self.assertEqual(HeartbeatStatus.WARNING, 1)
        self.assertEqual(HeartbeatStatus.ERROR, 2)
        self.assertEqual(HeartbeatStatus.CRITICAL, 3)

    def test_heartbeat_status_ordering(self):
        self.assertLess(HeartbeatStatus.OK, HeartbeatStatus.WARNING)
        self.assertLess(HeartbeatStatus.WARNING, HeartbeatStatus.ERROR)
        self.assertLess(HeartbeatStatus.ERROR, HeartbeatStatus.CRITICAL)


class TestHeartbeatPayload(unittest.TestCase):
    def test_heartbeat_with_context(self):
        context = {"cpu_usage": 0.45, "memory_usage": 0.60, "uptime": 3600}
        payload = HeartbeatPayload(status=HeartbeatStatus.WARNING, context=context)
        self.assertEqual(payload.status, HeartbeatStatus.WARNING)
        self.assertEqual(payload.context, context)

    def test_heartbeat_serialization(self):
        payload = HeartbeatPayload(status=HeartbeatStatus.CRITICAL, context={"reason": "disk_full"})
        json_str = payload.model_dump_json()
        deserialized = HeartbeatPayload.model_validate_json(json_str)

        self.assertEqual(payload.status, deserialized.status)
        self.assertEqual(payload.context, deserialized.context)


class TestRegisteredMessages(unittest.TestCase):
    def test_message_serialization(self):
        log_payload = LogPayload(message="Serialization test", level=LogLevel.DEBUG)
        message = RegisteredMessages(
            message_type=MessageType.REQUEST,
            timestamp=datetime.datetime.now(datetime.timezone.utc),
            payload=log_payload,
            process_id="test_process",
            hostname="test_host",
            rig_name="test_rig",
        )
        json_str = message.model_dump_json()
        deserialized = RegisteredMessages.model_validate_json(json_str)

        self.assertEqual(message.message_type, deserialized.message_type)
        self.assertEqual(message.process_id, deserialized.process_id)
        self.assertEqual(message.hostname, deserialized.hostname)
        self.assertEqual(message.rig_name, deserialized.rig_name)


if __name__ == "__main__":
    unittest.main()
