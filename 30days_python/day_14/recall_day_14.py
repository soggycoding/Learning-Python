# Day 14: Higher Order Functions, Closures & Decorators - Pure Recall Challenges (Pass 3)

# ==============================================================================
# Starter Datasets Provided for Day 14
# ==============================================================================
import heapq
from collections import Counter
import itertools
from operator import itemgetter
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ==============================================================================
# BATCHED RECALL: LEVEL 2 (Exercises 1, 2, and 3)
# ==============================================================================
# Instructions:
#   Do NOT look back at `exercise_day_14.py` or `alternative_day14_solution.py`.
#   Write your implementations strictly from memory below.
#
# Recall Prompt 1: Uppercase Country Names
#   Input:
#     countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
#   Expected Output:
#     ['ESTONIA', 'FINLAND', 'SWEDEN', 'DENMARK', 'NORWAY', 'ICELAND']
#   Constraints:
#     Must return a materialized list of uppercase string elements.
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above
#     2. Boundary Case: `[]` -> `[]`
#     3. Trap Case: `['iCeLaNd']` -> `['ICELAND']`; result is a `list`, not a lazy object.
#
# Recall Prompt 2: Square Numbers
#   Input:
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   Expected Output:
#     [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#   Constraints:
#     Must return a materialized list of squared numbers.
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above
#     2. Boundary Case: `[0]` -> `[0]`
#     3. Trap Case: `[-4, 2.5]` -> `[16, 6.25]`; result is a `list`.
#
# Recall Prompt 3: Uppercase Person Names
#   Input:
#     names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
#   Expected Output:
#     ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
#   Constraints:
#     Must return a materialized list of uppercase string elements.
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above
#     2. Boundary Case: `['sam']` -> `['SAM']`
#     3. Trap Case: `['ABRAHAM']` (already uppercase) -> `['ABRAHAM']`; result is a `list`.
# ==============================================================================

# Recall Prompt 1: Uppercase Country Names — verified 2026-10-08
'''
country_upper = list(map(str.upper, countries))
print(country_upper)
'''

# Recall Prompt 2: Square Numbers — verified 2026-10-08
'''
squared = list(map(lambda x: x**2, numbers))
print(squared)
'''

# Recall Prompt 3: Uppercase Person Names — verified 2026-10-08
'''
names_upper = list(map(str.upper, names))
print(names_upper)
'''


# ==============================================================================
# BATCHED RECALL: LEVEL 2 (Exercises 4, 5, and 6)
# ==============================================================================
# Instructions:
#   Do NOT look back at `exercise_day_14.py` or `alternative_day14_solution.py`.
#   Write your implementations strictly from memory below.
#
# Recall Prompt 4: Filter Countries Containing 'land'
#   Input:
#     countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
#   Expected Output:
#     ['Finland', 'Iceland']
#   Constraints:
#     Must return a materialized list containing only countries that contain the substring 'land'.
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above
#     2. Boundary Case: `['Chad', 'Peru']` -> `[]`
#     3. Trap Case: Case sensitivity — handles `'IreLaNd'` if normalized -> `['IreLaNd']`; result is a `list`.
#
# Recall Prompt 5: Filter Countries with Exactly Six Characters
#   Input:
#     countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
#   Expected Output:
#     ['Sweden', 'Norway']
#   Constraints:
#     Must return a materialized list of countries whose character length is exactly 6.
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above
#     2. Boundary Case: `['Chad', 'Fiji']` -> `[]`
#     3. Trap Case: Exact equality `len(c) == 6`, not `>= 6`.
#
# Recall Prompt 6: Filter Countries with Six or More Letters
#   Input:
#     countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
#   Expected Output:
#     ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
#   Constraints:
#     Must return a materialized list of countries whose character length is 6 or greater.
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above
#     2. Boundary Case: `['Chad', 'Fiji', 'Peru']` -> `[]`
#     3. Trap Case: Inequality check `len(c) >= 6`.
# ==============================================================================

# Recall Prompt 4: Filter Countries Containing 'land' — verified 2026-10-09
'''
country = [x for x in countries if "land" in x.lower()]
print(country)
'''

# Recall Prompt 5: Filter Countries with Exactly Six Characters — verified 2026-10-09
'''
country = [x for x in countries if len(x) == 6]
print(country)
'''

# Recall Prompt 6: Filter Countries with Six or More Letters — verified 2026-10-09
'''
country = list(filter(lambda x: len(x) >= 6, countries))
print(country)
'''


