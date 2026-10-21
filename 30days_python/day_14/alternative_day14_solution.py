# Day 14: Higher Order Functions, Closures & Decorators - Alternative Solutions (Pass 2)

# ==============================================================================
# Starter Datasets Provided for Day 14
# ==============================================================================
from unittest import result
from collections import deque
import itertools
from operator import itemgetter
from collections import defaultdict
from collections import Counter
from operator import contains
from functools import reduce
import operator
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ==============================================================================
# Level 2 - Exercise 1: Uppercase Countries (Pass 2: Alternative Exploration) — verified 2026-10-07
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Transform each country name to uppercase using standard list comprehension
#      syntax `[... for x in ...]`.
#    - Option B (map() with no `def` helper):
#      Pass built-in `str.upper` directly into `map()` without defining a custom helper.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Function Call Overhead: In Python, calling a custom user-defined function in a
#      loop incurs bytecode frame overhead. List comprehensions and built-in methods
#      implemented in C skip that extra layer of Python function calls.
#    - Readability: In modern Python, list comprehensions are preferred over `map()`
#      for simple element-wise transformations.
# ==============================================================================

# Target Output: ['ESTONIA', 'FINLAND', 'SWEDEN', 'DENMARK', 'NORWAY', 'ICELAND']
'''
# Option A: List comprehension
country = [x.upper() for x in countries]
print(country)

# Option B: Method reference with map
upper_country = list(map(str.upper, countries))
print(upper_country)
'''


# ==============================================================================
# Level 2 - Exercise 2: Square Numbers (Pass 2: Alternative Exploration) — verified 2026-10-07
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Compute the square of each number using a list comprehension `[... for x in ...]`.
#    - Option B (Inline Lambda with map):
#      Instead of declaring a standalone `def` helper function that is only used once,
#      pass an anonymous inline `lambda` directly into `map()`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Single-use Functions: When a helper function is small (1 expression) and only
#      used in one place, declaring it with `def` pollutes the namespace. A `lambda`
#      keeps it localized, but list comprehensions are generally even cleaner and more
#      idiomatic in modern Python.
# ==============================================================================

# Target Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
# Option A: List comprehension
squared = [n**2 for n in numbers]
print(squared)

# Option B: Inline lambda with map
squared = list(map(lambda x: x**2, numbers))
print(squared)
'''


# ==============================================================================
# Level 2 - Exercise 3: Uppercase Names (Pass 2: Alternative Exploration) — verified 2026-10-07
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Transform each name to uppercase using a list comprehension.
#    - Option B (map() with no `def` helper):
#      Transform `names` using `map(str.upper, names)`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Consistency across String Iterables: Notice how cleanly the patterns from
#      Exercise 1 generalize to any string sequence.
# ==============================================================================

# Target Output: ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
'''
# Option A: List comprehension
upper_names = [x.upper() for x in names]
print(upper_names)

# Option B: Method reference with map
upper_names = list(map(str.upper, names))
print(upper_names)
'''


# ==============================================================================
# Level 2 - Exercise 4: Filter Countries Containing 'land' (Pass 2: Alternative Exploration) — verified 2026-10-08
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension with Filtering):
#      Filter items using a list comprehension: `[elem for elem in ... if <condition>]`.
#    - Option B (Inline Lambda with filter()):
#      Instead of defining a standalone `def` helper function, pass an anonymous inline lambda directly to `filter()`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Readability vs Functional style: List comprehensions are generally considered more Pythonic and concise than `filter()` with a lambda.
#    - Execution Overhead: `filter()` with a Python lambda invokes a function frame for every element, whereas list comprehensions execute optimized C-level loop bytecode.
# ==============================================================================

# Target Output: ['Finland', 'Iceland']
'''
# Option A: List comprehension
country_six = [country for country in countries if "land" in country]
print(country_six)

# Option B: Inline lambda with filter
country_six = list(filter(lambda x: "land" in x, countries))
print(country_six)
'''


# ==============================================================================
# Level 2 - Exercise 5: Filter Countries with Exactly Six Characters (Pass 2: Alternative Exploration) — verified 2026-10-08
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Filter elements by exact length using a list comprehension: `[elem for elem in ... if len(elem) == ...]`.
#    - Option B (Inline Lambda with filter()):
#      Use `filter()` paired with an inline lambda checking the length.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - In-place predicate logic: Avoid namespace pollution by omitting single-use named functions for simple length checks.
# ==============================================================================

# Target Output: ['Sweden', 'Norway']
'''
# Option A: List comprehension
country_w_six = [country for country in countries if len(country) == 6]
print(country_w_six)

