# Day 13: List Comprehension & Lambda Functions - Alternative Solutions (Pass 2)

# ==============================================================================
# Exercise 1: Filter Negative and Zero (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Alternative A (Functional Filtering with filter + lambda):
#      Filter out positive numbers using Python's built-in `filter()` and a `lambda`
#      predicate instead of a list comprehension.
#    - Alternative B (Generator Expression for Streaming):
#      Construct a lazy generator `(x for x in numbers if x <= 0)` to conserve memory
#      when streaming potentially infinite or large sequences.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - List Comprehension vs `filter(lambda)`:
#      List comprehensions run in optimized C-level loops and avoid Python function-call
#      overhead, whereas `lambda` incurs a frame creation overhead on every iteration.
#    - Predicate Precision: Notice the distinction between `x <= 0` vs `not x > 0` vs bitwise checks.
# ==============================================================================

# Write your Pass 2 solution below:
# Target Output: [-4, -3, -2, -1, 0]
'''
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = list(filter(lambda x: x <= 0, numbers))
print(filtered)
'''


# ==============================================================================
# Exercise 2: Flatten Nested Lists (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Alternative A (Recursive Deep Flattening):
#      Build a recursive function `deep_flatten(element)` capable of handling arbitrary
#      nesting depths (e.g. 5+ levels deep), where a hardcoded comprehension would fail.
#    - Alternative B (Itertools Pipeline):
#      Use `itertools.chain.from_iterable()` to flatten known levels cleanly.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Static Depth vs Dynamic Depth: Comprehensions require knowing the exact nesting
#      depth at compile/write time. Recursion handles dynamic, irregular trees.
#    - Memory & Recursion Limit: Python's recursion limit (`sys.getrecursionlimit()`)
#      guards stack depth; iterative approaches with a custom stack avoid recursion limits.
# ==============================================================================

# Write your Pass 2 solution below:
# Target Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
list_of_lists = [[[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]]]
def deep_flatten(element):
    flatten = []
    for item in element:
        if isinstance(item, list):
            flatten.extend(deep_flatten(item))
        else:
            flatten.append(item)
    return flatten
