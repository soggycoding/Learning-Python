# Day 12: Modules Exercises

# ==============================================================================
# Level 1 - Exercise 1: random_user_id
# ==============================================================================
# Challenge: Write a function named random_user_id that generates a 6-character
# alphanumeric user ID (digits and characters).
# It takes no parameters and returns a 6-character string.
# Example: '1ee33d', '4f92bc', 'a8c19d'
# ==============================================================================

# Write your solution below:
import string
import random

def random_user_id(length=6):
    random_id = string.ascii_letters + string.digits
    return ''.join(random.choices(random_id, k=length))
print(random_user_id())