# Option B: Inline lambda with filter
country_w_six = list(filter(lambda x: len(x) == 6, countries))
print(country_w_six)
'''


# ==============================================================================
# Level 2 - Exercise 6: Filter Countries with Six or More Letters (Pass 2: Alternative Exploration) — verified 2026-10-08
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Filter elements using `>=` length comparison inside a list comprehension.
#    - Option B (Inline Lambda with filter()):
#      Use `filter()` paired with an inline lambda with `>=`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Comparison operators in functional pipelines: Observe the syntactic parity between exact match (`==`) and inequality (`>=`) across both paradigms.
# ==============================================================================

# Target Output: ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
'''
# Option A: List comprehension
country_w_six_or_more = [country for country in countries if len(country) >= 6]
print(country_w_six_or_more)

# Option B: Inline lambda with filter
country_w_six_or_more = list(filter(lambda x: len(x) >= 6, countries))
print(country_w_six_or_more)
'''


# ==============================================================================
# Level 2 - Exercise 7: Filter Countries Starting with 'E' (Pass 2: Alternative Exploration) — verified 2026-10-10
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Filter elements starting with `'E'` using a list comprehension: `[elem for elem in ... if <condition>]`.
#    - Option B (Case-Insensitive Tuple Matching):
#      Pass a tuple of allowed prefixes to `.startswith(('E', 'e'))` within `filter()` or a comprehension.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - String Prefix Flexibility: `str.startswith()` accepts a tuple of candidates (e.g. `str.startswith(('A', 'B'))`), making multi-character/multi-casing checks fast and idiomatic without boolean concatenation.
# ==============================================================================

# Target Output: ['Estonia']
'''
# Option A
target_letter = 'E', 'e'
country = [x for x in countries if x.startswith(target_letter)]
print(country)

# Option B
country = list(filter(lambda x: x.startswith(("E" , 'e')), countries))
print(country)
'''

# ==============================================================================
# Level 2 - Exercise 8: Chain Two or More List Iterators (Pass 2: Alternative Exploration) — verified 2026-10-10
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Generator Expression with built-in sum()):
#      Replace the nested `reduce()` + `map()` + `filter()` pipeline with a single generator expression fed into built-in `sum()`:
#      `sum(transform(elem) for elem in ... if predicate(elem))`
#    - Option B (Comprehension + built-in sum()):
#      Compare the generator pipeline against a list comprehension fed into `sum()`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Functional vs Pythonic: In Python, `sum(f(x) for x in seq if cond(x))` is universally preferred over nested `reduce(lambda ..., map(..., filter(...)))` because it eliminates lambda dispatch overhead, avoids deep nesting parentheses, and runs via optimized C loops.
# ==============================================================================

# Target Output: 220
'''
# Option A:
nums = sum(x ** 2 for x in numbers if x % 2 == 0)
print(nums)

# Option B:
nums = sum([x ** 2 for x in numbers if x % 2 == 0])
print(nums)
'''
# ==============================================================================
# Level 2 - Exercise 9: get_string_lists Function (Pass 2: Alternative Exploration) — verified 2026-10-10
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension inside function):
#      Implement `get_string_lists(lst)` using a concise list comprehension: `[elem for elem in lst if isinstance(elem, str)]`.
#    - Option B (Generator Function with yield):
#      Define a generator function `def get_string_gen(lst):` that `yield`s string elements on demand, then materialize with `list()`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Memory footprint: A generator function streams items one-by-one with O(1) auxiliary space until consumed by the caller, which is ideal for massive collections.
# ==============================================================================

# Target Output: ['apple', 'banana', 'cherry']
'''
# Option A
mixed_list = [1, 'apple', 3.14, 'banana', True, 'cherry']
def get_string_lists(lst):
    return [x for x in lst if isinstance(x, str)]
print(get_string_lists(mixed_list))

# Option B
mixed_list = [1, 'apple', 3.14, 'banana', True, 'cherry']
def get_string_gen(lst):
    for x in lst:
        if isinstance(x, str):
            yield x
print(list(get_string_gen(mixed_list)))
'''

# ==============================================================================
# Level 2 - Exercise 10: Sum Numbers (Pass 2: Alternative Exploration) — verified 2026-10-13
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Pythonic Built-in):
#      Eliminate the functional reduce overhead by leveraging Python's specialized built-in aggregation tool designed specifically for arithmetic summation.
#    - Option B (Standard Library Operator with reduce):
#      Retain the functional fold pattern, but replace the custom lambda dispatch with an optimized C-level binary addition callable from the standard library `operator` module.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Lambda Overhead vs C-level Dispatch: In Python, evaluating a lambda function on each step incurs function call overhead and stack frame creation. Both built-in aggregators and `operator` primitives run directly in C loops, yielding massive speed improvements.
# ==============================================================================

# Target Output: 55
'''
# Option A:
result = sum(numbers)
print(result)

