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

countries_cities = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_country = []
country_list = [rows for country_name in countries_cities for rows in country_name]
for _ in country_list:
    country, city = _
    country_name = country.upper()
    country_3rd_letter = country_name[:3]
    city_name = city.upper()
    country_city = [country_name, country_3rd_letter, city_name]
    list_of_country.append(country_city)
print(list_of_country)
'''
countries = country_list[::2]
city_names = 
print(countries)
print(city_names)
'''
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

