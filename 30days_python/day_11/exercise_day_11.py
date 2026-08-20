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
def check_season(month):
    if month == ["March","April","May"]:
        return "The season is Spring"
    if month == ["June","July","August"]:
        return "The season is Summer"
    if month == ["September","November","October"]:
        return "The season is Autumn"
    if month == ["December","January"," February"]:
        return "The season is Winter"
check_season("December")