# Option B:
result = reduce(operator.add, numbers, 0)
print(result)
'''

# ==============================================================================
# Level 2 - Exercise 11: Concatenate Countries (Pass 2: Alternative Exploration) — verified 2026-10-13
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (String Join with Slicing & Formatting):
#      Bypass `reduce()` entirely by separating the sequence into all elements up to the last and the trailing element, using Python's optimized `str.join()` combined with an f-string for the final conjunction and sentence ending.
#    - Option B (Streamlined Functional Reduction):
#      Implement the fold with `reduce()`, but avoid creating intermediate enumerated list copies by relying on a cleaner binary step logic or standard accumulation pattern.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Memory & String Immutability: Strings in Python are immutable. Folding strings with `reduce` allocates and copies a new string on each step (O(N^2) aggregate copying). `str.join()` calculates total buffer length up front and performs a single allocation (O(N) linear time).
# ==============================================================================

# Target Output: "Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries"
'''
# Option A:
print(', '.join(countries[:-1]) + f', and {countries[-1]} ' + "are north European countries")

# Option B:
country = reduce(lambda x, y: f"{x}, {y}", countries[:-1])
result = f"{country}, and {countries[-1]} are north European countries"
print(result)
'''

# ==============================================================================
# Level 2 - Exercise 12: categorize_countries (Pass 2: Alternative Exploration) — verified 2026-10-16
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Declarative List Comprehension):
#      Replace the accumulator loop and `.append()` calls with an idiomatic list comprehension that extracts the country name from each dictionary while applying the case-insensitive substring predicate.
#    - Option B (Higher-Order Function Pipeline):
#      Compose Python's `filter()` and `map()` to decouple the filtering predicate from the field projection (`'name'`).
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Bytecode Efficiency vs Functional Laziness: List comprehensions run at C speed using optimized bytecode instructions, eliminating attribute lookup overhead for `.append`. Meanwhile, `filter()` and `map()` stream data lazily without allocating entire intermediate lists.
# ==============================================================================

# Target Output: list of matched country names (e.g. categorize_countries('land'))
'''
# Option A
from countries_data import countries_data
def categorize_countries(pattern):
    return [item["name"] for item in countries_data if pattern.lower() in item["name"].lower()]
print(categorize_countries("land"))

# Option B
from countries_data import countries_data
def categorize_countries(pattern):
    filtered = filter(lambda country: pattern.lower() in country["name"].lower(), countries_data)
    mapped = map(lambda country: country["name"], filtered)
    return list(mapped)

print(categorize_countries("land"))
'''


# ==============================================================================
# Level 2 - Exercise 13: countries_by_starting_letter (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (dict.get() with a Default):
#      Replace the `if key in result / else` branch with a single line that reads the
#      current count with a fallback default and adds 1. Research: what does the 2nd
#      argument of `dict.get()` do?
#    - Option B (collections.Counter + Generator Expression):
#      Counting things is so common that the standard library has a dict subclass built
#      for it. Feed it a generator expression that produces each country's first letter:
#      `Counter(<first letter> for <country> in ...)`. No loop body, no branching.
#    - Option C (collections.defaultdict):
#      Explore `defaultdict(int)`. Why can you write `result[key] += 1` on a key that
#      doesn't exist yet without a KeyError?
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Double Lookup: Your Pass 1 `if key in result: result[key] += 1` hashes the key
#      twice (once for `in`, once for `+=`). Which options avoid that?
#    - Counter Extras: Counter is still a dict, but it adds `.most_common(n)`. Which
#      Level 3 task could reuse it?
#    - Complexity: All options are O(N) time and O(K) space (K = unique letters).
#
# 3. Additional Challenges & Edge Cases:
#    - Non-ASCII Trap: The dataset contains 'Åland Islands'. What key does it produce?
#      Should 'Å' be its own bucket or count under 'A'? (Research: `unicodedata.normalize`.)
#    - Sorted Output: Return the dict ordered alphabetically by letter.
# ==============================================================================

# Target Output (counts per first letter, e.g.): {'A': 15, 'B': 21, 'C': 23, ..., 'Z': 2, 'Å': 1}
# Write your Pass 2 solution below:
from countries_data import countries_data
'''
# Option A
def countries_by_starting_letters():
    result = {}
    for country in countries_data:
        country_name = country["name"][0].upper()
        result[country_name] = result.get(country_name, 0) + 1
    return result
