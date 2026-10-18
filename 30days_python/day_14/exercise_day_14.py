# Day 14: Higher Order Functions, Closures & Decorators Exercises

from collections import Counter
import collections
import enum
import string
from functools import reduce

# ==============================================================================
# Starter Datasets Provided for Day 14
# ==============================================================================
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Exercise 1: Explain map, filter, and reduce — verified 2026-10-04
'''
- map(), maps the list and without the need of indexing. To convert without the need of manually doing it each index, requires 1 helper function and returns lazy iterator
- filter(), filters out the data that is correct based on the instructions/directions given, requires 1 helper function and also returns a lazy iterator but filtered to only what meets the requiremenets
- reduce(), to fold a sequence of items down into a single final scalar value, takes 1 helper function. Must be import via functools, always supply initial seed value, running on empty list crashes with TypeError
'''

# Exercise 2: Explain HOF, Closure, and Decorator — verified 2026-10-04
'''
Higher Order Function - function that accepts or returns functions
Closure - Function inside a function, or a bundled function with captured outer variables. The three criterea. Must be a nested function, must have a reference variable, and the outer function must return the inner function object
Decorator - HOF + Closure that intercepts and extends a target function, it applies a design pattern combining the two without modifying the original functions source code
@functools.wraps helps us wrap a function inside a decorator, it preserves the original function's metadata
'''

# Exercise 3: Define Callback Functions for map, filter, and reduce — verified 2026-10-04
'''
def to_pounds(kg):
    return kg * 2.205
kilogram = [55, 78, 96]
result = list(map(to_pounds, kilogram))
print(result)

def is_string(value):
    return isinstance(value, str)

random_things = [1, '23', 3, 'hello', 'bye', 6]
string_in_list = list(filter(is_string, random_things))
print(string_in_list)

def accumulate_step(running_value, current_value):
    return running_value + current_value

factors = [1,2,3,4,5,6,7,8,9,10]

final_product = reduce(accumulate_step, factors, 0)
print(final_product)
'''

# Exercise 4: Print Countries using for loop — verified 2026-10-05
'''
for country in countries:
    print(country)
'''


# Exercise 5: Print Names using for loop — verified 2026-10-05
'''
for name in names:
    print(name)
'''


# Exercise 6: Print Numbers using for loop — verified 2026-10-05
'''
for nums in numbers:
    print(nums)
'''


# LEVEL 2 - EXERCISE 1: Uppercase Countries with map() — verified 2026-10-07
'''
def uppCountries(val):
    return val.upper()
country_upper = list(map(uppCountries, countries))
print(country_upper)
'''


# LEVEL 2 - EXERCISE 2: Square Numbers with map() — verified 2026-10-07
'''
def squarenum(val):
    return val**2
squarednum = list(map(squarenum, numbers))
print(squarednum)
'''


# LEVEL 2 - EXERCISE 3: Uppercase Names with map() — verified 2026-10-07
'''
def uppname(val):
    return val.upper()
uppernames = list(map(uppname, names))
print(uppernames)
'''




# LEVEL 2 - EXERCISE 4: Filter Countries Containing 'land' — verified 2026-10-08
'''
def country(val):
    return "land" in val.lower()
land_country = list(filter(country, countries))
print(land_country)
'''


# LEVEL 2 - EXERCISE 5: Filter Countries with Exactly Six Characters — verified 2026-10-08
'''
def counter(val):
    return len(val) == 6
country_w_six = list(filter(counter, countries))
print(country_w_six)
'''


# LEVEL 2 - EXERCISE 6: Filter Countries with Six or More Letters — verified 2026-10-08
'''
def counter(val):
    return len(val) >= 6
country_w_more_six = list(filter(counter, countries))
print(country_w_more_six)
'''

# ==============================================================================
# LEVEL 2 - EXERCISE 7: Filter Countries Starting with 'E' — verified 2026-10-09
'''
country = list(filter(lambda x: x.startswith('E'), countries))
print(country)
'''


# LEVEL 2 - EXERCISE 8: Chain Two or More List Iterators — verified 2026-10-09
'''
filtered = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)), 0)
print(filtered)
'''


# LEVEL 2 - EXERCISE 9: get_string_lists Function — verified 2026-10-09
'''
mixed_list = [1, 'apple', 3.14, 'banana', True, 'cherry']
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x,str), lst))
print(get_string_lists(mixed_list))
'''




