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

def groupping_by_letter(lst):
    new_dict= {}

    for item in lst:
        word = item[0]
        if word not in new_dict:
            new_dict[word] = [item]
        else:
            new_dict[word].append(item)
    return new_dict

lst = groupping_by_letter(['apple', 'banana', 'apricot', 'coconut', 'car'])
print(lst)


# 4. Nested Sum
#
# Write a function that:
#
# Takes a dictionary where values can be numbers or dictionaries
# Returns the total sum of all numbers
#
# 👉 Example:
# {'a': 10, 'b': {'c': 5, 'd': 15}} → 30

def sum_of_numbers(lst):
    total = 0
    for value in lst.values():
        if isinstance(value, dict):
            total += sum_of_numbers(value)
        else:
            total += value
    return total

lst =  sum_of_numbers({'a': 10, 'b': {'c': 5, 'd': 15}})
print(lst)




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

def aggregate_user_log(user_log):
    aggregate_log = {}
    for item in user_log:
        for key, value in item.items():
            if key not in aggregate_log:
                if key == 'user':
                    aggregate_log[key] = value

    return aggregate_log

user_log = aggregate_user_log([
    {"user": "u1", "action": "click"},
    {"user": "u2", "action": "view"},
    {"user": "u1", "action": "purchase"},
    {"user": "u2", "action": "click"},
])
print(user_log)










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









# 🟩 3. Top K Frequent Words (NLP Style)
# Problem:
# words = ["ai", "ml", "ai", "data", "ml", "ai"]
# k = 2
# Task:
#
# Return:
#
# ["ai", "ml"]
#
# 👉 This is used in:
#
# Search engines
# NLP models







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









# 🟪 5. Detect Duplicate Emails (Data Cleaning)

# Problem:
# emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]
# Task:
#
# Return:
#
# ["a@gmail.com"]
#
# 👉 Real-world use:
#
# Cleaning datasets before ML







# ⚫ 7. Group Products by Category (E-commerce)
# Problem:
# products = [
#     {"name": "shirt", "category": "clothing"},
#     {"name": "pants", "category": "clothing"},
#     {"name": "phone", "category": "electronics"},
# ]
# Task:
# {
#     "clothing": ["shirt", "pants"],
#     "electronics": ["phone"]
# }
#
# 👉 Same pattern as your previous exercise — but real-world








# 🔵 8. Merge Two Feature Dictionaries

# Problem:
# user1 = {"clicks": 10, "views": 5}
# user2 = {"clicks": 3, "purchases": 2}
# Task:
# {"clicks": 13, "views": 5, "purchases": 2}
#
# 👉 This is EXACTLY ML feature merging