# ==============================================================================
# BATCHED RECALL: LEVEL 2 (Exercises 7, 8, and 9)
# ==============================================================================
# Instructions:
#   Do NOT look back at `exercise_day_14.py` or `alternative_day14_solution.py`.
#   Write your implementations strictly from memory below.
#
# Recall Prompt 7: Filter Countries Starting with 'E'
#   Input:
#     countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
#   Expected Output:
#     ['Estonia']
#   Constraints:
#     Extract country names that start with the letter 'E' (or 'e') into a list.
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above
#     2. Boundary Case: `[]` -> `[]`
#     3. Trap Case: Multi-case check `['estonia', 'Estonia', 'spain']` -> `['estonia', 'Estonia']`
#
# Recall Prompt 8: Chain Transformations and Sum
#   Input:
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   Expected Output:
#     220
#   Constraints:
#     Identify the even numbers, square them, and calculate the total sum of those squared values as a single integer.
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above
#     2. Boundary Case: `[]` -> `0`
#     3. Trap Case: Only odd numbers `[1, 3, 5]` -> `0`; negative even numbers `[-2, -4]` -> `20`
#
# Recall Prompt 9: get_string_lists Function
#   Input:
#     mixed_list = [1, 'apple', 3.14, 'banana', True, 'cherry']
#   Expected Output:
#     ['apple', 'banana', 'cherry']
#   Constraints:
#     Define a function `get_string_lists(lst)` that accepts a list of mixed data types and returns a list containing only the string items.
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above
#     2. Boundary Case: `[]` -> `[]`
#     3. Trap Case: No strings present `[1, 2.5, True, False, None]` -> `[]`; preserves empty string `['', 42]` -> `['']`
# ==============================================================================

# Recall Prompt 7: Filter Countries Starting with 'E' — verified 2026-10-11
'''
country = [x for x in countries if x.startswith(("E", 'e'))]
print(country)
'''

# Recall Prompt 8: Chain Transformations and Sum — verified 2026-10-11
'''
nums = sum(x ** 2 for x in numbers if x % 2 == 0)
print(nums)
'''

# Recall Prompt 9: get_string_lists Function — verified 2026-10-11
'''
mixed_list = [1, 'apple', 3.14, 'banana', True, 'cherry']
def get_string_lists(val):
    return [x for x in val if isinstance(x, str)]
print(get_string_lists(mixed_list))
'''


# ==============================================================================
# BATCHED RECALL: LEVEL 2 (Exercises 10, 11, and 12)
# ==============================================================================
# Instructions:
#   Do NOT look back at `exercise_day_14.py` or `alternative_day14_solution.py`.
#   Write your implementations strictly from memory below.
#
# Recall Prompt 10: Sum Numbers
#   Input:
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   Expected Output:
#     55
#   Constraints:
#     Compute and return the total sum of all numbers in the list.
#   Adversarial Test Matrix:
#     1. Standard Case: numbers -> 55
#     2. Boundary Case: [] -> 0
#     3. Trap Case: Negative numbers [-5, 5, -10, 10] -> 0
#
# Recall Prompt 11: Concatenate Countries into a Sentence
#   Input:
#     countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
#   Expected Output:
#     "Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries"
#   Constraints:
#     Join the country names with commas, prefix the final country with "and ", and append " are north European countries".
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above
#     2. Boundary Case: Single element ['Estonia'] -> proper formatting without trailing/broken punctuation
#     3. Trap Case: Exact punctuation check — Oxford comma before "and", no double commas or trailing spaces
#
# Recall Prompt 12: categorize_countries Function
#   Input:
#     countries_data (from countries_data import countries_data), pattern string
#   Expected Output:
#     List of country names (e.g. categorize_countries('land'))
#   Constraints:
#     Define a function `categorize_countries(pattern)` that returns a list of names of countries where the country's name contains the specified pattern substring (case-insensitively).
#   Adversarial Test Matrix:
#     1. Standard Case: 'land' -> 29 countries
#     2. Boundary Case: 'xyz_nonexistent' -> []
#     3. Trap Case: Casing variation 'ICE' -> ['Iceland']
# ==============================================================================

# Recall Prompt 10: Sum Numbers — verified 2026-10-16
'''
result = sum(numbers)
print(result)
'''

