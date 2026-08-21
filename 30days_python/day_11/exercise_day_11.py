# Functions
'''
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(21,31))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** r
    return area
print(area_of_circle(10))
'''
'''
        def add_all_nums(*num):
            total = 0
            for nums in num:
                if nums != int:
                    print("Arguement is not equal to int")
                total += nums 
            return total
        print(add_all_nums(23,24,26))
'''
'''
def convert_celcius_to_fahrenheit(celc):
    fahrenheit = (celc * 9 / 5) + 32
    return fahrenheit
print(convert_celcius_to_fahrenheit(24))
'''
'''
def check_season(month):
    spring = ['March', 'April', 'May']
    summer =['June', 'July', 'August'] 
    autumn = ['September', 'October', 'November']
    winter =  ['December', 'January', 'February']
    if month in spring:
        return print("The season is Spring")
    if month in summer:
        return print("The season is Summer")
    if month in autumn:
        return print("The season is Autumn")
    if month in winter:
        return print("The season is Winter")

check_season("February")
'''
'''
def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return print(slope)
calculate_slope(2, 5, 10, 1)
'''
'''
        def solve_quadratic_eqn(a,b,c):
            quadratic = a*1**2 + b*1 + c
            return print(quadratic)
        solve_quadratic_eqn(-2,2,1)
'''
'''
def print_list(*items):
    for elements in items:
        print(elements)
print_list('potato', 'banana', 'hotdog', 'bente', 'wiowiwi')
'''
def reverse_list(*items):
