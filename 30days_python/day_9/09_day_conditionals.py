# Conditionals

## If condition
'''
if condition:
   this part of code runs for truthy conditions
'''

a = 3
if a > 0:
    print('A is a positive number')

## If Else

'''
if condition:
    this part of the code runs for truthy conditions
else:
    this part of the code runs for false conditions
'''

if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

## If Elif Else

'''
if condition:
    this part of the code runs for truthy conditions
elif condition:
    this part of the code runs for truthy conditions
else:
    this part of the code runs for false conditions
'''

if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

## Short hand

# code if conditions else code

print('A is positive') if a > 0 else print('A is negative')

# Nested Conditions

'''
if conditions:
    code
    if condition:
        code
'''

if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# If condition and Logical Operators

'''
if condition and condition:
    code
'''

if a > 0 and a % 2 == 0:
    print('A is a n even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators

'''
if condition or condition:
    code
'''

user = 'James'
access_level = 4
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')