# LEVEL 2 - EXERCISE 10: Sum Numbers with reduce() — verified 2026-10-12
'''
sum_of_nums = reduce(lambda x, y : x + y, numbers, 0)
print(sum_of_nums)
'''



# LEVEL 2 - EXERCISE 11: Concatenate Countries into a Sentence with reduce() — verified 2026-10-13
'''
last_index = len(countries) - 1
index_countries = list(enumerate(countries))
country_concat = reduce(lambda x, y: (f'{x}, and {y[1]} are north European countries' if y[0] == last_index else f"{x}, {y[1]}"), 
index_countries[1:],
index_countries[0][1])
print(country_concat)
'''

# LEVEL 2 - EXERCISE 12: categorize_countries — verified 2026-10-13
'''
from countries_data import countries_data
def categorize_countries(pattern):
    filtered_country = []
    for country in countries_data:
        country_name = country["name"]
        if pattern.lower() in country_name.lower() :
            filtered_country.append(country_name)
    return filtered_country

print(categorize_countries("stan"))
'''




# LEVEL 2 - EXERCISE 13: countries_by_starting_letter — verified 2026-10-16
'''
from countries_data import countries_data
def countries_by_starting_letter():
    result = {}
    for country in countries_data:
        country_name = country["name"][0].upper()
        if country_name in result:
            result[country_name] += 1
        else:
            result[country_name] = 1
    return result
print(countries_by_starting_letter())
'''

# ==============================================================================
# LEVEL 2 - EXERCISE 14: get_first_ten_countries
# ==============================================================================
# Challenge:
#   Declare a `get_first_ten_countries` function that returns a list of the
#   first ten countries from the countries dataset.
#
# Function signature:
#   def get_first_ten_countries():
#
# Adversarial Test Matrix:
#   1. Standard Case: Returns exactly 10 countries.
#   2. Boundary Case: If dataset has fewer than 10, return all available without IndexError.
#   3. Trap Case: Preserves original list ordering.
# ==============================================================================

# Write your solution below:
from countries_data import countries_data
'''
def get_first_ten_countries():
    return [country["name"] for country in countries_data[:10]]
print(get_first_ten_countries())
'''


# ==============================================================================
# LEVEL 2 - EXERCISE 15: get_last_ten_countries
# ==============================================================================
# Challenge:
#   Declare a `get_last_ten_countries` function that returns the last ten
#   countries from the countries dataset.
#
# Function signature:
#   def get_last_ten_countries():
#
# Adversarial Test Matrix:
#   1. Standard Case: Returns exactly the last 10 countries.
#   2. Boundary Case: If dataset has fewer than 10, return all available.
#   3. Trap Case: Slice indexing `[-10:]` does not invert order.
# ==============================================================================
'''
# Write your solution below:
def get_last_ten_countries():
    return [country["name"] for country in countries_data[-10:]]
print(get_last_ten_countries())
'''


# ==============================================================================
# LEVEL 3 - EXERCISE 1: Sorting and Data Analysis with countries_data
# ==============================================================================
# Challenge:
#   Use `countries_data.py` to perform the following higher-order operations:
#   1. Sort countries by name, by capital, and by population.
#   2. Sort out the ten most spoken languages by location.
#   3. Sort out the ten most populated countries.
#
# Adversarial Test Matrix:
#   1. Standard Case: Uses `sorted()` with key lambdas; top 10 lists have length 10.
#   2. Boundary Case: Handles missing fields or empty values cleanly.
#   3. Trap Case: Descending sort (`reverse=True`) for top populated and spoken items.
# ==============================================================================

# Write your solution below:
'''
sorted_by_name = sorted(countries_data, key=lambda country: country["name"])
sorted_by_capital = sorted(countries_data, key=lambda country: country["capital"])
sorted_by_population = sorted(countries_data, key=lambda country: country["population"])
'''
def country_language():
    result = {}
    for country in countries_data:
        multi_language = country["languages"]
        for single_language in multi_language:
            if single_language in result:
                result[single_language] += 1
            else:
                result[single_language] = 1
    return result
most_spoken_language = sorted(country_language(), key=lambda item: item[1], reverse=True)
print(most_spoken_language)
