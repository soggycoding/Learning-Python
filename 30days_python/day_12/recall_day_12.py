# Day 12: Modules - Pure Recall Challenges (Pass 3)

# ==============================================================================
# BATCHED RECALL PROTOCOL: LEVEL 1 (Exercises 1, 2, and 3)
# ==============================================================================
# Rules for Pure Recall:
# 1. Do NOT look back at `exercise_day_12.py` or `alternative_day12_solution.py`!
# 2. Write your implementations from pure conceptual retrieval.
# 3. Test each function against its Adversarial Test Matrix.
# ==============================================================================

# ------------------------------------------------------------------------------
# Recall 1: random_user_id()
# ------------------------------------------------------------------------------
# - Task: Write a function `random_user_id()` that returns a 6-character
#   alphanumeric random ID (using digits + uppercase + lowercase letters).
# - Contract: () -> str of length 6
# ------------------------------------------------------------------------------
'''
import string
import random

def random_user_id(length=6):
    characters = string.ascii_letters + string.digits
    generated_character = random.choices(characters, k=length)
    return ''.join(generated_character)
print(random_user_id())
'''
# ------------------------------------------------------------------------------
# Recall 2: user_id_gen_by_user()
# ------------------------------------------------------------------------------
# - Task: Write a function `user_id_gen_by_user()` that prompts the user for:
#     1. Number of characters per ID
#     2. Number of IDs to generate
#   and returns all generated IDs separated by newlines.
# - Contract: () -> str containing multiple IDs joined by '\n'
# ------------------------------------------------------------------------------
'''
import string
import random

def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits
    characters_per_id = int(input("Number of characters per ID: "))
    id_requirements = int(input("Number of IDs to generate: "))
    id_list = []
    for _ in range(id_requirements):
        id_generator = random.sample(characters, k=characters_per_id)
        id_generated = ''.join(id_generator)
        id_list.append(id_generated)
    return '\n'.join(id_list)
print(user_id_gen_by_user())
'''
# ------------------------------------------------------------------------------
# Recall 3: rgb_color_gen()
# ------------------------------------------------------------------------------
# - Task: Write a function `rgb_color_gen()` that returns a random RGB color
#   string in standard format: "rgb(r, g, b)" where 0 <= r, g, b <= 255.
# - Contract: () -> str
# ------------------------------------------------------------------------------
'''
import random

def rgb_color_gen():
    r,g,b = tuple([random.randint(0,255) for _ in range(3)])
    return f"rgb({r}, {g}, {b})"
result = rgb_color_gen()
print(result)
'''