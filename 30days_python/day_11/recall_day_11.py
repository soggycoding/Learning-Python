'''
def reverse_list(*items):
    for item in items[::-1]:
        print(item)

reverse_list('Bing', 'Bong', 'Boop', 'Bloop')
'''

'''
def capitalize_list_items(*items):
    return [str(item).upper() for item in items]

print(capitalize_list_items("bing", 'bong', 'boop'))
'''

'''
def add_item(item_list, item):
    item_list.append(item)
    return item_list

print(add_item(['iiting', 'biting'], 'wingwing'))
'''

'''
def remove_item(item_list, item):
    if item not in item_list:
        return "Item not in list"
    else:
        item = str(item)
        item_list.remove(item)
        return item_list

item_list = ['Banana', 'Apple', 'Mangga']
print(remove_item(item_list, 'Mangga'))
'''

'''
def sum_of_numbers(num):
    return (num * (num + 1)) // 2

print(sum_of_numbers(10))
'''

'''
def sum_of_odds(num):
    return sum(range(1, num + 1, 2))

print(sum_of_odds(5))
'''

'''
def sum_of_even(num):
    k = num // 2
    return k * (k + 1)

print(sum_of_even(5))
'''

'''
def evens_and_odds(num):
    even_counter = (num // 2) + 1
    odd_counter = (num + 1) // 2
    return f"Even numbers: {even_counter} \nOdd numbers: {odd_counter}"

print(evens_and_odds(100))
'''

'''
def factorial(num):
    acc = 1
    for i in range(1, num + 1):
        acc *= i
    return acc

print(factorial(6))
'''

'''
def is_empty(param):
    if param is None:
        return True
    else:
        return len(param) == 0

print(is_empty(''))
'''

'''
def calculate_mean(num):
    return sum(num) / len(num)

print(calculate_mean([25, 55, 35]))
'''

'''
import statistics

def calculate_median_import(num):
    return statistics.median(num)

print(calculate_median_import([1, 2, 3, 4]))
'''

'''
def calculate_range(nums):
    if not nums:
        return "Empty"
    max_num = max(nums)
    min_num = min(nums)
    result = max_num - min_num
    return result

print(calculate_range([-10, 0, 15, 25]))
'''

'''
def calculate_variance(nums):
    mean = sum(nums) / len(nums)
    variance = 0
    for i in nums:
        x = (i - mean)**2
        variance = variance + x
    total = variance / len(nums)
    return total
    
print(calculate_variance([1,2,3]))

import statistics
def calculate_variance(nums):
    return statistics.variance(nums)
print(calculate_variance([1,2,3]))
'''
'''
def calculate_mode(nums):
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return max(d, key=d.get)
print(calculate_mode([1,2,2,3,4]))
'''

'''
import statistics
def calculate_mode(nums):
    return statistics.multimode(nums)
print(calculate_mode([1,2,2,3,3,4,4,5]))
'''

'''
def calculate_variance(nums):
    mean = sum(nums) / len(nums)
    var = 0
    for i in nums:
        x = (i - mean)** 2
        var += x
    total = var / len(nums)
    return total

def calculate_std(nums):
    return calculate_variance(nums)**0.5

print(calculate_std([1,2,3]))
'''

'''
def greet(name="Guest"):
    resolved = name or "Guest"
    return f"Welcome {resolved}!"
print(greet("Soggy"))

def show_args(**user):
    if not user:
        return "Argument is empty"
    return "Received: " + ", ".join(f'{k}: {v}' for k, v in user.items())
print(show_args())
'''

# =====================================================================
# BATCHED SPACED RECALL: LEVEL 3 CHUNK (Day 11)
# =====================================================================
# Complete all 3 challenges below from pure memory without looking at
# exercise_day_11.py or alternative_day11_solution.py!
#
# ---------------------------------------------------------------------
# CHALLENGE 1: is_prime(num)
# ---------------------------------------------------------------------
# Contract: num (int) -> bool
# Guard Clauses: Numbers <= 1 are not prime.
# Flow Architecture:
# - Mathematical upper bound for factors is int(num ** 0.5) + 1.
# - Test divisibility from 2 up to the square root limit (loop or all(...)).
#
# Adversarial Test Matrix:
# - Standard: is_prime(7) -> True
# - Boundary: is_prime(1) -> False, is_prime(2) -> True
# - Trap: is_prime(9) -> False (odd composite!), is_prime(15) -> False
#
# ---------------------------------------------------------------------
# CHALLENGE 2: check_unique(items)
# ---------------------------------------------------------------------
# Contract: items (sequence) -> bool
# Guard Clauses: len <= 1 is inherently unique.
# Flow Architecture:
# - Either use a hash set tracker with O(1) early exit on first duplicate,
#   OR compare collection length against set conversion length.
#
# Adversarial Test Matrix:
# - Standard: check_unique([1, 2, 3]) -> True, check_unique([1, 2, 2, 3]) -> False
# - Boundary: check_unique([]) -> True, check_unique(['solo']) -> True
# - Trap: check_unique(['a', 'b', 'A']) -> True (case distinction)
#
# ---------------------------------------------------------------------
# CHALLENGE 3: same_data_type(data)
# ---------------------------------------------------------------------
# Contract: data (sequence) -> bool
# Guard Clauses: Empty sequence has 0 conflicting types (True).
# Flow Architecture:
# - Either use set comprehension to count unique type(item) instances (<= 1),
#   OR guard against empty, capture type of first item, and lazy-check with all(...).
#
# Adversarial Test Matrix:
# - Standard: same_data_type([1, 2, 3]) -> True, same_data_type([1, 'a', 3]) -> False
# - Boundary: same_data_type([]) -> True, same_data_type([42]) -> True
# - Trap: same_data_type([1, 1.0, 2]) -> False (int vs float), same_data_type([1, True, 0]) -> False (int vs bool)
#
# ---------------------------------------------------------------------
# WRITE YOUR IMPLEMENTATIONS BELOW FROM MEMORY:
'''
def is_prime(num):
    if num <= 1:
        return False
    max = int(num ** 0.5) + 1

    for i in range(2, max):
        if num % i == 0:
            return False
    return True
print(is_prime(2))
'''
'''
def check_unique(items):
    seen = set()
    for item in items:
        if item in seen:
            return False
        seen.add(item)
    return True
     # return len(items) == len(set(items))
print(check_unique([1,2,3]))
'''

def same_data_type(data):
    if not data:
        return True
    unique = type(data[0])
    for item in data:
        if type(item) != unique:
            return False
    return True

print(same_data_type([1, 2, 2]))