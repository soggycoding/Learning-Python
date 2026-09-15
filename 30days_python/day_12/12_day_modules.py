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

# 6. Built-in: secrets module (Cryptographically Secure for sensitive data)
import secrets

# A. Selecting a random element from a sequence (e.g. load balancing / server selection)
servers = ['server-us-east-1', 'server-eu-west-1', 'server-ap-south-1']
assigned_server = secrets.choice(servers)
print('Assigned server:', assigned_server)

# B. Secure integer below a bound [0, n) (e.g. rolling a 20-sided die: 1 to 20)
d20_roll = secrets.randbelow(20) + 1
print('D20 roll result:', d20_roll)

# C. Generating a URL-safe token (e.g. email verification / password reset link)
password_reset_token = secrets.token_urlsafe(16)
print('Reset link token:', password_reset_token)

# D. Generating a random hex key (e.g. API access token)
api_session_key = secrets.token_hex(16)
print('API session key:', api_session_key)

# E. Safe comparison resistant to timing attacks (constant-time comparison)
stored_token = 'vault_key_abc123'
incoming_token = 'vault_key_abc123'
is_authenticated = secrets.compare_digest(stored_token, incoming_token)
print('Token match valid:', is_authenticated)

