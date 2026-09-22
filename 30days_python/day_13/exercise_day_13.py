# Day 13: List Comprehension & Lambda Functions

# ==============================================================================
# Overview of Day 13 Exercises
# ==============================================================================
# Exercise 1: Filter only negative and zero in the list using list comprehension
'''
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [c for c in numbers if c <= 0]
print(filtered)
'''
# Exercise 2: Flatten the following list of lists of lists to a one-dimensional list:
'''
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#   output -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
flatten = [num for sublist in list_of_lists for row in sublist for num in row]
print(flatten)
'''

# ==============================================================================
# Exercise 3: Powers of Numbers Tuple List
# ==============================================================================
# Challenge:
#   Using list comprehension, create the following list of tuples from i = 0 to 10:
#   [(0, 1, 0, 0, 0, 0, 0),
#    (1, 1, 1, 1, 1, 1, 1),
#    (2, 1, 2, 4, 8, 16, 32),
#    (3, 1, 3, 9, 27, 81, 243),
#    (4, 1, 4, 16, 64, 256, 1024),
#    (5, 1, 5, 25, 125, 625, 3125),
#    (6, 1, 6, 36, 216, 1296, 7776),
#    (7, 1, 7, 49, 343, 2401, 16807),
#    (8, 1, 8, 64, 512, 4096, 32768),
#    (9, 1, 9, 81, 729, 6561, 59049),
#    (10, 1, 10, 100, 1000, 10000, 100000)]
#
# Hint / Mathematical Pattern for each tuple:
#   Examine the columns for index `i`:
#   Column 0: i
#   Column 1: i**0 (which is 1)
#   Column 2: i**1 (which is i)
#   Column 3: i**2
#   Column 4: i**3
#   Column 5: i**4
#   Column 6: i**5
#
# Adversarial Test Cases:
#   1. Standard Case: Returns a list of 11 tuples (for 0 through 10 inclusive).
#   2. Boundary Case: First tuple is (0, 1, 0, 0, 0, 0, 0); Last tuple is (10, 1, 10, 100, 1000, 10000, 100000).
#   3. Trap Case: Ensure range includes 10! (i.e. `range(11)`).
# ==============================================================================

# Write your Exercise 3 solution below:

#
# Exercise 4: Flatten the following list to a new list:
#   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#   output -> [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
#
# Exercise 5: Change the following list to a list of dictionaries:
#   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#   output -> [{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]
#
# Exercise 6: Change the following list of lists to a list of concatenated strings:
#   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#   output -> ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
#
# Exercise 7: Write a lambda function which can solve a slope or y-intercept of linear functions.
# ==============================================================================

# ==============================================================================
# Exercise 1: Filter Negative and Zero
# ==============================================================================
# Challenge:
#   Given the list `numbers = [-4, -3, -2, -1, 0, 2, 4, 6]`, filter out all
#   positive numbers so that only negative numbers and zero remain.
#   You MUST use a list comprehension.
#
# Adversarial Test Matrix:
#   1. Standard Case: numbers = [-4, -3, -2, -1, 0, 2, 4, 6] -> [-4, -3, -2, -1, 0]
#   2. Boundary Case: numbers = [] -> []
#   3. Trap Case: numbers = [0, 1, -1] -> [0, -1] (ensure 0 is explicitly included!)
# ==============================================================================

# Write your Exercise 1 solution below:

