# Day 12: Modules Exercises

# ==============================================================================
# Level 1 - Exercise 1: random_user_id (COMPLETED)
# ==============================================================================
from collections.abc import Sequence
import string
import random
#
def random_user_id(length):
    random_id = string.ascii_letters + string.digits
    return ''.join(random.choices(random_id, k=length))
#
# print(random_user_id())

# ==============================================================================
# Level 1 - Exercise 2: user_id_gen_by_user
# ==============================================================================
# Challenge: Declare a function named user_id_gen_by_user.
# It takes no parameters, but prompts the user for two inputs using input():
#   1. Number of characters per ID (e.g. 5)
#   2. Number of IDs to generate (e.g. 5)
#
# It generates the specified number of unique/random alphanumeric IDs,
# each having the specified character length, and returns them
# (formatted across newlines or printed).
#
# Example run:
#   user_id_gen_by_user()
#   Enter character count: 5
#   Enter ID count: 3
#   Output:
#     kcsy2
#     SMFYb
#     bWmeq
#
# Adversarial Test Matrix:
#   1. Standard Case: chars=5, count=3 (generates 3 distinct 5-char IDs)
#   2. Boundary Case: chars=1, count=1 (single 1-character token)
#   3. Trap Case: count=0 (zero IDs generated, returns empty / handles cleanly)
# ==============================================================================

# Write your solution below:

'''
import string
import random

def user_id_gen_by_user():
    items = string.ascii_letters + string.digits
    input_char_count = int(input("Enter character count: "))
    input_id_count = int(input("Enter ID count: "))
    generated_id = []

    for _ in range(input_id_count):
        randomized_id = ''.join([random.choice(items) for _ in range(input_char_count)])
        generated_id.append(randomized_id)
    return '\n'.join(generated_id)




print(user_id_gen_by_user())
'''

# ==============================================================================
# Level 1 - Exercise 3: rgb_color_gen (COMPLETED)
# ==============================================================================
# Challenge: Write a function named rgb_color_gen that generates random RGB colors.
# An RGB color format has three integer values, each ranging from 0 to 255 inclusive.
# The function takes no parameters and returns a formatted string: "rgb(125, 244, 255)".
#
# Examples:
#   print(rgb_color_gen())  # "rgb(125, 244, 255)"
#   print(rgb_color_gen())  # "rgb(19, 12, 102)"
#
# Adversarial Test Matrix:
#   1. Standard Case: Output string format matches 'rgb(r, g, b)' exactly.
#   2. Boundary Case: All three values are valid integer values between 0 and 255 inclusive (0 <= val <= 255).
#   3. Trap Case: Return vs Print — must return the string object, not print it. Multiple successive calls must generate varying random numbers.
# ==============================================================================

'''
import random

def rgb_color_gen():
    rgb_list = []
    for _ in range(3):
        color = random.randrange(0,256)
        rgb_list.append(color)
    tuple_rgb = tuple(rgb_list)
    first, second, third = tuple_rgb
    return f"rgb({first}, {second}, {third})"
result = rgb_color_gen()
print(result)
'''

# ==============================================================================
# Level 2 - Exercise 1: list_of_hexa_colors
# ==============================================================================
# Challenge: Write a function named list_of_hexa_colors which returns any number
# of hexadecimal colors in a list.
# A hexadecimal color starts with a '#' symbol followed by six hexadecimal
# digits (0-9, a-f).
#
# Function signature:
#   def list_of_hexa_colors(count=1):
#
# Examples:
#   list_of_hexa_colors(1)  # ['#a3e12f']
#   list_of_hexa_colors(3)  # ['#a3e12f', '#03ed55', '#eb3d2b']
#
# Adversarial Test Matrix:
#   1. Standard Case: count=3 -> returns a list of 3 hex strings, each formatted as '#hhhhhh' (length 7).
#   2. Boundary Case: count=0 -> returns empty list `[]`. count=1 -> returns 1-element list.
#   3. Trap Case: Ensure each color begins with '#' and consists only of valid hexadecimal characters (0-9, a-f).
# ==============================================================================

# Write your solution below:
