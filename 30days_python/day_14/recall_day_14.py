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

# Write your Recall solutions below:



