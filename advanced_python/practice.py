class FibonacciIterator:
    def __init__(self, limit=None):
        self.a, self.b = 0, 1
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.limit is not None and self.count >= self.limit:
            raise StopIteration

        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result





fib_bounded = FibonacciIterator(limit=6)

for num in fib_bounded:
    print(num)



def running_stats():
    count = 0
    total = 0
    min_val = None
    max_val = None

    while True:
        val = yield {
            "count": count,
            "total": total,
            "mean": total / count if count > 0 else 0.0,
            "min": min_val,
            "max": max_val,
        }
        count += 1
        total += val
        min_val = val if min_val is None else min(min_val, val)
        max_val = val if max_val is None else max(max_val, val)