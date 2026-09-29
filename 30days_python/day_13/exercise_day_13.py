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

# [num(final action)
#  for sublist in list_of_lists(copy loop 1 directly),
#  for row in sublist(copy loop 2 directly),
#  for num in row(copy loop 3 directly)]
'''

# Exercise 3: Powers of Numbers Tuple List
'''
result = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)
'''

# ==============================================================================
# Exercise 4: Flatten Country/City Tuples to Formatted Lists
# ==============================================================================
# Challenge:
#   Given the list:
#   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#   Flatten and transform it into the following list of lists using list comprehension:
#   [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
#
# Hint / Architecture:
#   - Each item in `countries` is a list containing a single tuple with (country, city).
#   - You need to unpack/extract the country name and city name.
#   - For each country/city pair, build a 3-element list:
#       [country in uppercase, first 3 letters of country in uppercase, city in uppercase]
#
# Adversarial Test Matrix:
#   1. Standard Case: countries as defined above -> [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
#   2. Boundary Case: empty list `[]` -> `[]`
#   3. Trap Case: Ensure each transformed item is a list `[...]`, not a tuple!
# ==============================================================================

# Write your Exercise 4 solution below:
'''
countries_cities = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_list = [rows for country_name in countries_cities for rows in country_name]
list_of_country = [[country.upper(), country[:3].upper(), city.upper() ]for country, city in country_list]
print(list_of_country)
'''
#   output -> [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
#
# Exercise 5: Change the following list to a list of dictionaries:
#   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#   output -> [{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]
'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_list = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print(country_list)
'''
# Exercise 6: Change the following list of lists to a list of concatenated strings:
#   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#   output -> ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
'''
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
outed_names = [' '.join(name_tuple) for sublist in names for name_tuple in sublist]
print(outed_names)
'''
# Exercise 7: Linear Function Slope Lambda — verified 2026-09-29
'''
calc_slope = lambda x1, y1, x2, y2 : (y2 - y1) / (x2 - x1)
print(calc_slope(2, 3, 6, 11))
'''

