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
'''

# =====================================================================
# BATCHED SPACED RECALL: LEVEL 3 COMPLETION (Day 11)
# =====================================================================
# Complete all challenges below from pure memory without looking at
# exercise_day_11.py or alternative_day11_solution.py!
#
# ---------------------------------------------------------------------
# CHALLENGE 1: is_valid_variable(name)
# ---------------------------------------------------------------------
# Contract: name (str) -> bool
# Guard Clauses:
# - Must be a non-empty string.
# Flow Architecture:
# - Validate that the string is a syntactically legal Python identifier
#   AND is NOT a reserved language keyword.
# - You may use string validation methods + keyword module, OR manual character parsing.
#
# Adversarial Test Matrix:
# - Standard: is_valid_variable('user_name') -> True, is_valid_variable('_counter') -> True
# - Boundary: is_valid_variable('') -> False, is_valid_variable('_') -> True
# - Trap:     is_valid_variable('1st_var') -> False, is_valid_variable('for') -> False, is_valid_variable('var-name') -> False
#
# ---------------------------------------------------------------------
# CHALLENGE 2: most_spoken_languages(data, top_n=10)
# ---------------------------------------------------------------------
# Contract: data (list of dicts), top_n (int, default 10) -> dict or list
# Flow Architecture:
# - Aggregate the occurrence count of each language across all country records.
# - Rank the counts in descending order and slice the top `top_n`.
# - Choose either:
#   * Manual dictionary frequency count + sorted(), OR
#   * List comprehension flattening + Counter.most_common().
#
# Adversarial Test Matrix:
# - Standard: most_spoken_languages(countries_data, 10) -> top 10 languages
# - Boundary: most_spoken_languages(countries_data, 1)  -> top 1 language
# - Trap:     most_spoken_languages([], 5)              -> empty result ({})
#
# ---------------------------------------------------------------------
# CHALLENGE 3: most_populated_countries(data, top_n=10)
# ---------------------------------------------------------------------
# Contract: data (list of dicts), top_n (int, default 10) -> list or dict
# Flow Architecture:
# - Rank countries in descending order based on their population value.
# - Slice the top `top_n` records and return.
# - Choose either:
#   * Direct in-situ keyed sort: sorted(..., key=..., reverse=True)[:top_n], OR
#   * Map to country: population pairs, sort, and slice.
#
# Adversarial Test Matrix:
# - Standard: most_populated_countries(countries_data, 10) -> top 10 populated countries
# - Boundary: most_populated_countries(countries_data, 1)  -> top 1 populated country
# - Trap:     most_populated_countries([], 5)              -> empty result ([])
#
# ---------------------------------------------------------------------
# WRITE YOUR IMPLEMENTATIONS BELOW FROM MEMORY:
'''
import keyword
def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)
print(is_valid_variable(""))
'''
'''
from collections import Counter
from countries_data import countries_data

def most_spoken_language(data, top_n=10):
    language_list = {}
    for language in data:
        lang = language['languages']
        for spoken_language in lang:
            if spoken_language in language_list:
                language_list[spoken_language] += 1
            else:
                language_list[spoken_language] = 1
    sorted_list = sorted(language_list.items(), key=lambda item:item[1], reverse=True)[:top_n]
    return sorted_list
print(most_spoken_language(countries_data, 10))
'''
