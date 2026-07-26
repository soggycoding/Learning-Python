# Day 2: 30 Days of python programming

# Exercise #1
first_name = 'Soggy'
last_name = 'Woggy'
full_name = 'Soggy Woggy'
country = 'Philippines'
city = 'Manila'
age = 100
year = 1900
is_married = False
is_true = True
is_lights_on = True
big, small, tiny = 'circle', 'triangle', 'rectangle'

# Exercise #2
# 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_lights_on))

# 2
print(len(first_name))

# 3
len_firstname = len(first_name)
len_lastname = len(last_name)
print(len_firstname > len_lastname)

# 4
num_one = 5
num_two = 4
# 5
total = num_one + num_two
# 6
total = num_two - num_one   
# 7
total = num_two * num_one
# 8
total = num_one / num_two
# 9
remainder = num_two % num_one
# 10
exp = num_one ** num_two
# 11
floor_division = num_one // num_two
# 12
rad = 30
pi = 3.14
area_of_circle = pi * 30 ** 2
radius = input("Please input the radius: ")
circum_of_circle = 2 * pi * int(radius)
print (circum_of_circle)

# 13
user_name = input("Please enter your first name: ")
user_last = input("Please enter your last name: ")
user_country = input("Please input your country: ")
user_age = input("Please input your age: ")