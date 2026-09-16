# Day 12: Modules - Alternative Solutions (Pass 2)

# ==============================================================================
# Level 1 - Exercise 1: random_user_id (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Alternative A (List Comprehension with random.choice):
#      Build the 6-character token using a list comprehension + join with
#      `random.choice(pool)` rather than `random.choices(pool, k=6)`.
#    - Alternative B (Cryptographically Secure via secrets module):
#      Explore Python's built-in `secrets` module (e.g. `secrets.choice`) and observe
#      why security tokens and user session IDs prefer `secrets` over `random`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Contrast `random.choices` (sampling WITH replacement) vs `random.sample` (sampling WITHOUT replacement).
#    - Analyze Time & Space Complexity: Compare bulk `random.choices` vs comprehension loop.
# ==============================================================================

# Write your Pass 2 solution below:
'''
# OPTION A:
# Sample with replacement and list comprehension
import string
import random

def random_user_id(length=6):
    item = string.ascii_letters + string.digits
    return ''.join([random.choice(item) for items in range(length)])
print(random_user_id())
'''

'''
# OPTION B:
import string
import secrets

def random_user_id(length=6):
    items = string.ascii_letters + string.digits
    return ''.join([secrets.choice(items) for item in range(length)])
print(random_user_id())
'''
'''
# Sampling without replacement
import string
import random

def random_user_id(length=6):
    item = string.ascii_letters + string.digits
    return ''.join(random.sample(item, k=length))
print(random_user_id())
'''

# ==============================================================================
# Level 1 - Exercise 2: user_id_gen_by_user (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Modular Decomposition (Function Composition):
#    - Instead of re-implementing character selection inside user_id_gen_by_user,
#      reuse `random_user_id(char_count)` from Exercise 1 as a dedicated helper.
# 2. Return Contract vs Side-Effect:
#    - Rather than printing directly in the loop and returning None, build a
#      function that returns a list of tokens, or returns a multi-line string
#      via `'\n'.join(...)` so the caller controls display/storage.
# 3. Loop Idiom & Safety:
#    - Replace the manual `while counter != count` loop with an idiomatic `for`
#      loop or list comprehension over `range(count)`.
# ==============================================================================

# Write your Pass 2 solution below:
'''
from exercise_day_12 import random_user_id

def user_id_gen_by_user():
    random_id_gen = int(input("Input how many characters should be randomized: "))
    user_id_count = int(input("Input how many ID's should be generated: "))
    user_list = []
    for _ in range(user_id_count):
        generated_id = random_user_id(random_id_gen)
        user_list.append(generated_id)
    return '\n'.join(user_list)
        
print(user_id_gen_by_user())
'''
'''
import string
import secrets


def user_id_gen_by_user():
    items = string.ascii_letters + string.digits
    input_char_count = int(input("Enter character count: "))
    input_id_count = int(input("Enter ID count: "))
    generated_id = []

    for _ in range(input_id_count):
        randomized_id = ''.join([secrets.choice(items) for _ in range(input_char_count)])
        generated_id.append(randomized_id)
    return '\n'.join(generated_id)

print(user_id_gen_by_user())
'''

# ==============================================================================
# Level 1 - Exercise 3: rgb_color_gen (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Alternative A (Unpacking with List Comprehension & randint):
#      Generate the 3 channel values using a list comprehension with `random.randint(0, 255)`,
#      unpack them into discrete variables (e.g. `r, g, b`), and format via an explicit f-string.
#    - Alternative B (Bulk Generation with random.choices):
#      Explore sampling directly from `range(256)` using `random.choices(range(256), k=3)`
#      to produce all three channels in a single call without a Python-level loop.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Brittle Formatting vs Explicit Formatting: Why relying on `tuple`'s string representation
#      `f"rgb{tuple_val}"` is a clever shortcut for 3 items, but why explicit string interpolation
#      is preferred in production (e.g. custom spacing, or single-element tuple trailing commas).
#    - Complexity Analysis:
#      * Time Complexity: O(1) constant time (generating exactly 3 channels).
#      * Space Complexity: O(1) constant auxiliary space.
#      * Micro-efficiency: Bulk sampling (`random.choices`) vs 3 separate Python loop iterations.
# ==============================================================================

# Write your Pass 2 solution below:

'''
import random

# Solution 1
def rgb_color_gen():
    r,g,b = tuple(random.randint(0,255) for _ in range(3))
    return f"rgb({r}, {g}, {b})"
result = rgb_color_gen()
print(result)

# Solution 2
def rgb_color_gen():
    r,g,b = random.choices(range(256), k=3)
    return f"rgb({r}, {g}, {b})"
result = rgb_color_gen()
print(result)
'''

# ==============================================================================
# Level 2 - Exercise 1: list_of_hexa_colors (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Alternative A (Nested List Comprehension & Expression Inlining):
#      Eliminate manual list initialization and `.append()` loops by returning
#      a list comprehension. Generate the 6-character hex string inline
#      using an f-string or helper composition.
#    - Alternative B (Numeric Randomness with Hex Format Specifier `:06x`):
#      Instead of picking 6 random characters from a string pool, sample a single
#      random integer from the entire 24-bit color space (0 to 16,777,215, or 0xFFFFFF)
#      and format it directly using hex formatting: `f"#{val:06x}"`.
#    - Alternative C (Standard Library `secrets.token_hex`):
#      Examine `secrets.token_hex(nbytes=3)`—each byte produces 2 hex characters,
#      yielding exactly 6 hex characters directly from the operating system's CSPRNG.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Why `:06x` padding matters: What happens if an integer is `15` without padding?
#    - Algorithmic Complexity:
#      * Time Complexity: Compare string character sampling (6 lookups + join per color)
#        vs single integer generation ($O(N)$ with lower constant factor).
#      * Space Complexity: Auxiliary space comparison.
# ==============================================================================

# Write your Pass 2 solution below:

import secrets
import string
import random

'''
def list_of_hexa_colors(count=3):
    pool = string.ascii_lowercase[:6] + string.digits
    return [f"#{''.join(random.choices(pool, k=6))}" for _ in range(count)]
print(list_of_hexa_colors(3))
'''
'''
def list_of_hexa_colors(count=1):
    return [f"#{random.getrandbits(24):06x}" for _ in range(count)]
print(list_of_hexa_colors(3))
'''

'''
def list_of_hexa_colors(count=1):
    return [f"#{secrets.token_hex(3)}" for _ in range(count)]
print(list_of_hexa_colors(3))
'''
