#LIST EXERCISES (5)

# 1. Filter + Transform
#
# Write a function that:
#
# Takes a list of integers
# Returns a new list with only even numbers, each multiplied by 2
#
# 👉 Example:
# [1, 2, 3, 4] → [4, 8]

def new_lists(d):
    sqrt_even_list = []
    even_list = []
    for k in d:
        if k % 2 == 0:
            sqrt_even_list.append(k * 2)
            even_list.append(k)
    return sqrt_even_list, even_list


d = new_lists([1,2,3,4,5,6,7,8,9])
print(d)




#2. Remove Duplicates (Keep Order)

# Write a function that:

# Takes a list
# Returns a new list with duplicates removed
# Must preserve original order

# 👉 Example:
# [1, 2, 2, 3, 1] → [1, 2, 3]

def remove_duplicates(d):
    lst = []
    for i in d:
        if i not in lst:
            lst.append(i)
    return lst

d = remove_duplicates([1,1,2,3,3,4,5,6,6])
print(d)



# 3. Find Second Largest
#
# Write a function that:
#
# Returns the second largest number
# Do NOT use sort()
#
# 👉 Example:
# [10, 5, 8, 20] → 10

def second_largests(d):
    largest = float('-inf')
    second_largest = float('-inf')
    for k in d:
        if k > largest:
            second_largest = largest
            largest = k
        elif k > second_largest and k != largest:
            second_largest = k
    return second_largest

d = second_largests([10, 5, 8, 20])
print(d)


# 4. Flatten a Nested List
#
# Write a function that:
#
# Takes a list like [1, [2, 3], [4, [5]]]
# Returns a fully flattened list
#
# 👉 Output:
# [1, 2, 3, 4, 5]

def flatten_lst(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_lst(item))
        else:
            flat_list.append(item)
    return flat_list

lst = flatten_lst( [1, [2, 3], [4, [5]]])
print(lst)




# 5. Sliding Window Sum
#
# Write a function that:
#
# Takes a list and integer k
# Returns list of sums of each window of size k
#
# 👉 Example:
# [1, 2, 3, 4], k=2 → [3, 5, 7]






# DICTIONARY EXERCISES (5)

# 1. Count Frequency
#
# Write a function that:
#
# Takes a list
# Returns a dictionary with frequency of each element
#
# 👉 Example:


# ['a', 'b', 'a'] → {'a': 2, 'b': 1}

def frequency_element(lst):
    frequency = {}
    for item in lst:
        if item not in frequency:
            frequency[item] = 1
        else:
            frequency[item] += 1
    return frequency
lst = frequency_element(['a', 'b', 'a', 'c', 'c', 'c'])
print(lst)

# 2. Invert Dictionary
#
# Write a function that:
#
# Swaps keys and values
# If duplicate values exist → store keys in a list
#
# 👉 Example:
# {'a': 1, 'b': 1} → {1: ['a', 'b']}

def swap_duplicate_value(lst):
    new_dict = {}
    for item, value in lst.items():
        if value not in new_dict:
            new_dict[value] = [item]
        else:
            new_dict[value].append(item)
    return new_dict

lst=  swap_duplicate_value({'a': 1, 'b': 1, 'c': 2, 'd': 3})
print(lst)


# 3. Group by First Letter
#
# Write a function that:
#
# Takes a list of words
# Groups them by first letter
#
# 👉 Example:
# ['apple', 'banana', 'apricot']
# → {'a': ['apple', 'apricot'], 'b': ['banana']}

# def groupping_by_letter(lst):
#     new_dict= {}
#
#     for item in lst:
#         word = item[0]
#         if word not in new_dict:
#             new_dict[word] = [item]
#         else:
#             new_dict[word].append(item)
#     return new_dict
#
# lst = groupping_by_letter(['apple', 'banana', 'apricot', 'coconut', 'car'])
# print(lst)


# 4. Nested Sum
#
# Write a function that:
#
# Takes a dictionary where values can be numbers or dictionaries
# Returns the total sum of all numbers
#
# 👉 Example:
# {'a': 10, 'b': {'c': 5, 'd': 15}} → 30

