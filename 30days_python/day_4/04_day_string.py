#  Create a string

letter = 'P'
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline string
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name)
# Checking the length of a string using len() built-in function
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Escape Sequence in Strings
print(' I hope everyone is enjoying the python challenge. \nAre you ?')
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol (\\)')
print('In every programming language it starts with \"Hello, World!\"')

# Strings only
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name,last_name, language)
print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius %d is %.2f.' %(radius, area)

python_libraries = ['Django', 'Flash', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string)

# New Style String Formatting
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 3
b = 4

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'(radius, area)
print(formated_string)

# String Interpolation / f-Strings
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')

# Unpacking characters
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessing characters in Strings by Index
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language)
last_letter = language[last_index]
print(last_letter)

# If we want to start from right end we can use negative indexing. -1 is te last index.
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

# Slicing Python Strings
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)
# Another way
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

# Reversing a string
greeting = 'Hello, World!'
print(greeting[::-1]) 

# Skippinng characters while slicing
language = 'Python'
pto = language[0:6:2]
print(pto)

# String methods
## Capitalize
challenge = 'thirty days of python'
print(challenge.capitalize())

## Count
print(challenge.count('y'))
print(challenge.count('y', 7, 14))

## endswith
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

## expandtabs
print(challenge.expandtabs())
print(challenge.expandtabs(10))

## find
print(challenge.find('y'))
print(challenge.find('th'))

## rfind
print(challenge.rfind('y'))
print(challenge.rfind('th'))

## format
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)

## index
substring = 'da'
print(challenge.index(substring))
print(challenge.index(substring, 9))

## rindex
