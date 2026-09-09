# Functions Exercises - Day 11

'''
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(21, 31))

def area_of_circle(r):
    PI = 3.14
    area = PI * (r ** 2)
    return area
print(area_of_circle(10))
'''

'''
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            print(f"Argument {num} is not a valid number")
            return None
        total += num 
    return total
print(add_all_nums(23, 24, 26))
'''

'''
def convert_celcius_to_fahrenheit(celc):
    fahrenheit = (celc * 9 / 5) + 32
    return fahrenheit
print(convert_celcius_to_fahrenheit(24))
'''

'''
def check_season(month):
    month = month.capitalize()
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August'] 
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    if month in spring:
        return "Spring"
    if month in summer:
        return "Summer"
    if month in autumn:
        return "Autumn"
    if month in winter:
        return "Winter"
    return "Invalid month"

print(check_season("February"))
'''

'''
def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(2, 5, 10, 1))
'''

'''
import math

def solve_quadratic_eqn(a, b, c):
    # ax^2 + bx + c = 0 -> x = (-b ± sqrt(b^2 - 4ac)) / 2a
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "No real roots"

print(solve_quadratic_eqn(1, -5, 6))
'''

'''
def print_list(*items):
    for element in items:
        print(element)
print_list('potato', 'banana', 'hotdog', 'bente', 'wiowiwi')
'''

'''
def reverse_list(*items):
    item_list = []
    for item in items:
        item_list.append(item)
    item_list.reverse()
    return item_list

print(reverse_list('bing', 'bong', 'doot', 'bloop'))
'''

'''
def capitalize_list_items(*items):
    #item_list = []
    for item in items:
        #item_upper = item.upper()
        item = str(item)
        item = item.upper()
        print(item)
capitalize_list_items('bing', 'bong', 'boop')
'''

'''
def add_item(item_list, item):
    item = str(item)
    item_list.append(item)
    return item_list
item_list = ['Potato', 'Tomato', 'Brotato']
print(add_item(item_list, 'Bed'))
'''

'''
def remove_item(item_list, item):
    item_list.remove(item)
    return item_list
print(remove_item(['Bing', 'Bong', 'Boop'], 'Bong'))
'''

'''
def sum_of_numbers(num):
    num = int(num)
    num_plus = 0
    for i in range(0,num):
        i = i + 1
        num_plus = num_plus + i
    return num_plus
print(sum_of_numbers(10))
'''

'''
def sum_of_odds(num):
    num_plus = 0
    for i in range(0,num + 1):
        if i % 2 == 0: 
            pass
        else:
            num_plus = num_plus + i
    return num_plus
print(sum_of_odds(5))
'''

'''
def sum_of_even(num):
    return sum(range(2, num + 1, 2))
print(sum_of_even(5))
'''

# Exercise 2:

'''
def evens_and_odds(num):
    even = 0
    odds = 0
    for i in range (0, num + 1):
        if i % 2 == 0:
            even += 1
        else:
            odds += 1
    result_even = "The number of even numbers are"
    result_odds = "The number of odd numbers are"
    return {result_even: even, 
            result_odds: odds}
print(evens_and_odds(100))
'''

'''
def factorial(num):
    fact = num
    for i in range(num, 1, -1):
        i = i - 1
        fact = fact * i
    return fact
print(factorial(6))
'''

'''
def is_empty(param):
    if len(param) == 0:
        return "empty parameter"
    else:
        return "parameter has value"
print(is_empty([]))
'''

'''
def calculate_mean(num):
    sort_number = sorted(num)
    acc = 0
    for i in sort_number:
        acc += i
    return acc / len(sort_number)
print(calculate_mean([1, 2]))
'''


'''
def calculate_median(num):
    sorted_num = sorted(num)
    n = len(sorted_num)
    if n % 2 != 0:
        return sorted_num[n // 2]
    else:
        middle1 = sorted_num[(n // 2) - 1]
        middle2 = sorted_num[n // 2]
        return (middle1 + middle2) / 2
print(calculate_median([1, 2, 3 ,4]))
'''

'''
def calculate_mode(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return max(d, key=d.get)
print(calculate_mode([1, 2, 3, 3, 4]))
'''


'''
def calculate_range(list_of_number):
    number_range = max(list_of_number) - min(list_of_number)
    return number_range
print(calculate_range([1, 2, 3, 4]))
'''
'''
def calculate_variance(num):
    mean = sum(num) / len(num)
    total_sum = 0
    for i in num:
        total_sum += (i - mean)**2
    variance = (total_sum / len(num))
    return variance
print(calculate_variance([1,2,3]))
'''


'''
def calculate_std(nums):
    mean = sum(nums) / len(nums)
    var = 0
    for i in nums:
        x = (i - mean)** 2
        var += x
    total = var / len(nums)
    std = total**0.5
    return std
print(calculate_std([1,2,3]))
'''

'''
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()
'''

'''
def show_args(**user):
    user_info = []
    received = "Received: "
    for key, value in user.items():
        user_info.append(f"{key}: {value}")
    formatted = ', '.join(user_info)
    return received + formatted
print(show_args(name='Soggy', age=30, city='Bingbong Island'))
'''

'''
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_prime(9))
'''

'''
def check_unique(items):
    seen = []
    for item in items:
        if item not in seen:
            duplicate_checker = item
            seen.append(duplicate_checker)
        else:
            return False
    return True
print(check_unique([1, 2, 3, 5]))
'''

