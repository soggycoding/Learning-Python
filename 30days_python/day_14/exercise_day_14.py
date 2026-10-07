# Day 14: Higher Order Functions, Closures & Decorators Exercises

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




# ==============================================================================
# LEVEL 2 - EXERCISE 4: Filter Countries Containing 'land'
# ==============================================================================
# Challenge:
#   Use `filter()` to filter out countries containing `'land'` from `countries`.
#   (Only countries with 'land' in their name should remain).
#
# Adversarial Test Matrix:
#   1. Standard Case: `['Finland', 'Iceland']`
#   2. Boundary Case: If no country contains 'land', return `[]`.
#   3. Trap Case: Case sensitivity check — handles substrings properly.
# ==============================================================================

# Write your solution below:




# ==============================================================================
# LEVEL 2 - EXERCISE 5: Filter Countries with Exactly Six Characters
# ==============================================================================
# Challenge:
#   Use `filter()` to filter out countries having exactly six characters.
#
# Adversarial Test Matrix:
#   1. Standard Case: `['Sweden', 'Norway']`
#   2. Boundary Case: List with no 6-letter countries returns `[]`.
#   3. Trap Case: Exact equality `len(c) == 6`, not `>= 6`.
# ==============================================================================

# Write your solution below:




# ==============================================================================
# LEVEL 2 - EXERCISE 6: Filter Countries with Six or More Letters
# ==============================================================================
# Challenge:
#   Use `filter()` to filter out countries containing six letters and more.
#
# Adversarial Test Matrix:
#   1. Standard Case: `['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']`
#   2. Boundary Case: Short names like `['Chad', 'Fiji', 'Peru']` -> all filtered out -> `[]`.
#   3. Trap Case: Greater-than-or-equal `len(c) >= 6`.
# ==============================================================================

# Write your solution below:




# ==============================================================================
# LEVEL 2 - EXERCISE 7: Filter Countries Starting with 'E'
# ==============================================================================
# Challenge:
#   Use `filter()` to filter out countries starting with the letter `'E'`.
#
# Adversarial Test Matrix:
#   1. Standard Case: `['Estonia']`
#   2. Boundary Case: List without any 'E' countries returns `[]`.
#   3. Trap Case: Handles casing (e.g. `.startswith('E')` or case-insensitive check).
# ==============================================================================

# Write your solution below:




# ==============================================================================
# LEVEL 2 - EXERCISE 8: Chain Two or More List Iterators
# ==============================================================================
# Challenge:
#   Chain two or more higher-order operations together in a pipeline
#   (e.g., filter numbers, map transformations, then reduce to a final result).
#
# Adversarial Test Matrix:
#   1. Standard Case: Clear functional pipeline (e.g. filter evens -> square -> sum).
#   2. Boundary Case: Pipeline functions cleanly when intermediary produces an empty sequence.
#   3. Trap Case: Avoid nested parentheses confusion; ensure lazy consumption flows properly.
# ==============================================================================

# Write your solution below:




# ==============================================================================
# LEVEL 2 - EXERCISE 9: get_string_lists Function
# ==============================================================================
# Challenge:
#   Declare a function called `get_string_lists` which takes a list as a
#   parameter and returns a list containing only string items using `filter()`.
#
# Function signature:
#   def get_string_lists(lst):
#
# Adversarial Test Matrix:
#   1. Standard Case: `[1, 'apple', 3.14, 'banana', True, 'cherry']` -> `['apple', 'banana', 'cherry']`
#   2. Boundary Case: List of numbers only `[1, 2, 3]` -> `[]`; empty list `[]` -> `[]`
#   3. Trap Case: Ensure boolean `True`/`False` are not treated as strings; use `isinstance(x, str)`.
# ==============================================================================

# Write your solution below:




# ==============================================================================
# LEVEL 2 - EXERCISE 10: Sum Numbers with reduce()
# ==============================================================================
# Challenge:
#   Use `reduce()` from `functools` to sum all the numbers in the `numbers` list.
#
# Adversarial Test Matrix:
#   1. Standard Case: `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` -> `55`
#   2. Boundary Case: Single element `[42]` -> `42`; empty list with initializer `0` -> `0`
#   3. Trap Case: Pass initializer `0` to prevent `TypeError` on empty lists.
# ==============================================================================

# Write your solution below:




# ==============================================================================
# LEVEL 2 - EXERCISE 11: Concatenate Countries into a Sentence with reduce()
# ==============================================================================
# Challenge:
#   Use `reduce()` to concatenate all countries in `countries` to produce this
#   exact sentence:
#   "Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries"
#
# Adversarial Test Matrix:
#   1. Standard Case: Matches target string with Oxford comma and conjunction: "..., Norway, and Iceland are north European countries".
#   2. Boundary Case: Handling trailing and special formatting accurately.
#   3. Trap Case: Ensure the sentence ending is exact without extra trailing commas.
# ==============================================================================

# Write your solution below:




# ==============================================================================
# LEVEL 2 - EXERCISE 12: categorize_countries
# ==============================================================================
# Challenge:
#   Declare a function called `categorize_countries` that takes a pattern (e.g.
#   'land', 'ia', 'island', 'stan') and returns a list of countries containing
#   that pattern from the full countries dataset.
#
# Function signature:
#   def categorize_countries(pattern):
#
# Adversarial Test Matrix:
#   1. Standard Case: `categorize_countries('land')` returns all countries ending with or containing 'land'.
#   2. Boundary Case: Pattern not found returns `[]`.
#   3. Trap Case: Case-insensitive search (`pattern.lower() in country.lower()`).
# ==============================================================================

# Write your solution below:




# ==============================================================================
# LEVEL 2 - EXERCISE 13: countries_by_starting_letter
# ==============================================================================
# Challenge:
#   Create a function returning a dictionary where keys stand for starting letters
#   of countries and values are the number of country names starting with that letter.
#
# Function signature:
#   def countries_by_starting_letter():
#
# Adversarial Test Matrix:
#   1. Standard Case: Returns dict `{ 'A': count, 'B': count, ... }`.
#   2. Boundary Case: Letters with 0 countries should not have invalid counts.
#   3. Trap Case: Ensure uppercase standardization of starting letters.
# ==============================================================================

# Write your solution below:




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

# Write your solution below:




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

