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