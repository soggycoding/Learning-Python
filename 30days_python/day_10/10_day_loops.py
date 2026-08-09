# Loops
'''
while condition:
    code goes here
'''

count = 0
while count < 5:
    print(count)
    count = count + 1

# In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use 'else'.

'''
while condition:
    code goes here
else:
    code goes here if condition is false
'''

while count < 5:
    print(count)
    count = count + 1
else:
    print('Loop finished')

# In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use 'else'.

# Break and Continue - Part 1
# Break: WE yse break when we like to get out of or stop the loop

'''
while condition:
    code goes here
    if another_condition:
        break
'''

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# The above while loop only prints 0,1,2 but when it reaches 3 it stops.
# Continue: With the continue statement we can skip the current iteration, the continue with the next:
'''
while condition:
    code goes here
    if another_condition:
        continue
'''

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        continue
print(count)
count = count + 1

# For Loop
# Using For loop on list


'''
for iterator in lst:
    code goes here
'''

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# For loop on string
'''
for iterator in string:
    code goes here
'''

language = 'Python'
for letter in 'Python':
    print(letter)

for i in range(len(language)):
    print(language[i])

# Using For loop on tuple
'''
for iterator in tpl:
    code goes here
'''

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For loop with dictionary looping through a dictionary gives you the key of the dictionary.language

'''
for iterator in dct:
    code goes here
'''

person = {
    'first_name' : 'Soggy',
    'last_name' : 'Bing',
    'age' : 25,
    'country' : 'Norway',
    'is_married' : True,
    'skills' : ['JavaScript', 'HTML', 'CSS', 'React'],
    'address': {
        'street' : '123 Main St',
        'city' : 'Oslo',
        'zip_code' : '0101'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

# Using For loop in set:

'''
for iterator in st:
    code goes here
'''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# Break and continue - Part 2
'''
for iterator in sequence:
    code goes here
    if condition:
        break
'''
# BREAK
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

# CONTINUE

'''
for iterator in sequence:
    code goes here
    if condition:
        continue
'''

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")
print('outside the loop')

# The range function

'''
range(start, stop, step)
'''

lst = list(range(11))
print(lst)
st = set(range(1,11))
print(st)

lst = list(range(0,11,2))
print(lst)
lst = list(range(10,0,-1))
print(lst)

# For backward from start to end
lst = list(range(11, 0, -2))
print(lst)

for number in range(11):
    print(number)

# Nested For loop

'''
for x in y:
    for t in x:
        print(t)
'''

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# For else

'''
For iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
'''

for number in range(11):
    print(number)
else:
    print('The loop stops at ', 11)

# The 'pass' statement

for number in range(6):
    pass