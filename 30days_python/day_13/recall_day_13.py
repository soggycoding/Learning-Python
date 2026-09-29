# Day 13: List Comprehension & Lambda Functions - Pure Recall Challenges (Pass 3)

# ==============================================================================
# BATCHED RECALL CHUNK 1 (Exercises 1, 2, and 3)
# ==============================================================================
# Instructions:
#   Do NOT look back at `exercise_day_13.py` or `alternative_day13_solution.py`.
#   Write your solutions from pure mental recall below.
#
# Recall Prompt 1: Filter Negative & Zero
#   Given `numbers = [-4, -3, -2, -1, 0, 2, 4, 6]`, filter out all positive numbers
#   so only negative numbers and zero remain using a list comprehension.
#
# Recall Prompt 2: Flatten 3D List to 1D
#   Given `list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]`,
#   flatten it into `[1, 2, 3, 4, 5, 6, 7, 8, 9]` using list comprehension.
#
# Recall Prompt 3: Powers Tuple List
#   Generate the 11 tuples for i = 0 to 10 where each tuple has 7 items:
#   (i, i**0, i**1, i**2, i**3, i**4, i**5) using list comprehension.
# ==============================================================================
'''
# Write your Recall solutions below:
numbers = [-4, -3, -2, -1, 0, 2, 4 ,6]
filtered = [c for c in numbers if c <= 0]
print(filtered)
'''

'''
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [nums for sublist in list_of_lists for rows in sublist for nums in rows]

for sublist in list_of_lists:
    for rows in sublist:
        for nums in rows:
            flatten.append(nums)

print(flatten)
'''
'''
i = 0
powers_tuple = [(i,) + tuple(i**x for x in range(6)) for i in range(11)]
print(powers_tuple)
'''

# ==============================================================================
# BATCHED RECALL CHUNK 2 (Exercises 4, 5, and 6)
# ==============================================================================
# Instructions:
#   Do NOT look back at `exercise_day_13.py` or `alternative_day13_solution.py`.
#   Write your implementations strictly from memory below.
#
# Recall Prompt 4: Country-City Structured List
#   Input:
#     countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#   Expected Output:
#     [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
#   Constraints:
#     Each inner list must contain: [UPPERCASED_COUNTRY, 3_LETTER_CODE, UPPERCASED_CITY].
#     Must return a list of lists.
#
# Recall Prompt 5: Country-City Dictionary Records
#   Input:
#     countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#   Expected Output:
#     [{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]
#   Constraints:
#     Must return a list of dicts with exact keys 'country' and 'city' (both values uppercased).
#
# Recall Prompt 6: Full Name String Formatter
#   Input:
#     names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#   Expected Output:
#     ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
#   Constraints:
#     Must return a 1D list of strings with first and last names separated by a single space.
# ==============================================================================

# Write your Batch 2 Recall solutions below:
'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
listed_list = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]
print(listed_list)
'''
'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_dict = [{"country" : country.upper(), "city" : city.upper()} for sublist in countries for country, city in sublist]
print(country_dict)
'''
'''
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
flat_list = [f"{first} {last}" for sublist in names for first, last in sublist]
print(flat_list)
'''
