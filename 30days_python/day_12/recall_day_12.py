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

# ==============================================================================
# BATCHED RECALL PROTOCOL: LEVEL 2 (Exercises 1, 2, and 3)
# ==============================================================================
# Rules for Pure Recall:
# 1. Do NOT look back at `exercise_day_12.py` or `alternative_day12_solution.py`!
# 2. Write your implementations from pure conceptual retrieval.
# 3. Test each function against its Adversarial Test Matrix.
# ==============================================================================

# ------------------------------------------------------------------------------
# Recall 1: list_of_hexa_colors(count=1)
# ------------------------------------------------------------------------------
# - Task: Write a function `list_of_hexa_colors(count=1)` that returns a list
#   of any number of random hexadecimal color strings.
# - Format: Each string begins with '#' followed by 6 hex characters (0-9, a-f).
# - Contract: (int) -> list[str]
# - Adversarial Test Cases:
#   * Standard: count=3 -> list of 3 '#hhhhhh' strings.
#   * Boundary: count=0 -> [], count=1 -> 1-element list.
#   * Trap: Each color must be valid hex characters, length 7.
# ------------------------------------------------------------------------------
# Write Recall 1 below:
'''
import string
import random

def list_of_hexa_colors(count=1):
    pool = string.ascii_letters[:6] + string.digits
    hexa_list = []
    for _ in range(count):
        generator = random.choices(pool, k=6)
        generated = ''.join(generator)
        generated = "#" + generated
        hexa_list.append(generated)
    return hexa_list
'''



# ------------------------------------------------------------------------------
# Recall 2: list_of_rgb_colors(count=1)
# ------------------------------------------------------------------------------
# - Task: Write a function `list_of_rgb_colors(count=1)` that returns a list
#   of any number of random RGB color strings.
# - Format: Each string formatted as "rgb(r, g, b)" where 0 <= r, g, b <= 255.
# - Contract: (int) -> list[str]
# - Adversarial Test Cases:
#   * Standard: count=3 -> list of 3 'rgb(r, g, b)' strings.
#   * Boundary: count=0 -> [], count=1 -> 1-element list.
#   * Trap: Channel values must be integers between 0 and 255 inclusive.
# ------------------------------------------------------------------------------

# Write Recall 2 below:

'''
def list_of_rgb_colors(count=1):
    rgb_list = []
    for _ in range(count):
        r,g,b = random.choices(range(256), k=3)
        generated = f"rgb({r}, {g}, {b})"
        rgb_list.append(generated)
    return rgb_list
'''


# ------------------------------------------------------------------------------
# Recall 3: generate_colors(color_type='hexa', count=1)
# ------------------------------------------------------------------------------
# - Task: Write a function `generate_colors(color_type='hexa', count=1)` that
#   dispatches to generate any number of hexa or rgb colors.
# - Architecture: Use a dispatch table / first-class function lookup.
# - Contract: (str, int) -> list[str] | str
# - Adversarial Test Cases:
#   * Standard: ('hexa', 3), ('rgb', 2).
#   * Boundary: count=0 -> [], case-insensitive & whitespace ('RGB', 'rgb ').
#   * Trap: Invalid types ('' or 'cmyk') return an error message cleanly.
# ------------------------------------------------------------------------------

# Write Recall 3 below:

'''
def generate_colors(color_type='hexa', count=1):
    clean = color_type.lower().strip()
    dispatch = {
        'hexa' : list_of_hexa_colors,
        'rgb' : list_of_rgb_colors
    }
    generated = dispatch.get(clean)
    if not generated:
        return f"Invalid input '{color_type}', should be 'hexa' or 'rgb'."
    return generated(count)
print(generate_colors('rgb ', 3))
'''