'''
def same_data_type(data):
    if not data:
        return True
    checker = type(data[0])
    for types in data:
        if type(types) != checker:
            return False
    return True
print(same_data_type([]))
'''

# =====================================================================
# LEVEL 3 - EXERCISE 4: is_valid_variable(name)
# =====================================================================
# Goal: Validate whether a string is a legal, assignable Python variable identifier.
#
# Rules of Python Identifiers & Variables:
# 1. Must start with a letter (a-z, A-Z) or an underscore (_). It CANNOT start with a digit.
# 2. Remaining characters can only be letters, digits, or underscores.
# 3. Cannot contain spaces, hyphens, or special punctuation (e.g. $, @, -, .).
# 4. Cannot be a reserved Python keyword (e.g. 'for', 'while', 'def', 'class', 'if', 'return', etc.).
#
# Architectural Blueprint:
# - Contract: name (str) -> bool
# - Guard Clauses:
#   * If input is not a non-empty string, immediately reject (False).
# - Flow Architecture:
#   * Python strings have a built-in method .isidentifier() that verifies lexical syntax rules.
#   * Python's standard library module `keyword` contains `keyword.iskeyword(...)` to check if a word is reserved.
#   * A variable is valid if and only if it is a valid identifier AND NOT a reserved keyword.
#   *(You can also build the character-by-character validation loop yourself if you prefer manual parsing!)*
#
# ADVERSARIAL TEST MATRIX:
# 1. Standard Cases:
#    is_valid_variable('user_name')   -> True
#    is_valid_variable('_counter')    -> True
#    is_valid_variable('total_sum_1') -> True
# 2. Boundary Cases:
#    is_valid_variable('')            -> False (empty string)
#    is_valid_variable('_')           -> True  (single underscore)
#    is_valid_variable('x')           -> True  (single character)
# 3. Trap Cases:
#    is_valid_variable('1st_number')  -> False (cannot start with a number)
#    is_valid_variable('first-name')  -> False (hyphen is invalid operator)
#    is_valid_variable('first name')  -> False (space not allowed)
#    is_valid_variable('for')         -> False (reserved keyword)
#    is_valid_variable('def')         -> False (reserved keyword)
#
# WRITE YOUR BASELINE SOLUTION BELOW:

'''
import keyword
def is_valid_variable(name):
    if keyword.iskeyword(name):
        return False
    if name.isidentifier():
        return True
    return False
print(is_valid_variable('total_sum_1'))
'''

# =====================================================================
# LEVEL 3 - EXERCISE 5: Countries Data Analysis (Functions & Data Structures)
# =====================================================================
# Goal: Build real-world data processing functions on a dataset of 250 countries.
#
# Import the dataset cleanly (no need to paste 2,600 lines!):
# from countries_data import countries_data
#
# Each country is a dictionary structured like:
# {
#     "name": "Afghanistan",
#     "capital": "Kabul",
#     "languages": ["Pashto", "Uzbek", "Turkmen"],
#     "population": 27657145
# }
#
# ---------------------------------------------------------------------
# PART A: most_spoken_languages(data, top_n=10)
# ---------------------------------------------------------------------
# Contract: data (list of dicts), top_n (int, default 10) -> list
# Flow Architecture:
# 1. Guard against empty data (return []).
# 2. Tally: Loop through every country, and for every language in country['languages'],
#    count its total frequency across the world (using a dict).
# 3. Sort: Order the tallies in descending order by count.
# 4. Slice: Return the top `top_n` results.
#
# ADVERSARIAL TEST MATRIX (Part A):
# - Standard Case: most_spoken_languages(countries_data, 10) -> Top 10 languages
# - Boundary Case: most_spoken_languages(countries_data, 1)  -> Top 1 language
# - Trap Case:     most_spoken_languages([], 5)              -> [] (empty dataset)
#
# ---------------------------------------------------------------------
# PART B: most_populated_countries(data, top_n=10)
# ---------------------------------------------------------------------
# Contract: data (list of dicts), top_n (int, default 10) -> list
# Flow Architecture:
# 1. Guard against empty data (return []).
# 2. Sort countries directly by their 'population' key in descending order.
# 3. Slice the top `top_n` countries and return clean summary records
#    (e.g. list of dicts with {'country': name, 'population': pop} or tuples).
#
# ADVERSARIAL TEST MATRIX (Part B):
# - Standard Case: most_populated_countries(countries_data, 10) -> Top 10 populated countries
# - Boundary Case: most_populated_countries(countries_data, 3)  -> Top 3 populated countries
# - Trap Case:     most_populated_countries([], 5)              -> [] (empty dataset)
#
# WRITE YOUR BASELINE SOLUTIONS BELOW:
'''
# PART A
from collections import Counter
from countries_data import countries_data

def most_spoken_languages(data, top_n=10):
    language_tally = {}
    counter = 1
    for language_data in data:
        lang = language_data['languages']
        for language in lang:
            if language in language_tally:
                counter += 1
            else:
                counter == 1
            d = {language: counter}
            language_tally.update(d)
    language_list = dict(sorted(language_tally.items(), key=lambda item: item[1], reverse=True))
    language_top10 = dict(Counter(language_list).most_common(top_n))
    return language_top10
print(most_spoken_languages([], 1))
'''
        '''
        from countries_data import countries_data

        def most_populated_countries(data, top_n=10):
            population_list = {}
            if not data:
                return data
            for population_data in data:
                population = population_data['population']
                country = population_data['name']
                country_and_population = {population, country}
                population_list.update(country_and_population)
            return population_list
        print(most_populated_countries(countries_data,10))
        '''