# def sum_of_numbers(lst):
#     total = 0
#     for value in lst.values():
#         if isinstance(value, dict):
#             total += sum_of_numbers(value)
#         else:
#             total += value
#     return total
#
# lst =  sum_of_numbers({'a': 10, 'b': {'c': 5, 'd': 15}})
# print(lst)
#
#


#===============================================PART TWO=================================

# 🟦 1. User Activity Aggregator (Logs → Features)
# Problem:
#
# You receive user activity logs:

# logs = [
#     {"user": "u1", "action": "click"},
#     {"user": "u2", "action": "view"},
#     {"user": "u1", "action": "purchase"},
#     {"user": "u2", "action": "click"},
# ]

# Task:
#
# Return:
# {
#     "u1": {"click": 1, "purchase": 1},
#     "u2": {"view": 1, "click": 1}
# }
#
# def aggregate_user_log(user_log):
#     aggregate_log = {}
#     for item in user_log:
#         for key, value in item.items():
#             if key not in aggregate_log:
#                 if key == 'user':
#                     aggregate_log[key] = value
#
#     return aggregate_log
#
# user_log = aggregate_user_log([
#     {"user": "u1", "action": "click"},
#     {"user": "u2", "action": "view"},
#     {"user": "u1", "action": "purchase"},
#     {"user": "u2", "action": "click"},
# ])
# print(user_log)










# 🟨 2. Flatten API JSON (Real Backend Problem)

# Problem:
#
# You get nested API data:
#
# data = {
#     "user": {
#         "id": 1,
#         "profile": {
#             "name": "John",
#             "skills": ["Python", "ML"]
#         }
#     }
# }

# Task:
#
# Flatten it into:
#
# {
#     "user_id": 1,
#     "user_profile_name": "John",
#     "user_profile_skills_0": "Python",
#     "user_profile_skills_1": "ML"
# }
#
# 👉 This is used in:
#
# Data pipelines
# ML preprocessing
# def flatten_dict(api, parent_key='', result=None):
#     if result is None:
#         result = {}
#
#     for key, value in api.items():
#         new_key = f"{parent_key}.{key}" if parent_key else key
#
#         if isinstance(value, dict):
#             flatten_dict(value, new_key, result)
#         elif isinstance(value, list):
#             for i, item in enumerate(value):
#                 result[f"{parent_key}.{i}"] = item
#         else:
#             result[new_key] = value
#     return result
#
#
#
# # Output
# api = {
#     "user": {
#         "id": 1,
#         "profile": {
#             "name": "John",
#             "skills": ["Python", "ML"]
#         }
#     }
# }
# print(flatten_dict(api))
#
#
#











#🟥 4. Transaction Analyzer (Finance Style)
# Problem:
# transactions = [
#     {"user": "u1", "amount": 100},
#     {"user": "u2", "amount": 200},
#     {"user": "u1", "amount": 50},
# ]
# Task:
#
# Return total spent per user:
#
# {
#     "u1": 150,
#     "u2": 200
# }
#
# 👉 Real-world use:
#
# Fintech
# Fraud detection
# ML features

# def transactions(api ):
#     total = {}
#
#     for item in api:
#         user = item["user"]
#         amount = item["amount"]
#
#         if user in total:
#             total[user] += amount
#         else:
#             total[user] = amount
#
#     return total
#
#
#
#
# api = [
#     {"user": "u1", "amount": 100},
#     {"user": "u2", "amount": 200},
#     {"user": "u1", "amount": 50},
# ]
# print(transactions(api))




# 🟥 1. Order Revenue Analyzer (E-commerce Style)

# def Revenue_analysis(orders):
#     revenue = {}
#
#     for order in orders:
#        store = order["store"]
#        price = order["price"]
#
#        if store in revenue:
#            revenue[store] += price
#        else:
#            revenue[store] = price
#     return revenue
#
# orders = [
#     {"store": "Nike", "price": 120},
#     {"store": "Adidas", "price": 80},
#     {"store": "Nike", "price": 200},
# ]
#
# print(Revenue_analysis(orders))



# 🟥 2. Employee Work Hours Tracker (HR Style)

