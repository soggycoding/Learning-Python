# Day 14: Higher Order Functions, Closures & Decorators - Pure Recall Challenges (Pass 3)

# ==============================================================================
# Starter Datasets Provided for Day 14
# ==============================================================================
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