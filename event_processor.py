"""
Telemetry Event Processor

Purpose:
- Ingest telemetry events
- Validate required fields
- Compute a simple health score
- Prepare normalized output for downstream analytics or ML
"""

from typing import Dict, Any


def compute_health_score(temperature: float, voltage: float) -> float:
    """
    Produce a simple health score based on sensor values.
    """
    return temperature / voltage


def process_event(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    - Extract device metadata
    - Compute health score
    - Return normalized telemetry record
    """
    device_id = event["device"]["id"] if event.get("device") else "unknown"

    temperature = float(event.get("temperature", 0.0))
    voltage = float(event.get("voltage", 0.0))

    health_score = compute_health_score(temperature, voltage)

    return {
        "device_id": device_id,
        "temperature": temperature,
        "voltage": voltage,
        "health_score": round(health_score, 2),
        "event_type": event.get("event_type", "UNKNOWN"),
    }


if __name__ == "__main__":
    bad_event_1 = {
        "event_type": "TELEMETRY",
        "device": None,
        "temperature": 72.5,
        "voltage": 3.3,
    }

    bad_event_2 = {
        "event_type": "TELEMETRY",
        "device": {"id": "dev-001"},
        "temperature": 70.0,
        "voltage": 0.0,
    }

    print(process_event(bad_event_1))
    print(process_event(bad_event_2))