# def hr_tracker(employees):
#     hr_tracker = {}
#
#     for employer in employees:
#         worker = employer["employee"]
#         hour = employer["hours"]
#
#         if worker in hr_tracker:
#             hr_tracker[worker] += hour
#         else:
#             hr_tracker[worker] = hour
#
#     return hr_tracker
#
#
#
# employees = [
#     {"employee": "John", "hours": 8},
#     {"employee": "Sarah", "hours": 6},
#     {"employee": "John", "hours": 5},
# ]
# print(hr_tracker(employees))



# 🟥 1. Monthly Expense Analyzer (Large Dataset)

# expenses = [
#     {"month": "Jan", "amount": 300},
#     {"month": "Feb", "amount": 200},
#     {"month": "Jan", "amount": 150},
#     {"month": "Mar", "amount": 500},
#     {"month": "Feb", "amount": 100},
#     {"month": "Apr", "amount": 250},
#     {"month": "Jan", "amount": 400},
#     {"month": "Mar", "amount": 100},
#     {"month": "May", "amount": 600},
#     {"month": "Apr", "amount": 300},
#     {"month": "Jun", "amount": 450},
#     {"month": "May", "amount": 200},
# ]


# Task:
#
# Return total expenses per month.



#🟥 2. Product Sales Counter (Large Dataset)

# sales = [
#     {"product": "Laptop"},
#     {"product": "Phone"},
#     {"product": "Laptop"},
#     {"product": "Tablet"},
#     {"product": "Laptop"},
#     {"product": "Phone"},
#     {"product": "Mouse"},
#     {"product": "Keyboard"},
#     {"product": "Tablet"},
#     {"product": "Phone"},
#     {"product": "Laptop"},
#     {"product": "Mouse"},
#     {"product": "Headphones"},
#     {"product": "Keyboard"},
#     {"product": "Laptop"},
# ]

# Task:
#
# Count how many times each product appears.




# 🟥 3. Highest Paid Employee Finder (Large Dataset)

# employees = [
#     {"name": "John", "salary": 5000},
#     {"name": "Sarah", "salary": 7000},
#     {"name": "Mike", "salary": 4500},
#     {"name": "David", "salary": 6200},
#     {"name": "Emma", "salary": 8100},
#     {"name": "Sophia", "salary": 7600},
#     {"name": "James", "salary": 6800},
#     {"name": "Olivia", "salary": 5400},
#     {"name": "Daniel", "salary": 9000},
#     {"name": "Liam", "salary": 7300},
# ]


# ask:
#
# Return employee with highest salary.





# 🟥 1. Fraud Transaction Detector

# transactions = [
#     {"user": "u1", "amount": 1200, "location": "NY", "time": "09:00"},
#     {"user": "u2", "amount": 80, "location": "CA", "time": "10:30"},
#     {"user": "u1", "amount": 3000, "location": "TX", "time": "09:10"},
#     {"user": "u3", "amount": 150, "location": "FL", "time": "11:00"},
#     {"user": "u2", "amount": 5000, "location": "CA", "time": "10:40"},
#     {"user": "u1", "amount": 50, "location": "NY", "time": "09:20"},
#     {"user": "u3", "amount": 7000, "location": "NV", "time": "11:05"},
# ]

# ask
#
# Return a list of suspicious transactions where:
#
# amount is greater than 2000, or
# the same user makes transactions from different locations within a short time






# 🟥 2. Top 3 Customers by Total Spending
# Problem


# orders = [
#     {"customer": "Alice", "amount": 250},
#     {"customer": "Bob", "amount": 400},
#     {"customer": "Alice", "amount": 100},
#     {"customer": "David", "amount": 900},
#     {"customer": "Bob", "amount": 200},
#     {"customer": "Emma", "amount": 700},
#     {"customer": "Alice", "amount": 300},
#     {"customer": "David", "amount": 150},
#     {"customer": "Emma", "amount": 100},
#     {"customer": "Frank", "amount": 1200},
#     {"customer": "Bob", "amount": 50},
#     {"customer": "Grace", "amount": 650},
# ]



