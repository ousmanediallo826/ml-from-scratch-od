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


#+=====================
def count_up(max_number):
    count = 1
    while count <= max_number:
        print("count")
        yield count
        count += 1


counter = count_up(3)
print(next(counter))
print(next(counter))
print(next(counter))





#
#
#
# fib_bounded = FibonacciIterator(limit=6)
#
# for num in fib_bounded:
#     print(num)
#
#
#
# def running_stats():
#     count = 0
#     total = 0
#     min_val = None
#     max_val = None
#
#     while True:
#         val = yield {
#             "count": count,
#             "total": total,
#             "mean": total / count if count > 0 else 0.0,
#             "min": min_val,
#             "max": max_val,
#         }
#         count += 1
#         total += val
#         min_val = val if min_val is None else min(min_val, val)
#         max_val = val if max_val is None else max(max_val, val)







import time

log_data = [
    "INFO: System booted successfully.",
    "INFO: User 'admin' logged in.",
    "WARNING: High CPU usage detected.",
    "INFO: Database backup completed.",
    "CRITICAL: Firewall breached!",
    "INFO: User 'guest' logged out.",
    "CRITICAL: Power supply failure!",
    "CRITICAL: Water breached!",
"CRITICAL: Electricity breached!",
]

def log_reader(logs):
    for log in logs:
        time.sleep(0.5)
        yield log


def critical_alert_system(log_stream):
    for line in log_stream:
        if "WARNING" in line:
            yield f"🚨 ALARM: {line}"



stream = log_reader(log_data)
alert = critical_alert_system(stream)

print("Starting security monitor...")
print("-" * 30)

for alert in alert:
    print(alert)

print("-" * 30)
print("Monitoring finished.")


#===============sushi

def make_sushi(number_sushi):
    sushi = 1
    while sushi <= number_sushi:
        yield sushi
        sushi += 1


sushis = make_sushi(10)
print(next(sushis))
print(next(sushis))
print(next(sushis))
for sushi in sushis:
    print(sushi)



#+==================================
import time
import random

def temperature_stream():
    readings = [70,72,78,74,81,71,91,100]
    for temp in readings:
        time.sleep(0.5)
        yield temp

def heat_temperature_alert(logs):
    for log in logs:
        time.sleep(0.5)
        if log >= 75:
            yield f"🔥 WARNING: High Temp Detected: {log}"


logs = temperature_stream()
temperature = heat_temperature_alert(logs)
print("Starting security monitor...")
print("-" * 30)
for temps in temperature:
    print(temps)
print("-" * 30)
print("Monitoring finished.")




#Problem 2: The E-Commerce Price Converter (Transforming Data)

def usd_price_stream():
    prices = [10.0, 25.5, 99.9, 5.0]
    for price in prices:
        time.sleep(0.5)
        yield price

def euro_convertor(prices):
    for price in prices:
        yield f"Euro: ${price * 0.92:.2f}"

usd_stream= usd_price_stream()
euro = euro_convertor(usd_stream)
print("Starting money convertor...")
print("-" * 30)
for price in euro:
    print(price)

print("End money convertor...")
print("-" * 30)



# Problem 3: The Username Cleaner (Data Cleaning)

def usernames():
    messy_signups = ["  alice   ", "BOB  ", "   ", "charlie_99", "  DEBBY "]
    for signup in messy_signups:
        time.sleep(0.5)
        yield signup

def cleanup_messy_data(messy_data):
    for user in messy_data:
        if user == " ":
            messy_data.remove(user)
        else:
            user = user.strip().lower()
            yield f"Here the cleanup username: {user}"

users = usernames()
clean_users = cleanup_messy_data(users)
print("Cleaning up...")
print("-" * 30)

for user in clean_users:
    print(user)
print("Finished Cleaning up...")
print("-" * 30)
