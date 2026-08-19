# Functions
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(21,31))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** r
    return area
print(area_of_circle(10))

def add_all_nums(num):
    while num is int:
        num + num
        if num != int:
            print("A value is not an integer ")
            pass
print(add_all_nums(23))