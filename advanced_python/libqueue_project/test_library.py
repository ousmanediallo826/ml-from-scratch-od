import pytest
from library_processor import LibraryHardwareStream, LibraryProcessor


@pytest.fixture
def hardware_logs():
    """Provides mock sensor logs mimicking real library gate scanners."""
    return [
        "RES_ID:ROOM101 | TYPE:GROUP-ROOM | OCCUPANCY:5 | DURATION:60.0",  # Valid - Available (5 <= 8)
        "RES_ID:POD202  | TYPE:INDIVIDUAL-POD | OCCUPANCY:3 | DURATION:30.0",  # Valid - Overcrowded (3 > 1)
        "RES_ID:ROOM102 | TYPE:GROUP-ROOM | OCCUPANCY:0 | DURATION:45.0",  # Filtered out (Ghost Reservation)
        "RES_ID:GATE_SCANNER_BAD_DATA_DROPPED_ANOMALY"  # Regex skipped safely
    ]


def test_libqueue_pipeline(hardware_logs):
    stream = LibraryHardwareStream(hardware_logs)
    parsed_data = LibraryProcessor.parse_hardware_logs(stream)
    dashboard_metrics = LibraryProcessor.process_library_analytics(parsed_data)

    # --- MATHEMATICAL ACCURACY VERIFICATION ---
    # ROOM101 duration calibrated: 60.0 * 1.10 = 66.0 mins
    # POD202 duration calibrated: 30.0 * 1.10 = 33.0 mins
    # Expected Average Length of Stay: (66.0 + 33.0) / 2 = 49.5 mins
    assert dashboard_metrics["average_duration"] == 49.5

    # Assert Dashboard Alerts
    assert len(dashboard_metrics["alerts"]) == 2
    assert dashboard_metrics["alerts"]["ROOM101"] == "AVAILABLE"
    assert dashboard_metrics["alerts"]["POD202"] == "OVERCROWDED"