# Task
# Calculate total spending per customer
# Return the top 3 highest spending customers
# Concepts tested
# grouping totals
# sorting dictionaries
# ranking
# transforming output format
# Real-world use
# e-commerce analytics
# customer segmentation
# loyalty programs
# ML customer value features






# features
# 🟥 3. Inventory Stock Report Generator

# inventory = [
#     {"product": "Laptop", "in": 20, "out": 5},
#     {"product": "Phone", "in": 50, "out": 10},
#     {"product": "Laptop", "in": 10, "out": 8},
#     {"product": "Tablet", "in": 30, "out": 15},
#     {"product": "Phone", "in": 20, "out": 25},
#     {"product": "Mouse", "in": 100, "out": 40},
#     {"product": "Keyboard", "in": 60, "out": 20},
#     {"product": "Tablet", "in": 10, "out": 5},
#     {"product": "Laptop", "in": 5, "out": 12},
# ]


# Task
#
# Return a final stock report per product:
#
# total stock in
# total stock out
# remaining stock = in - out
# mark product as "LOW" if remaining stock is less than 10


# Concepts tested
# nested dictionary building
# accumulation
# computed fields
# business rule flags
# Real-world use
# warehouse systems
# supply chain dashboards
# retail stock management


# 🟢 Beginner Level

# 1. Unique Visitor Counter (Sets)
#
# A website logs usernames visiting today:

# ["john", "mary", "john", "alex", "mary", "kevin"]

# Task:
#
# Use a set to print:
#
# Total unique visitors
# Names of unique visitors
#
# 👉 Real world: Website analytics

def visitor_counter(people):
    unique_visitor = set()
    for person in people:
        unique_visitor.add(person)
    return unique_visitor

people = ["john", "mary", "john", "alex", "mary", "kevin"]
print(visitor_counter(people))







# 2. Login Access Checker (Input + Conditional)
#
# Ask user:
# Enter password:
# password is "admin123":
#
# Access Granted
#
# Else:
#
# Access Denied
#
# 👉 Real world: Login systems

def access_checkr(username):


        if username == "admin123":
            return "Access granted"

        else:
            return "Access denied"
username = input("Please enter your username: ")
print(access_checkr(username))

# 3. Age Restriction App
#
# Ask user age.
#
# If:
#
# Under 18 → "Minor"
# 18 to 64 → "Adult"
# 65+ → "Senior"
#
# 👉 Real world: Insurance / Ticket pricing

def restriction_app(age):
    if age >= 65:
        return "You're Senior"
    elif age >= 18 and age <= 64:
        return "You're an Adult"
    else:
        return "You're a Minor"

age = int(input("Please enter your age: "))
print(restriction_app(age))



# pricing
#
# 🟡 Intermediate Level
# 4. Remove Duplicate Products (Sets)
#
# Store products scanned in warehouse:
# ["TV", "Phone", "TV", "Laptop", "Phone", "Tablet"]
# Task:
#
# Print clean unique product list.
#
# 👉 Real world: Inventory system

def duplicate_product(lst):
    new_product_list = set()
    for item in lst:
        new_product_list.add(item)
    return list(new_product_list)

lst =  ["TV", "Phone", "TV", "Laptop", "Phone", "Tablet"]
print(duplicate_product(lst))






# 5. Country Shipping Checker (Conditional + Input)
#
# Allowed shipping countries:
#
# USA, Canada, UK
#
# Ask user country.
#
# If country allowed:
#
# Shipping Available
#
# Else:
#
# Shipping Not Available
#
# 👉 Real world: E-commerce checkout

def shipping_checkr(country):

    if country == "UK" or country == "USA" or country == "Canada":
        return "Shipping Available"
    else:
        return "Shipping Not Available"


country = input("Please enter your country: ")
print(shipping_checkr(country))








# 6. Frozen Set VIP Permissions
#
# Create VIP permissions:

# {"lounge", "priority boarding", "free meal"}

# Store it as frozenset
#
# Then print:
#
# All permissions
# Check if "free meal" exists
#
# 👉 Real world: Airline memberships


def airline_membership(info):
    vip_permission = set()
    for item in info:
        vip_permission.add(item)
    vip_permission = frozenset(vip_permission)
    if "free meal" in vip_permission:
        print("Free Meal")
    return vip_permission



