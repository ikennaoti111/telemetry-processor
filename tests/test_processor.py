from event_processor import process_event

def test_missing_device_is_handled():
    event = {"event_type": "TELEMETRY", "device": None, "temperature": 72.5, "voltage": 3.3}
    process_event(event)

def test_voltage_zero_is_handled():
    event = {"event_type": "TELEMETRY", "device": {"id": "dev-001"}, "temperature": 70.0, "voltage": 0.0}
    process_event(event)