print(deep_flatten(list_of_lists))
'''


# ==============================================================================
# Exercise 3: Powers of Numbers Tuple List (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Alternative A (Dynamic Exponent Range with Tuple Concatenation):
#      Instead of hardcoding `(i, i**0, i**1, i**2, i**3, i**4, i**5)`, dynamically
#      compute powers using `(i,) + tuple(i**p for p in range(6))`.
#    - Alternative B (Mathematical Mapping via math.pow / map):
#      Explore `tuple(map(lambda p: i**p, range(6)))` or integer bit-shifts for base 2.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Code Duplication vs Dynamic Generation: Hardcoding powers is fast but brittle.
#      A dynamic range scales effortlessly if the requirement expands to 10 powers.
# ==============================================================================

# Write your Pass 2 solution below:
# Target Output: [(0, 1, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), (2, 1, 2, 4, 8, 16, 32), ..., (10, 1, 10, 100, 1000, 10000, 100000)]
'''
nested_dynamic_tuple = [(i,) + tuple(i**p for p in range(6)) for i in range(11)]
print(nested_dynamic_tuple)
'''


# ==============================================================================
# Exercise 4: Flatten Country/City Tuples to Formatted Lists (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Alternative A (Decoupled Pipeline with itertools.chain.from_iterable):
#      Instead of coupling flattening and transformation in a single nested comprehension,
#      decouple the pipeline into two distinct stages:
#        Stage 1: Flatten outer lists to a 1D stream of (country, city) tuples using
#                 `itertools.chain.from_iterable(countries)`.
#        Stage 2: Map each tuple to `[country.upper(), country[:3].upper(), city.upper()]`.
#    - Alternative B (Functional Transformation via map and helper function):
#      Implement the formatting using `list(map(format_country, flat_stream))` or a pure
#      lambda to compare readability against list comprehensions.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Monolithic vs Decoupled Pipelines:
#      A single comprehension `[[...] for sublist in countries for country, city in sublist]`
#      is concise, but decoupling allows re-using the flattener for Exercises 5 and 6!
#    - String Slicing Allocation:
#      `country[:3]` allocates a new string slice in memory. Contrast this with index lookups.
#
# 3. Additional Challenges & Edge Cases:
#    - Short Country Names: What if a country name has fewer than 3 characters (e.g. 'UK', 'US')?
#      Test if `country[:3]` handles short strings without index out-of-range errors, and
#      consider how to pad or preserve shorter names.
#    - Multi-City Sublists: What if an outer list contains multiple city tuples for the same
#      country: `[[('Finland', 'Helsinki'), ('Finland', 'Espoo')], [('Norway', 'Oslo')]]`?
#      Verify that your alternative solution flattens and formats all items seamlessly.
# ==============================================================================

# Write your Pass 2 solution below:
# Target Output: [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
'''
# Alternative A:
import itertools
countries_cities = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat = itertools.chain.from_iterable(countries_cities)
country_ = [[country.upper(), country[:3].upper(), city.upper()] for country, city in list(flat)]
print(country_)
'''
# Alternative B:
import itertools
countries_cities = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def format_country(pair):
    country, city = pair
    return [country.upper(), country[:3].upper(), city.upper()]

flat_stream = itertools.chain.from_iterable(countries_cities)

result = list(map(format_country, flat_stream))
print(result)

# ==============================================================================
# Exercise 5: List to List of Dictionaries (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Alternative A (Dynamic Key-Value Pairing via dict(zip(...))):
#      Instead of hardcoding dictionary literals `{'country': ..., 'city': ...}`, define
#      a reusable schema `keys = ('country', 'city')` and construct dictionaries dynamically
#      via `dict(zip(keys, (country.upper(), city.upper())))`.
#    - Alternative B (Functional Dict Construction via map and dict constructor):
#      Build the list of dictionaries using `list(map(lambda pair: dict(country=pair[0].upper(), city=pair[1].upper()), ...))`
#      or by passing key-value pairs into `dict([...])`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Dict Literal `{k: v}` vs `dict(zip(...))` vs `dict(k=v)`:
#      * `{}` uses the specialized CPython opcode `BUILD_MAP` (fastest execution).
#      * `dict(zip(...))` incurs function-call overhead and tuple allocation, but provides
#        effortless scalability when schemas expand from 2 fields to 10+ fields.
#    - Data Structure Trade-offs: Why APIs and databases prefer list-of-dicts over list-of-tuples
#      (named access vs positional indexing).
#
# 3. Additional Challenges & Edge Cases:
#    - Dynamic Schema Expansion: Inject the 3-letter country code from Exercise 4 as a third key:
#      `{'country': 'FINLAND', 'code': 'FIN', 'city': 'HELSINKI'}` using `zip()`.
#    - Irregular Tuples: Safely handle tuples with missing city data (e.g. `('Iceland',)` or `('Monaco', None)`)
#      without throwing unpacking errors (`ValueError: not enough values to unpack`).
# ==============================================================================

# Write your Pass 2 solution below:
# Target Output: [{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]





# ==============================================================================
# Exercise 6: List of Lists to Concatenated Strings (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Alternative A (Pure Functional Pipeline with map and ' '.join):
#      Flatten the stream with `itertools.chain.from_iterable` and feed it directly
#      into `list(map(' '.join, flat_names))`—achieving zero manual variable naming and zero indexing.
#    - Alternative B (Structural Unpacking with Formatted f-strings):
#      Unpack directly in the loop or comprehension and format with an f-string:
#      `[f"{first} {last}" for [(first, last)] in names]`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - `str.join(tuple)` vs f-string `f"{first} {last}"` vs Chained `+`:
#      * `str.join(iterable)` calculates the exact memory buffer required once and fills it in O(N).
#      * Chained `first + ' ' + last` allocates multiple intermediate string objects.
#      * `str.join` works on tuples of ANY length; f-strings require knowing the exact number of variables.
#
# 3. Additional Challenges & Edge Cases:
#    - Arbitrary Name Component Lengths:
#      Support names with 1 part (`('Madonna',)`), 2 parts (`('Bill', 'Gates')`), or 4+ parts
#      (`('Martin', 'Luther', 'King', 'Jr.')`) without crashing or dropping components.
#    - Whitespace Sanitization:
#      Handle dirty input strings containing irregular padding or extra spaces:
#      `[[('  David  ', '  Smith ')]]` -> normalize to `'David Smith'`.
# ==============================================================================

# Write your Pass 2 solution below:
# Target Output: ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']