print(countries_by_starting_letters())
'''
'''
# Option B
def countries_by_starting_letters():
    return dict(Counter([country["name"][0].upper() for country in countries_data]))
print(countries_by_starting_letters())
'''
'''
# Option C
def countries_by_starting_letters():
    letter_counts = defaultdict(int)
    for country in countries_data:
        first_letter = country["name"][0].upper()
        letter_counts[first_letter] += 1
    return dict(letter_counts)
print(countries_by_starting_letters())
'''
# ==============================================================================
# Level 2 - Exercise 14: get_first_ten_countries (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (map() + operator.itemgetter):
#      Replace the comprehension with `map()` over the sliced data. Instead of a lambda,
#      use the standard library's ready-made "grab this key" callable from the
#      `operator` module.
#    - Option B (itertools.islice: Lazy Slicing):
#      Slicing `[:10]` only works on sequences (lists, tuples, strings). Rewrite the
#      function using `itertools.islice()`, which works on ANY iterable,
#      including generators that have no `len()` and can't be indexed.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Slice Copy vs Lazy Iterator: `countries_data[:10]` builds a new 10-item list.
#      `islice` creates nothing up front; it stops pulling items after 10.
#    - itemgetter vs lambda: `itemgetter('name')` runs in C with no Python frame per call.
#    - Complexity: O(k) time where k = 10, for both slicing and islice.
#
# 3. Additional Challenges & Edge Cases:
#    - Parameterize: `get_first_n_countries(n=10)`. What should happen with n=0? A negative n?
#    - Generator Source: Test your Option B on `(c for c in countries_data)`. Does
#      Option A still work on that input? Why not?
# ==============================================================================

# Target Output: ['Afghanistan', 'Åland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda']
# Write your Pass 2 solution below:
'''
# Option A:
def get_first_ten_countries():
    return list(map(itemgetter('name'), countries_data[:10]))
print(get_first_ten_countries()) 
'''
'''
# Option B:
def get_first_ten_countries():
    return list(map(itemgetter('name'), itertools.islice(countries_data, 10)))
print(get_first_ten_countries()) 
'''

# ==============================================================================
# Level 2 - Exercise 15: get_last_ten_countries (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (map() + operator.itemgetter):
#      Same tool as Exercise 14 Option A, applied to the negative slice.
#    - Option B (collections.deque with maxlen):
#      A `deque` created with `maxlen=10` automatically drops old items from the left
#      as new ones arrive. Feed the whole stream of names into it. What's left at the end?
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Negative Slicing Needs a Length: `[-10:]` only works when Python knows the size.
#      A generator has no end until you consume it. Which option still works?
#    - Memory: Option B walks all N items (O(N) time) but never holds more than 10 (O(1) space).
#
# 3. Additional Challenges & Edge Cases:
#    - Fewer Than 10: Test on a 3-item list. Does `[-10:]` crash or return all 3?
#    - Off-by-One Trap: Compare `data[-10:]` vs `data[len(data) - 10:]` on a 3-item list.
#      What does the negative start index do in the second version?
# ==============================================================================

# Target Output: ['Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela (Bolivarian Republic of)', 'Viet Nam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']
# Write your Pass 2 solution below:
'''
# Option A
def get_last_ten_countries():
    return list(map(itemgetter("name"), countries_data[-10:]))
print(get_last_ten_countries())
'''
'''
# Option B
def get_last_ten_countries():
    dq = deque([country["name"] for country in countries_data], maxlen=10)
    return list(dq)
