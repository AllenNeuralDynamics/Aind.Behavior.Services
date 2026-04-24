from aind_behavior_services.rig.olfactometer import OlfactometerCalibration, OlfactometerChannelType


def test_olfactometer_calibration_deserializes_legacy_channel_config_and_does_not_serialize_it():
    legacy_payload = {
        "channel_config": {
            "0": {
                "channel_index": 0,
                "channel_type": "Odor",
                "flow_rate_capacity": 100,
                "flow_rate": 100.0,
                "odorant": "Amyl Acetate",
                "odorant_dilution": 1.5,
            },
            "1": {
                "channel_index": 1,
                "channel_type": "Odor",
                "flow_rate_capacity": 100,
                "flow_rate": 100.0,
                "odorant": "Banana",
                "odorant_dilution": 1.5,
            },
            "2": {
                "channel_index": 2,
                "channel_type": "Odor",
                "flow_rate_capacity": 100,
                "flow_rate": 100.0,
                "odorant": "Apple",
                "odorant_dilution": 1.5,
            },
            "3": {
                "channel_index": 3,
                "channel_type": "Carrier",
                "flow_rate_capacity": 1000,
                "flow_rate": 100.0,
                "odorant": None,
                "odorant_dilution": None,
            },
        }
    }

    model = OlfactometerCalibration.model_validate(legacy_payload)

    assert model.channel0 is not None
    assert model.channel1 is not None
    assert model.channel2 is not None
    assert model.channel3 is not None

    assert model.channel0.odorant == "Amyl Acetate"
    assert model.channel1.odorant == "Banana"
    assert model.channel2.odorant == "Apple"
    assert model.channel3.channel_type == OlfactometerChannelType.CARRIER

    dumped = model.model_dump(mode="json")
    assert "channel_config" not in dumped

    # legacy-only keys should not survive model serialization
    assert "channel_index" not in dumped["channel0"]
    assert "flow_rate" not in dumped["channel0"]
