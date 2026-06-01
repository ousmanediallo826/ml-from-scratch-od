import pytest
from telemetry_processor import TelemetryStream, TelemetryProcessor, get_device_threshold


@pytest.fixture
def sample_logs():
    """Provides test data containing clean strings, spikes, and noise."""
    return [
        "DEVICE:DEV_A | TIME:2026-06-01 | METRIC:TEMP | VAL:45.0",  # Valid normal
        "DEVICE:DEV_B | TIME:2026-06-01 | METRIC:TEMP | VAL:125.0",  # Valid over-threshold spike
        "DEVICE:DEV_A | TIME:2026-06-01 | METRIC:TEMP | VAL:-10.0",  # Filtered out (<= 0)
        "DEVICE:MALFUNCTION_DATA_STREAM_CORRUPTED"  # Regex skipped
    ]


def test_telemetry_pipeline_end_to_end(sample_logs):
    # Initialize Generator Stream Iterator
    stream = TelemetryStream(sample_logs)

    # Process Extraction via Regex Generator
    parsed_readings = TelemetryProcessor.parse_log(stream)

    # Run Reductions and Zip Maps
    metrics = TelemetryProcessor.process_telemetry(parsed_readings)

    # --- EXPECTED MATHEMATICAL VERIFICATION ---
    # DEV_A calibrated: 45.0 * 1.05 = 47.25 USD (Normal, limit is 80.0)
    # DEV_B calibrated: 125.0 * 1.05 = 131.25 USD (Critical, limit is 120.0)
    # Total Average: (47.25 + 131.25) / 2 = 89.25

    assert metrics["average"] == 89.25

    # Verify Zip Mapping Layout
    assert len(metrics["alerts"]) == 2  # Bad rows successfully purged
    assert metrics["alerts"]["DEV_A"] == "NORMAL"
    assert metrics["alerts"]["DEV_B"] == "CRITICAL"


def test_standalone_currying():
    """Validates the curried function factory logic."""
    calibrator = TelemetryProcessor.calibrate_factory(2.0)
    from telemetry_processor import Reading
    mock_reading = Reading("DEV_A", "2026", "TEMP", 10.0)

    calibrated_output = calibrator(mock_reading)
    assert calibrated_output.value == 20.0