# Recall Prompt 11: Concatenate Countries into a Sentence — verified 2026-10-16
'''
country = reduce(lambda x, y: x + ', ' + y, countries[:-1])
print(country + f', and {countries[-1]} ' + "are north European countries")
'''

# Recall Prompt 12: categorize_countries Function — verified 2026-10-16
'''
from countries_data import countries_data
def categorize_countries(pattern):
    filtered = filter(lambda country: pattern.lower() in country["name"].lower(), countries_data)
    mapped = map(lambda county: county["name"], filtered)
    return list(mapped)

print(categorize_countries("FIN"))
'''

# ==============================================================================
# BATCHED RECALL: LEVEL 2 (Exercises 13, 14, and 15)
# ==============================================================================
# Instructions:
#   Do NOT look back at `exercise_day_14.py` or `alternative_day14_solution.py`.
#   Write your implementations strictly from memory below.
#   Each function takes a `data` parameter that defaults to `countries_data`,
#   so you can run the Boundary and Trap cases on small hand-made lists.
#
# Recall Prompt 13: countries_by_starting_letter Function
#   Input:
#     countries_data (from countries_data import countries_data), 250 country dicts
#   Expected Output:
#     A dict mapping each first letter to how many countries start with it, e.g.
#     {'A': 15, 'B': 21, 'C': 23, ..., 'S': 33, ..., 'Z': 2, 'Å': 1}
#   Constraints:
#     Define `countries_by_starting_letter(data=countries_data)`.
#     Count with ONE lookup per country: no `if key in result / else` branch.
#   Adversarial Test Matrix:
#     1. Standard Case: default data -> 'S' is 33, 'Q' is 1, and the values sum to 250
#     2. Boundary Case: `[]` -> `{}`
#     3. Trap Case: `[{'name': 'chad'}, {'name': 'Chile'}]` -> `{'C': 2}` (lowercase name still
#        lands in the uppercase bucket); no letter appears with a count of 0 (there is no 'X' key)
#
# Recall Prompt 14: get_first_ten_countries Function
#   Input:
#     countries_data (from countries_data import countries_data)
#   Expected Output:
#     ['Afghanistan', 'Åland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra',
#      'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda']
#   Constraints:
#     Define `get_first_ten_countries(data=countries_data)` that returns a list of NAMES
#     (strings, not dicts), in their original order.
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above, length exactly 10
#     2. Boundary Case: a 3-item list -> all 3 names, no IndexError
#     3. Trap Case: `data=(c for c in countries_data)` (a generator) -> same 10 names.
#        Plain slicing can't do this. Which tool can?
#
# Recall Prompt 15: get_last_ten_countries Function
#   Input:
#     countries_data (from countries_data import countries_data)
#   Expected Output:
#     ['Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela (Bolivarian Republic of)', 'Viet Nam',
#      'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']
#   Constraints:
#     Define `get_last_ten_countries(data=countries_data)` that returns a list of NAMES
#     in their original order ('Zimbabwe' LAST, not first).
#   Adversarial Test Matrix:
#     1. Standard Case: the expected output above, length exactly 10
#     2. Boundary Case: a 3-item list -> all 3 names, in order
#     3. Trap Case: `data=(c for c in countries_data)` (a generator) -> same 10 names,
#        and your code never holds more than 10 names at once
# ==============================================================================
from countries_data import countries_data
# Recall Prompt 13: countries_by_starting_letter Function — verified 2026-10-23
'''
def countries_by_starting_letter(data=countries_data):
    result = {}
    for country in data:
        first_letter = country["name"][0].upper()
        result[first_letter] = result.get(first_letter, 0) + 1
    return result
print(countries_by_starting_letter())
'''
'''
# Recall Prompt 14: get_first_ten_countries Function — verified 2026-10-23
def get_first_ten_countries(data=countries_data):
    return list(map(itemgetter("name"), itertools.islice(data, 10)))
print(get_first_ten_countries())
'''
'''
from collections import deque
# Recall Prompt 15: get_last_ten_countries Function — verified 2026-10-23
def get_last_ten_countries(data=countries_data):
    db = deque(data, maxlen=10)
    return list(map(itemgetter("name"), db))
print(get_last_ten_countries())
'''

