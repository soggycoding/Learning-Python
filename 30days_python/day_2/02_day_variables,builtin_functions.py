
print("hello, world") # Prints the text value Hello, World
len("Hello, world") # Counts the number of characters including space
type('Hello, World') # Checks the data type
str(19) # it converts number to string
int('10') # it converts to number
float(10) # it converts integer to decimal
input('Enter your name: ') # it takes user input

min(20, 30, 40, 50) # gives the minimum value
max(20, 30, 40, 50) # gives the maximum value
min([20, 30, 40, 50]) # it takes list as an argument and return min
max([20, 30, 40, 50]) # takes list as an argument and return max
sum([20, 30, 40, 50]) # takes only list as an argument and return the sum

# Different Python data types
first_name = 'Hotdog' # str
last_name = 'Bentelog' #str
country = 'CDO' #str
city = 'Cheesy' #str
age = 100 #int

# Printing out types
print(type('Hotdog')) # str
print(type(first_name)) # str
print(type(10)) # int
print(type(3.14)) # float
print(type(1+1j)) # complex
print(type(True)) # bool
print(type([1, 2, 3, 4])) # list
print(type({'name': 'Hotdog'})) # dict
print(type((1,2))) # tuple
print(type(zip([1,2],[3,4]))) # zip

# Casting
# int to float
num_int = 10
print('num_int', num_int) # 10
num_float = float(num_int)
print('num_float', num_float) # 10.0

# float to int
gravity = 9.81
print(int(gravity)) # 9

# int to string
num_int = 10
print(num_int) # 10
num_str = str(num_int)
print(num_str) # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str) # Convert the string to a float first
num_int = int(num_float) # Then convert the float to an integer
print('num_int', int(num_str)) # 10
print('num_float', float(num_str)) # 10.6
num_int = int(num_float)
print('num_int', int(num_int)) # 10

# str to list
first_name1= 'hotdog'
print(first_name1)
first_name_to_list = list(first_name1)
print(first_name_to_list)