info = {"lounge", "priority boarding", "free meal"}
print(airline_membership(info))




# 🟠 Advanced Level
# 7. Fraud Detection by Duplicate IPs
#
# Login IP addresses:
# ["192.1.1.1", "192.1.1.2", "192.1.1.1", "10.0.0.1"]

# Task:
#
# Find duplicated IP addresses only.
#
# 👉 Real world: Cybersecurity fraud detection








# 8. Student Enrollment Match (Sets)
#
# Math students:
# {"John", "Mary", "Alex", "David"}

# Science students:
#
# {"Mary", "Alex", "Sarah"}

# Task:
#
# Print:
#
# Students in both classes
# Only Math
# Only Science
#
# 👉 Real world: University systems







# 9. Smart ATM Machine
#
# Ask user:
#
# Account balance
# Withdraw amount
#
# Rules:
#
# If withdraw > balance → "Insufficient Funds"
# If withdraw <= balance → show remaining balance
# If amount <= 0 → "Invalid Amount"
#
# 👉 Real world: Banking systems







# 🔴 Expert Level
# 10. Dynamic Access Control System
#
# Allowed roles:
#
# {"admin", "manager", "staff"}
#
# Ask user role + department.
#
# Rules:
#
# Admin can access all
# Manager only "sales" or "hr"
# Staff only "support"
# Else deny access
#
# 👉 Real world: Company internal systems







# 🔥 BONUS CHALLENGE (Very Real World)
# 11. Blacklist Checker
#
# Blacklisted emails:
#
# {"spam@gmail.com", "bot@yahoo.com"}
#
# Ask user email.
#
# If blacklisted:
#
# Blocked
#
# Else:
#
# Welcome
















# 🟢 Problem 1: E-Commerce Fraud & Order Analyzer
#
# A store receives orders from many users.

# orders = [
#     {"user": "u1", "email": "a@gmail.com", "ip": "1.1.1.1", "amount": 120},
#     {"user": "u2", "email": "b@gmail.com", "ip": "2.2.2.2", "amount": 450},
#     {"user": "u3", "email": "a@gmail.com", "ip": "3.3.3.3", "amount": 50},
#     {"user": "u4", "email": "d@gmail.com", "ip": "1.1.1.1", "amount": 900},
#     {"user": "u5", "email": "e@gmail.com", "ip": "5.5.5.5", "amount": 200}
# ]

# 🎯 Tasks
#
# Build a system that:
#
# 1. Detect duplicate emails
#
# (One email used by multiple accounts)
#
# 2. Detect duplicate IPs
#
# (Many users ordering from same IP)
#
# 3. Total money spent by each user
#
# Example:
# {
#  "u1": 120,
#  "u2": 450
# }
# 4. Flag suspicious orders:
#
# If:
#
# amount > 500
# OR
# duplicate IP used
#
# Then:
#
# Suspicious
# 5. Count safe vs suspicious orders
# 👉 Real World Use
# Amazon fraud detection
# Shopify risk systems
# Payment security teams
















# 🔥 Problem 2: Smart Employee Attendance & Bonus System
#
# A company tracks daily check-ins.
#
# attendance = [
#     {"name": "John", "department": "Sales", "days": 24},
#     {"name": "Mary", "department": "HR", "days": 19},
#     {"name": "Alex", "department": "Sales", "days": 26},
#     {"name": "John", "department": "Sales", "days": 24},
#     {"name": "Sarah", "department": "IT", "days": 28}
# ]
# 🎯 Tasks
#
# Build a system that:
#
# 1. Remove duplicate employee records
#
# (Use set logic)
#
# 2. Count employees per department
#
# Example:
#
# {
#  "Sales": 2,
#  "HR": 1,
#  "IT": 1
# }
# 3. Assign bonus using conditions:
#
# If days worked:
#
# 26+ → $1000 bonus
# 22–25 → $500
# Below 22 → $0
# 4. Find top attendance employee
# 5. Print employees who qualify for bonus
# 👉 Real World Use
# HR payroll systems
# Attendance dashboards
# Corporate analytics