# ==============================================================================
# BATCHED RECALL: LEVEL 3 (Exercises 1A, 1B, and 1C)
# ==============================================================================
# Instructions:
#   Do NOT look back at `exercise_day_14.py` or `alternative_day14_solution.py`.
#   Write your implementations strictly from memory below.
#
# Recall Prompt 16: Sort Countries by Name, Capital, and Population (Exercise 1A)
#   Input:
#     countries_data (from countries_data import countries_data)
#   Expected Output:
#     Three separate sorted collections:
#     - By name (ascending: A to Z)
#     - By capital (ascending: A to Z)
#     - By population (ordered by population count)
#   Constraints:
#     Use key extractor callables (e.g., `operator.itemgetter` or clean lambdas).
#     Pure operation: do NOT mutate the original `countries_data` list.
#   Adversarial Test Matrix:
#     1. Standard Case:
#        - Name sort starts with 'Afghanistan'
#        - Population sort is strictly ordered by numeric value
#     2. Boundary Case:
#        - Empty list `[]` sorts cleanly to `[]` without error
#     3. Trap Case:
#        - Immutability check: `countries_data` original ordering is untouched
#        - Tie-breaking: multi-key ordering works cleanly when primary keys match or are empty
#
# Recall Prompt 17: Ten Most Spoken Languages (Exercise 1B)
#   Input:
#     countries_data (from countries_data import countries_data)
#   Expected Output:
#     A list of 10 `(language, count)` tuples:
#     [('English', 91), ('French', 45), ('Arabic', 25), ('Spanish', 24), ('Portuguese', 9),
#      ('Russian', 9), ('Dutch', 8), ('German', 7), ('Chinese', 5), ('Serbian' or 'Swahili', 4)]
#   Constraints:
#     Define `most_spoken_languages(data=countries_data, n=10)`.
#     Flatten the nested `languages` lists using a clean generator/comprehension or `itertools.chain`
#     and leverage standard library counting tools (e.g., `Counter`).
#   Adversarial Test Matrix:
#     1. Standard Case: default dataset returns exactly 10 pairs with counts matching above
#     2. Boundary Case: `data=[]` -> `[]`; `n=0` -> `[]`
#     3. Trap Case: Countries with multiple languages (e.g., Switzerland with 4) must increment
#        each language count independently; `n > len(unique_languages)` returns all available without crash
#
# Recall Prompt 18: Ten Most Populated Countries (Exercise 1C)
#   Input:
#     countries_data (from countries_data import countries_data)
#   Expected Output:
#     The top 10 most populated countries (e.g. list of `(name, population)` tuples or dicts):
#     [('China', 1377422166), ('India', 1295210000), ('United States of America', 323947000), ...]
#   Constraints:
#     Define `most_populated_countries(data=countries_data, n=10)`.
#     Extract top N without unnecessary full-dataset reallocations (leverage `heapq.nlargest` or key extraction).
#   Adversarial Test Matrix:
#     1. Standard Case: default dataset -> 10 items, strictly descending from China to Japan
#     2. Boundary Case: `data=[]` -> `[]`; `n=3` on a 5-item list returns top 3
#     3. Trap Case: Ordering check — strictly descending order (highest population first);
#        `n > len(data)` returns all available records safely
# ==============================================================================
from countries_data import countries_data

# Recall Prompt 16: Sort Countries by Name, Capital, and Population — verified 2026-10-23
'''
sorted_by_name = sorted(countries_data, key=itemgetter("name"))
mapped_by_name = list(map(itemgetter("name"), sorted_by_name))
print(mapped_by_name)
'''
'''
sorted_by_capital = sorted(countries_data, key=itemgetter("capital"))
mapped_by_capital = list(map(itemgetter("name","capital"), sorted_by_capital))
print(mapped_by_capital)
'''
'''
sorted_by_population = sorted(countries_data, key=itemgetter("population"))
mapped_by_population = list(map(itemgetter("name", "population"), sorted_by_population))
print(mapped_by_population)
'''

# Recall Prompt 17: Ten Most Spoken Languages — verified 2026-10-23
'''
def most_spoken_language(data=countries_data, n=10):
    sorted_by_language = [languages for language in data for languages in language["languages"]]
    result = Counter(sorted_by_language)
    return result.most_common(n)
print(most_spoken_language())
'''

# Recall Prompt 18: Ten Most Populated Countries — verified 2026-10-23
'''
def most_populated_country(data=countries_data, n=10):
    sorted_by_population = heapq.nlargest(n, data, key=itemgetter("population"))
    mapped_by_population = list(map(itemgetter("name", "population"), sorted_by_population))
    return mapped_by_population
print(most_populated_country())
'''