print(get_last_ten_countries())
'''
# ==============================================================================
# Level 3 - Exercise 1A: Sort by Name, Capital, and Population (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (operator.itemgetter as the key):
#      Replace each `key=lambda country: country["..."]` with `itemgetter`.
#    - Option B (list.sort() In-Place vs sorted()):
#      Rewrite one sort using `.sort()` on a copy. What does `.sort()` return?
#      (Same trap as `random.shuffle` on Day 12.)
#
# 2. Mechanistic Analysis & Trade-offs:
#    - sorted() vs .sort(): One builds a new list, the other mutates and returns None.
#      When would you choose in-place?
#    - Stability: Python's sort (Timsort) is stable. Equal keys keep their original
#      order. How does that let you chain two sorts to get a multi-key ordering?
#    - Complexity: O(N log N) time; sorted() needs O(N) extra space.
#
# 3. Additional Challenges & Edge Cases:
#    - Unicode Trap: Sort by name and print the LAST 3 items. Why is 'Åland Islands'
#      after 'Zimbabwe'? (Research: how strings compare by code point, `str.casefold`,
#      `locale.strxfrm`.)
#    - Empty Capital Trap: 5 countries have capital == '' (Antarctica, Bouvet Island,
#      Heard Island and McDonald Islands, Macao, US Minor Outlying Islands). They sort to
#      the FRONT. Push them to the END using a TUPLE key, without filtering them out.
#    - Multi-Key: Sort by population descending, then by name ascending for ties.
#      Do it with ONE key, without `reverse=True`. (Hint: what happens if you negate a number?)
# ==============================================================================
from countries_data import countries_data
# Target Output: 3 sorted lists. Check: by name -> starts 'Afghanistan', by population -> starts with the smallest
# Write your Pass 2 solution below:
'''
# Option A:
sorted_names = sorted(countries_data, key=itemgetter("name"))
mapped_names = list(map(itemgetter("name"), sorted_names))
print(mapped_names)
'''
'''
sorted_capital = sorted(countries_data, key=itemgetter("capital", "name"))
mapped_capital = list(map(itemgetter("capital", "name"), sorted_capital))
print(mapped_capital[:5])
'''
'''
sorted_population = sorted(countries_data, key=itemgetter("population", "name"))
mapped_population = list(map(itemgetter("population", "name"), sorted_population))
print(mapped_population)
'''

# Option B
sorted_by_name = sorted(countries_data, key=lambda country: country["name"])
print(sorted_by_name)
# ==============================================================================
# Level 3 - Exercise 1B: Ten Most Spoken Languages (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Counter + Nested Generator + most_common):
#      Flatten every country's `languages` list with a nested generator expression
#      (Day 13 flattening pattern!), feed it to `Counter`, and use `.most_common(10)`.
#      Target: a single expression inside the function.
#    - Option B (itertools.chain.from_iterable Pipeline):
#      Decouple flattening from counting: first build a flat stream of languages with
#      `chain.from_iterable(map(...))`, then count it.
#    - Option C (heapq.nlargest on Your Pass 1 Dict):
#      Keep your manual tally, but replace `sorted(...)[:10]` with `heapq.nlargest(10, ...)`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Full Sort vs Heap: `sorted(...)[:10]` sorts ALL K languages, O(K log K).
#      `nlargest(10, ...)` keeps a 10-item heap, O(K log 10). When does that matter?
#    - Reuse: Is this the same counting problem as Exercise 13? What changed?
#
# 3. Additional Challenges & Edge Cases:
#    - Tie Trap: 10th place is a TIE. 'Serbian' and 'Swahili' both have 4. Which one
#      appears in your result, and why? Is that the same across all 3 options?
#      Write a version that includes every language tied with 10th place.
# ==============================================================================

# Target Output: [('English', 91), ('French', 45), ('Arabic', 25), ('Spanish', 24), ('Portuguese', 9), ('Russian', 9), ('Dutch', 8), ('German', 7), ('Chinese', 5), (<Serbian or Swahili>, 4)]
# Write your Pass 2 solution below:



# ==============================================================================
# Level 3 - Exercise 1C: Ten Most Populated Countries (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (heapq.nlargest with key=):
#      Get the top 10 dictionaries directly with `heapq.nlargest(n, iterable, key=...)`.
#      No full sort, no slicing, no `reverse=True`.
#    - Option B (itemgetter Key + Projection Pipeline):
#      Keep `sorted(..., reverse=True)[:10]`, but use `itemgetter` for the key AND build the
#      output records with `map()` instead of a comprehension.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - O(N log N) vs O(N log k): You sort 250 countries just to keep 10. Explain why
#      `nlargest` does less work, and when `sorted` is still the better choice
#      (hint: the docs say what happens when n is close to N).
#    - Data Shape: Your Pass 1 returns dicts `{"country": ..., "population": ...}`.
#      Compare that with returning `(name, population)` tuples. Which is easier for
#      a caller to use? Which is easier to print?
#
# 3. Additional Challenges & Edge Cases:
#    - Parameterize: `most_populated(n=10)`. Test n=0 and n=1000 (more than the dataset).
#    - Formatting: Print the result as a ranked table with thousands separators:
#      ` 1. China                 1,377,422,166` (research the f-string `,` format spec
#      and string alignment like `:<20`).
# ==============================================================================

# Target Output: [China 1377422166, India 1295210000, United States of America 323947000, Indonesia 258705000, Brazil 206135893, Pakistan 194125062, Nigeria 186988000, Bangladesh 161006790, Russian Federation 146599183, Japan 126960000]
# Write your Pass 2 solution below:



