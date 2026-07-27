# Boolean

print(True)
print(False)

# Example:Integers

print('Addition: ', 1 + 2) # 3
print('Subtraction: ', 2 - 1) # 1
print('Multiplication: ', 2 * 3) # 6
print('Division: ', 4 / 2) # 2.0
print('Division: ', 6 / 2) # 3.0
print('Division: ', 7 / 2) # 3.5
print('Division without the remainder: ', 7 // 2) # 3, gives without the floating number or without the remaining
print('Division without the remainder: ', 7 // 3) # 2
print('Modulus: ', 3 % 2) # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2

# Example:Floats
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Example:Complex Numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))

# Declaring a variable: Example

a = 3 # a is a variable name and 3 is an integer data type 
b = 2 # b is a variable name and 2 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print ('a + b = ', total)
print ('a - b = ', diff)
print ('a * b = ', product)
print ('a / b = ', division)
print ('a % b = ', remainder)
print ('a // b = ', floor_division)
print ('a ** b = ', exponential)

# Declaring Values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('diff: ', diff)
print('product: ', product)
print('div: ', div)
print('remainder: ', remainder)

# Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print ('Area of a circle: ', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

# Calculate the density of a liquid
mass = 75 # in kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # Adding unit to the density

# Comparison Operators
print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 > 3)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('milk') != len('meat'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))
print(len('python') > len('dragon'))

# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False: ', False == False)

print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)
print('S in Soggy', 'S' in 'Soggy')
print('B not in Bong', 'B' in 'Bong')
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')
print('4 is 2 ** 2:', 4 is 2 ** 2)

# Logical Operators
print(3 > 2 and 4 > 3)
print(3 > 2 and 4 < 3)
print(3 < 2 and 4 < 3)
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)
print(3 > 2 or 4 < 3)
print(3 < 2 or 4 < 3)
print('True or False: ', True or False)
print(not 3 > 2)
print(not True)
print(not False)
print(not not True)
print(not not False)