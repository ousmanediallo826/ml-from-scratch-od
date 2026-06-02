# Station A: Optimization & Configuration
from functools import reduce, wraps
import re

def performance_monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

def memoize(func):
    cache = {}
    def wrapper(room_type):
        if room_type not in cache:
            cache[room_type] = func(room_type)
        return cache[room_type]
    return wrapper
@memoize
def get_room_capacity_ceiling(room_type):
    room_capacity_ceiling = {"GROUP-ROOM": 8, "INDIVIDUAL-POD": 1}
    return room_capacity_ceiling.get(room_type, 4)


# Station B: The Live Tracking Record (Functional OOP)

class ResourceEvent:
    def __init__(self, resource_id: str, room_type: str, current_occupancy: int, duration_minutes: float):
        self.resource_id = resource_id
        self.room_type = room_type
        self.current_occupancy = current_occupancy
        self.duration_minutes = duration_minutes

    def __str__(self):
        return f"ResourceEvent({self.resource_id}, {self.room_type}, {self.current_occupancy},{self.duration_minutes})"



# Station C: The Streaming Ingestion Grid (Generators & Iterators)

class LibraryHardwareStream:
    def __init__(self, resources_log: list):
        self.log = resources_log


    def __iter__(self):
        for resource in self.log:
            yield resource


# Station D: The Logistics Workshop
class LibraryProcessor:
    @staticmethod
    @performance_monitor
    def parse_hardware_logs(stream: LibraryHardwareStream):
        resources_pattern =resources_pattern = r"RES_ID:([\w\d]+)\s*\|\s*TYPE:([A-Z-]+)\s*\|\s*OCCUPANCY:([\d.]+)\s*\|\s*DURATION:([\d.]+)"
        for resource in stream:
            match = re.search(resources_pattern, resource)
            if match:
                resource_id, room_type, current_occupancy, duration_minutes = match.groups()
                yield ResourceEvent(resource_id, room_type, int(current_occupancy), float(duration_minutes))

    def calibrate_duration_factory(multiplier: float):
        return lambda resource: ResourceEvent(
            resource.resource_id,
            resource.room_type,
            resource.current_occupancy,
            resource.duration_minutes * multiplier
        )

    def compose(*functions):
        return reduce(lambda f, g: lambda x: g(f(x)), functions)

    @staticmethod
    def process_library_analytics(resources_iterable):
        resources_log = list(resources_iterable)
        if not resources_log:
            return {"average_duration": 0.0, "alerts": {}}

        validated_library = filter(lambda r:r.current_occupancy > 0, resources_log)
        calibrator = LibraryProcessor.calibrate_duration_factory(1.10)

        calibrated_events = list(map(calibrator, validated_library))

        library_values = [e.duration_minutes for e in calibrated_events]

        total_time = reduce(lambda x, y: x + y, library_values, 0.0)
        average_duration = round(total_time / len(library_values), 2) if library_values else 0.0

        resource_ids = [r.resource_id for r in calibrated_events]
        alerts = [
            "OVERCROWDED" if r.current_occupancy > get_room_capacity_ceiling(r.room_type) else "AVAILABLE"
            for r in calibrated_events
        ]
        summary = dict(zip(resource_ids, alerts))

        return {
            "average_duration": average_duration,
            "alerts": summary
        }






