from time import sleep


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
# 
# log_data = [
#     "INFO: System booted successfully.",
#     "INFO: User 'admin' logged in.",
#     "WARNING: High CPU usage detected.",
#     "INFO: Database backup completed.",
#     "CRITICAL: Firewall breached!",
#     "INFO: User 'guest' logged out.",
#     "CRITICAL: Power supply failure!",
#     "CRITICAL: Water breached!",
# "CRITICAL: Electricity breached!",
# ]
# 
# def log_reader(logs):
#     for log in logs:
#         time.sleep(0.5)
#         yield log
# 
# 
# def critical_alert_system(log_stream):
#     for line in log_stream:
#         if "WARNING" in line:
#             yield f"🚨 ALARM: {line}"
# 
# 
# 
# stream = log_reader(log_data)
# alert = critical_alert_system(stream)
# 
# print("Starting security monitor...")
# print("-" * 30)
# 
# for alert in alert:
#     print(alert)
# 
# print("-" * 30)
# print("Monitoring finished.")
# 
# 
# #===============sushi
# 
# def make_sushi(number_sushi):
#     sushi = 1
#     while sushi <= number_sushi:
#         yield sushi
#         sushi += 1
# 
# 
# sushis = make_sushi(10)
# print(next(sushis))
# print(next(sushis))
# print(next(sushis))
# for sushi in sushis:
#     print(sushi)
# 
# 
# 
# #+==================================
# import time
# import random
# 
# def temperature_stream():
#     readings = [70,72,78,74,81,71,91,100]
#     for temp in readings:
#         time.sleep(0.5)
#         yield temp
# 
# def heat_temperature_alert(logs):
#     for log in logs:
#         time.sleep(0.5)
#         if log >= 75:
#             yield f"🔥 WARNING: High Temp Detected: {log}"
# 
# 
# logs = temperature_stream()
# temperature = heat_temperature_alert(logs)
# print("Starting security monitor...")
# print("-" * 30)
# for temps in temperature:
#     print(temps)
# print("-" * 30)
# print("Monitoring finished.")
# 
# 
# 
# 
# #Problem 2: The E-Commerce Price Converter (Transforming Data)
# 
# def usd_price_stream():
#     prices = [10.0, 25.5, 99.9, 5.0]
#     for price in prices:
#         time.sleep(0.5)
#         yield price
# 
# def euro_convertor(prices):
#     for price in prices:
#         yield f"Euro: ${price * 0.92:.2f}"
# 
# usd_stream= usd_price_stream()
# euro = euro_convertor(usd_stream)
# print("Starting money convertor...")
# print("-" * 30)
# for price in euro:
#     print(price)
# 
# print("End money convertor...")
# print("-" * 30)
# 
# 
# 
# # Problem 3: The Username Cleaner (Data Cleaning)
# 
# def usernames():
#     messy_signups = ["  alice   ", "BOB  ", "   ", "charlie_99", "  DEBBY "]
#     for signup in messy_signups:
#         time.sleep(0.5)
#         yield signup
# 
# def cleanup_messy_data(messy_data):
#     for user in messy_data:
#         if user == " ":
#             messy_data.remove(user)
#         else:
#             user = user.strip().lower()
#             yield f"Here the cleanup username: {user}"
# 
# users = usernames()
# clean_users = cleanup_messy_data(users)
# print("Cleaning up...")
# print("-" * 30)
# 
# for user in clean_users:
#     print(user)
# print("Finished Cleaning up...")
# print("-" * 30)
# 
# 
# 



# Problem 1: The Bio-Data Clean (Using map)

heights_cm = [160, 185, 152, 170, 192]

convert_m = map(lambda x: x/100, heights_cm)
print(list(convert_m))

#Problem 2: The Spam Filter (Using filter)
messages = ["Hi", "Hello world!", "Test", "Python is fun", "Thx", "Good morning"]

filter_out_msg = filter(lambda msg: len(msg) >= 5, messages)
print(list(filter_out_msg))


# Problem 3: The Order Totaler (Using reduce)
from functools import reduce
cart_prices = [5.99, 12.50, 3.00, 45.00, 1.25]

