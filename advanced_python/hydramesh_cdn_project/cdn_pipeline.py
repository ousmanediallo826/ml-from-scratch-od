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
    def wrapper(region_code):
        if region_code not in cache:
            cache[region_code] = func(region_code)
        return cache[region_code]
    return wrapper

@memoize
def get_region_threshold(node_id: str):
    max_network_latency = {"US-EAST": 150, "EU-WEST": 100}
    return max_network_latency.get(node_id, 100)

# Station B: The Node Registry (Functional OOP)

class NodePacket:
    def __init__(self, node_id: str, region: str, request_count: int, latency: int):
        self.node_id = node_id
        self.region = region
        self.request_count = request_count
        self.latency = latency
    def __str__(self):
        return f"NodePacket({self.node_id}, {self.region}, {self.request_count}, {self.latency})"


# Station C: The Streaming Ingestion Grid (Generators & Iterators)

class CDNStream:
    def __init__(self, log_list: list):
        self.log = log_list

    def __iter__(self):
        for log in self.log:
            yield log

# Station D: The Optimization Workshop

class CDNSStream:
    @staticmethod
    @performance_monitor
    def parse_packet(stream: CDNStream):
        log_pattern = r"NODE:([\w\d]+)\s\|\sREGION:([A-Z-]+)\s\|\sREQS:([\d.]+)\s\|\sLATENCY:([\d.]+)"

        for log in stream:
            match = re.search(log_pattern, log)
            if match:
                noid, region, reqs, latency = match.groups()
                yield NodePacket(noid, region, int(reqs), int(latency))

    def optimize_factory(multiplier: int):
        return lambda nodepacket: NodePacket(
            nodepacket.node_id,
            nodepacket.region,
            nodepacket.request_count,
            nodepacket.latency * multiplier

        )

    def compose(*functions):
        return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

    def process_nodes(packet_list: list):
        reading_packets = list(packet_list)

        valid_packet_request = filter(lambda packet: packet.request_count > 0, reading_packets)
        calibrator = CDNStream.optimize_factory(0.90)
        map_valid_packets = list(map(calibrator, valid_packet_request))

        compress = [p.latency for p in map_valid_packets]
        total_latency = reduce(lambda x, y: x + y, compress)
        device_ids = [r.device_id for r in map_valid_packets]
        alerts = [
            "OVERLOAD" if r.latency > get_region_threshold(r.node_id) else "OPTIMAL"
            for r in map_valid_packets
        ]

        summary = zip(device_ids, alerts)

        return summary











