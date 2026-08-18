# Functions

## Declaring and calling a function
# Function without parameters
'''
from typing_extensions import get_original_bases
def generate_full_name():
    first_name = 'John'
    last_name = 'Bing'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name ()

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
'''

# Function Returning a Value - Part 1
def generate_full_name():
    first_name = "John"
    last_name = "Bing"
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

# Function with Parameters
def greetings(name):
    message = name + ', welcome to python for everyone! '
    return message

print(greetings('John'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x