total_bill = reduce(lambda x, y: x + y, cart_prices)
print(f"total_bill: ${total_bill:.2f}")


# Problem 4: The Inventory Discounter (Combining filter and map)
inventory_prices = [25, 60, 15, 120, 45, 80]
over_priced = filter(lambda price: price > 50, inventory_prices)
discounted_price = map(lambda p: p * 0.8, over_priced)
print(list(discounted_price))


# Problem 5: Word Length Sum (Combining map and reduce)
words = ["apple", "banana", "cherry"]
words_length = map(lambda word: len(word), words)

reduce_words = reduce(lambda x, y: x + y, words_length)
print(reduce_words)



# The Uber/Lyft Surge Pricing Engine.


import time
from functools import reduce

def live_trip_stream():
    trips = [
        {"passenger": "Alice", "base_fare": 10.0, "rush_hour": True},
        {"passenger": "Bob", "base_fare": 25.0, "rush_hour": False},
        {"passenger": "Charlie", "base_fare": 15.0, "rush_hour": True},
        {"passenger": "David", "base_fare": 8.0, "rush_hour": False},
        {"passenger": "Eva", "base_fare": 20.0, "rush_hour": True}
    ]

    for trip in trips:
        time.sleep(0.5)
        yield trip

incoming_trips = live_trip_stream()
rushed_hours = filter(lambda trip: trip["rush_hour"], incoming_trips)

surged_fares = map(lambda trip: trip["base_fare"], rushed_hours)

total_revenue = reduce(lambda x, y: x + y, surged_fares)
print(f"💰 Total Rush-Hour Surge Revenue: ${total_revenue:.2f}")



# Digital Advertising Analytics Engine (like Google Ads or Facebook Ads).

def ad_campaign_stream():
    campaigns = [
        {"ad_name": "Summer Shoes Promo", "ctr": 2.5, "spend": 100, "revenue": 450},
        {"ad_name": "Winter Coat Clearance", "ctr": 1.2, "spend": 200, "revenue": 300},
        {"ad_name": "Watch Flash Sale", "ctr": 3.1, "spend": 50, "revenue": 500},
        {"ad_name": "Backpack Banner Ad", "ctr": 0.8, "spend": 80, "revenue": 90},
        {"ad_name": "Bogo Socks Video Ad", "ctr": 4.0, "spend": 150, "revenue": 600}
    ]
    for campaign in campaigns:
        time.sleep(0.5)
        yield campaign

live_ads = ad_campaign_stream()

filter_out_ads = filter(lambda ad: ad["ctr"] > 2.0, live_ads)

revenue = map(lambda ad: ad["revenue"], filter_out_ads)

total_revenue = reduce(lambda x, y: x + y, revenue)
print(f"💰 Total revenue of the ads: ${total_revenue:.2f}")






#======Problem 1: Fraudulent Transaction Detector=============

def fraud_detection():
    transactions = [
        {"user": "Alice", "amount": 1200, "is_international": False},
        {"user": "Bob", "amount": 6500, "is_international": True},
        {"user": "Charlie", "amount": 8000, "is_international": False},
        {"user": "David", "amount": 300, "is_international": True},
        {"user": "Eva", "amount": 5200, "is_international": True}
    ]

    for transaction in transactions:
        time.sleep(0.5)
        yield transaction

frauds = fraud_detection()


high_transactions = filter(lambda tx: tx["amount"] > 5000 and tx["is_international"], frauds)

user_names = map(lambda user: user["user"], high_transactions)

print(list(user_names))


#=======Problem 2: Warehouse Restock Value=================
def ware_house_stream():
    items = [
        {"name": "Wireless Mouse", "stock": 5, "restock_cost": 20},
        {"name": "Mechanical Keyboard", "stock": 25, "restock_cost": 70},
        {"name": "Gaming Monitor", "stock": 2, "restock_cost": 250},
        {"name": "USB-C Cable", "stock": 50, "restock_cost": 5},
        {"name": "Desk Mat", "stock": 8, "restock_cost": 15}
    ]
    for item in items:
        time.sleep(0.5)
        yield item


live_inventory = ware_house_stream()

stocks = filter(lambda item: item["stock"] < 10, live_inventory)

