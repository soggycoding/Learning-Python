# Day 12: Modules Walkthrough & Examples

# 1. Built-in: random module
import random

# Random float between 0.0 and 1.0
print(random.random())

# Random integer in range [a, b] inclusive
print(random.randint(1, 10))

# Random choice from a sequence
fruits = ['apple', 'banana', 'cherry', 'date']
print(random.choice(fruits))

# 2. Built-in: string module
import string

print(string.ascii_letters)   # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)          # '0123456789'
print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# 3. Combining random + string to generate random characters
def generate_sample_token(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

print(generate_sample_token(6))

# 4. Built-in: math module
import math

print(math.pi)
print(math.sqrt(25))
print(math.floor(9.8))
print(math.ceil(9.1))

# 5. Built-in: statistics module
import statistics

scores = [85, 90, 78, 92, 85, 95]
print(statistics.mean(scores))
print(statistics.median(scores))
print(statistics.mode(scores))
