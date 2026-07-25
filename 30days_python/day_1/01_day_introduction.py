# This is an introduction for Day 1 that will tackle the following

## How to use print

print("Hello World")

# String
"""A collection of one or more characters under a single double quote "this" 
if a string is more than one sentence then we use a triple quote"""
# An example of this are:
# 'Bong'
# 'Triangle'
# 'Box'

## What are the arithmetics

print(1 + 1) #Addition(+)
print(2 - 1) #Division(-)
print(2 * 2) #Multiplication(*)
print(3 + 2) # Addition(+)
print(3 * 2) # Multiplication(*)
print(2 / 1) # Division(/)
print(4 ** 5) # Exponential(**)
print(3 % 2) # Modulus(%)
print(3 // 2) # Floor Division Operator(//)

# Data types
# Integer (Positive and Negative) = -3, -2, -1, 0, 1, 2, 3
# Float: Decimal number = -3.25, -2.55, 3.14
# Complex = 1 + j, 2 + 4j

## Checking data types

print(type(10)) # Int
print(type(3.14)) # Float
print(type(1 + 3j)) # Complex
print(type('Soggy')) # String
print(type([1, 2, 3])) # List
print(type({'name': "Soggy"})) # Dictionary
print(type({9.8, 3.14, 2.7})) # Tuple

# '#' this is for a single line comment
"""" This is for multiline comments"""

# Boolean: It is either a True or False value, T and F should always be uppercase
highnum = 5
lownum = 3

print(highnum < lownum) # False because 5 is not less than 3
print(lownum < highnum) # True because 3 is less than 5

# List
''' List is an ordered collection which allows to store different data type items.
A list is similar to an array in JavaScript'''
# Example

basket = ['Banana', 'Potato', 'Sugar', 'Plum'] # A list of items in the basket
numbers = [1, 2, 3, 4, 5] # List of numbers 
different = ['Hotdog', 3, True, 0.41] # Different data types in the list

# Dictionary
# Dictionary object is an unordered collection of data in a key value pair format.

# Example
user = {'name' : 'Bentelog',
        'age' : 12,
        'country' : 'Tondo',
        'is_married' : 'True',
        'skills' : ['holdap', 'carnap', 'snatcher']
        }

print(user)

# Tuple
# An ordered collection of different data types like list but tuples can not be modified once they are created

#Example
names = ('Soggy', 'boggy', 'lobby', 'bobby') # These are names
planets = ('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus') # These are planets

# Set
# A collection of data types similar to list and tuple.

#Example

num = {2, 4, 3, 6}
rand = {3.14, 9.81, 2.7}
# Order is not important in set