low_stocks = map(lambda item: item["restock_cost"], stocks)

total_amount = reduce(lambda x, y: x + y, low_stocks)

print(f"💰 Total replacement stocks: ${total_amount:.2f}")


# Problem 2: Tri-Zipping Inventory
products = ["Wireless Mouse", "Mechanical Keyboard", "Gaming Monitor"]
stock = [15, 0, 4]
prices = [25.00, 75.00, 250.00]

inventory = zip(products, stock, prices)
for name, stock, price in inventory:
    time.sleep(0.5)
    print(f"{name} costs ${price:.2f} ({stock:.2f} left in stock) ")


# Problem 3: Coordinate Addition (Using List Comprehension)
x_coords = [10, 20, 30, 40]
y_coords = [5, 15, 25, 35]

result = list(zip(x_coords, y_coords))
print(result)


#Problem 4: Setting Up User Accounts (zip + dict)
employee_ids = [101, 102, 103, 104]
employee_names = ["Rachel", "Monica", "Chandler", "Joey"]

employee_profiles = dict(zip(employee_ids, employee_names))
print(employee_profiles)


# Problem 5: The Ultimate Combo (zip + map)
fruits = ["Apples", "Bananas", "Cherries"]
base_prices = [2.00, 1.00, 4.00]

combo = dict(zip(fruits, base_prices))
print(combo)
result = map(lambda item: f"{item[0]}: ${item[1] * 1.10:.2f}", combo.items())
print(list(result))



#====Problem 1: User Logins and Timestamps======
users = ["charlie_dev", "emma_secure", "admin_sam"]
timestamps = ["14:22:05", "14:23:11", "14:25:40"]

users_logs = zip(users, timestamps)

for user, timestamp in users_logs:
    time.sleep(0.5)
    print(f"{user} has logged in at {timestamp}")


#=========Problem 2: Tracking Score Differences====================
week1_scores = [14, 21, 7, 28]
week2_scores = [24, 21, 14, 35]

scores = zip(week1_scores, week2_scores)
results = map(lambda score: score[1] - score[0], scores )
print(list(results))



# Problem 3: Merging Config Settings (zip + dict)

elements = ["background", "text", "buttons", "borders"]
dark_colors = ["#121212", "#FFFFFF", "#1F1F1F", "#333333"]

config_setting = dict(zip(elements, dark_colors))
print(config_setting)


#========Problem 1: The Input Logger (*args practice)=============

def log_arguments(func):

    def wrapper(*args, **kwargs):
        print("📝 System Log - Arguments given:")
        func(*args, **kwargs)

    return wrapper

@log_arguments
def greet_user(name, age):

    print(f"Hello {name}, you are {age} years old.")

greet_user("Bob", 25)


# Problem 2: The Double Trouble Decorator (Return Value practice)
def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) * 2
        return result
    return wrapper

@double_result
def add_scores(base_score, bonus_score):
    return base_score + bonus_score

final_score = add_scores(5, 10)
print(final_score)


# Problem 3: The HTML Text Stylist (String Transformation practice)
def make_bold(func):
    def wrapper(*args, **kwargs):
        html= f"<b>{func(*args, **kwargs)}</b>"
        return html
    return wrapper

@make_bold
def get_announcement(topic):
    return f"System Update: {topic} is now live!"

print(get_announcement("Python 3.12"))


# Problem 4: The Performance Stopwatch (Real-World practice)
def calculate_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
    return wrapper

@calculate_time
def process_heavy_data():
    print("Parsing files...")
    time.sleep(0.8)
    return "Data Processed Successfully"

status = process_heavy_data()
print(status)


# Problem 5: The Execution Counter (State Management practice)
# def count_calls(func):
#
#
#     def wrapper(count=None,*args, **kwargs):
#
#         func(*args, **kwargs)
#
#
#         wrapper.count = wrapper.count + 1
#         return count
#
#     return wrapper
#
# @count_calls
# def send_notification():
#     print("Notification sent!")
#
#
# send_notification()
# send_notification()
# send_notification()


#===============Data for Problem 1: Global Shipping Logistics Router===================



