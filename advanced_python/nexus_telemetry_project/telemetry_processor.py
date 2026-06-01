import re
from functools import wraps, reduce

def performance_monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

def memoize(func):
    cache = {}

    def wrapper(sensor_id):
        if sensor_id not in cache:
            cache[sensor_id] = func(sensor_id)
        return cache[sensor_id]
    return wrapper

@memoize
def get_device_threshold(device_id: str) -> float:
    limits = {"DEV_A": 80.0, "DEV_B": 120.0}
    return limits.get(device_id, 80.0)




# Station B: The Hardware Record (Functional OOP)
class Reading:
    def __init__(self, device_id: str, timestamp: str, metric: str, value: float):
        self.device_id = device_id
        self.timestamp = timestamp
        self.metric = metric
        self.value = value

    def __str__(self):
        return f"Reading(Device:{self.device_id}, timestamp:{self.timestamp}, metric:{self.metric}, value:{self.value})"



# Station C: The Ingestion Grid (Generators & Regular Expressions)
class TelemetryStream:
    def __init__(self, log_list: list):
        self.log = log_list

    def __iter__(self):
        for log in self.log:
            yield log

# Letters/digits after a DEVICE: prefix
#
# An ISO timestamp string after a TIME: prefix
#
# Word characters after a METRIC: prefix
#
# A floating-point number (including a decimal) after a VAL: prefix
class TelemetryProcessor:
    @staticmethod
    @performance_monitor
    def parse_log(stream: TelemetryStream):
        log_pattern = r"DEVICE:([\w_]+)\s\|\sTIME:([\d-]+)\s\|\sMETRIC:(\w+)\s\|\sVAL:([\d.]+)"
        for log in stream:
            match = re.search(log_pattern, log)
            if match:
                dv_id, timestamp, metric, value = match.groups()
                yield Reading(device_id=dv_id, timestamp=timestamp, metric=metric, value=value)

    def calibrate_factory(multiplier: float):

        return lambda reading: Reading(
            reading.device_id,
            reading.timestamp,
            reading.metric,
            reading.value * multiplier
        )

    def compose(*functions):
        return reduce(lambda f, g: lambda x: g(f(x)), functions)
    @staticmethod
    def process_telemetry(readings_iterable):
        tele_readings = list(readings_iterable)

        valid_readings = list(filter(lambda r: r.value > 0.0, tele_readings))

        calibrator = TelemetryProcessor.calibrate_factory(1.05)
        calibrated_readings = list(map(calibrator, valid_readings))

        calibrated_values = [r.value for r in calibrated_readings]

        total_sum = reduce(lambda acc,val: acc + val, valid_readings, 0.0)
        batch_average = round(total_sum / len(calibrated_values), 2)
        device_ids = [r.device_id for r in calibrated_readings]
        alerts = [
            "CRITICAL" if r.value > get_device_threshold(r.device_id) else "NORMAL"
            for r in calibrated_readings
        ]

        summary_dict = dict(zip(device_ids, alerts))

        return {
            "average": batch_average,
            "alerts": summary_dict
        }