def shippment_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️ {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def shipping_generator():
    shipments = [
        {"vessel": "Pacific Titan", "weight_kg": 500_000, "is_international": True},
        {"vessel": "Atlantic Breeze", "weight_kg": 80_000, "is_international": False},
        {"vessel": "Northern Explorer", "weight_kg": 1_200_000, "is_international": True},
        {"vessel": "Coastal Express", "weight_kg": 30_000, "is_international": False},
        {"vessel": "Orient Star", "weight_kg": 750_000, "is_international": True}
    ]
    for shipment in shipments:
        time.sleep(0.5)
        yield shipment



@shippment_decorator
def run_logistic_pipeline():
    docking_codes = ["DOCK-ALPHA", "DOCK-BETA", "DOCK-GAMMA"]
    shipping_stream = shipping_generator()

    filtering_shipment = filter(lambda s: s["is_international"], shipping_stream)
    mapping_shipment = map(lambda s: s["weight_kg"] / 1000, filtering_shipment)
    zip_shipment = zip(mapping_shipment, docking_codes)
    total_tonnage = reduce(lambda x, y: x + y[0], zip_shipment, 0)

    return total_tonnage

final_weight = run_logistic_pipeline()
print(f"Total Fleet Weight: {final_weight} Tons")




#===================Instructions for Problem 2: Crypto Whales Transaction Flagging=======================
def track_fraud_scans(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"🔒 Security Sweep #{wrapper.count} Active...")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


def block_chain_stream():
    ledger = [
        {"tx_id": "0xABC123", "amount_usd": 15_000, "asset": "BTC"},
        {"tx_id": "0xXYZ789", "amount_usd": 750_000, "asset": "ETH"},
        {"tx_id": "0xDEF456", "amount_usd": 2_500, "asset": "SOL"},
        {"tx_id": "0xMNO987", "amount_usd": 1_100_000, "asset": "BTC"},
        {"tx_id": "0xGHI321", "amount_usd": 450_000, "asset": "ETH"}
    ]
    for entry in ledger:
        time.sleep(0.5)
        yield entry

@track_fraud_scans
def block_chain_pipeline():
    risk_tags = ["TIER_3_HIGH_RISK", "TIER_4_CRITICAL", "TIER_2_MODERATE"]
    live_blockchain_feed = block_chain_stream()

    filter_scans = filter(lambda s: s["amount_usd"] > 100_000, live_blockchain_feed)
    map_scans = map(lambda s: s["amount_usd"] * 0.005, filter_scans)
    zip_scans = zip(map_scans, risk_tags)
    sum_scans = reduce(lambda x, y: x + y[0], zip_scans, 0)
    return sum_scans

final_fraud_scans = block_chain_pipeline()
print(f"Higher scans fraud detected: {final_fraud_scans}")







#====================Problem 1: The Multi-Currency Converter=======================
def cache_rates(func):

    notepad  = {}
    def wrapper(*args):
        if args in notepad:
            print("⚡ [CACHE HIT] Answer found in notepad!")
            return notepad[args]
        result = func(*args)
        notepad[args] = result
        return result
    return wrapper

@cache_rates
def get_exchange_rate(from_currency, to_currency):
    print(f"💰 Fetching live rates from the web for {from_currency} -> {to_currency}...")
    # Simulated live exchange rate multiplier
    return 1.12



# Problem 2: The Video Game Math Engine

def engine_cache(func):
    notepad = {}
    def wrapper(*args):
        if args in notepad:
            print("⚡ [CACHE HIT] Answer found in notepad!")
            return notepad[args]
        result = func(*args)
        notepad[args] = result
        return result
    return wrapper

@engine_cache
def calculate_distance(x, y):
    print(f"🧮 Running heavy coordinate physics math for position ({x}, {y})...")
    # Simulated distance calculation result
    return (x**2 + y**2)**0.5


print(calculate_distance(10, 20))
print(calculate_distance(10, 20)) # Should hit the cache!
print(calculate_distance(5, 5))
print(calculate_distance(5, 5))
print(calculate_distance(5, 5))




print(get_exchange_rate("USD", "EUR"))
print(get_exchange_rate("GBP", "USD"))
print(get_exchange_rate("USD", "EUR"))


# Problem 3: The Multi-Argument DB Query Cache


