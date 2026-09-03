# Functions Exercises - Day 11

'''
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(21, 31))

def area_of_circle(r):
    PI = 3.14
    area = PI * (r ** 2)
    return area
print(area_of_circle(10))
'''

'''
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            print(f"Argument {num} is not a valid number")
            return None
        total += num 
    return total
print(add_all_nums(23, 24, 26))
'''

'''
def convert_celcius_to_fahrenheit(celc):
    fahrenheit = (celc * 9 / 5) + 32
    return fahrenheit
print(convert_celcius_to_fahrenheit(24))
'''

'''
def check_season(month):
    month = month.capitalize()
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August'] 
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    if month in spring:
        return "Spring"
    if month in summer:
        return "Summer"
    if month in autumn:
        return "Autumn"
    if month in winter:
        return "Winter"
    return "Invalid month"

print(check_season("February"))
'''

'''
def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(2, 5, 10, 1))
'''

'''
import math

def solve_quadratic_eqn(a, b, c):
    # ax^2 + bx + c = 0 -> x = (-b ± sqrt(b^2 - 4ac)) / 2a
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "No real roots"

print(solve_quadratic_eqn(1, -5, 6))
'''

'''
def print_list(*items):
    for element in items:
        print(element)
print_list('potato', 'banana', 'hotdog', 'bente', 'wiowiwi')
'''

'''
def reverse_list(*items):
    item_list = []
    for item in items:
        item_list.append(item)
    item_list.reverse()
    return item_list

print(reverse_list('bing', 'bong', 'doot', 'bloop'))
'''

'''
def capitalize_list_items(*items):
    #item_list = []
    for item in items:
        #item_upper = item.upper()
        item = str(item)
        item = item.upper()
        print(item)
capitalize_list_items('bing', 'bong', 'boop')
'''

'''
def add_item(item_list, item):
    item = str(item)
    item_list.append(item)
    return item_list
item_list = ['Potato', 'Tomato', 'Brotato']
print(add_item(item_list, 'Bed'))
'''

'''
def remove_item(item_list, item):
    item_list.remove(item)
    return item_list
print(remove_item(['Bing', 'Bong', 'Boop'], 'Bong'))
'''

'''
def sum_of_numbers(num):
    num = int(num)
    num_plus = 0
    for i in range(0,num):
        i = i + 1
        num_plus = num_plus + i
    return num_plus
print(sum_of_numbers(10))
'''

'''
def sum_of_odds(num):
    num_plus = 0
    for i in range(0,num + 1):
        if i % 2 == 0: 
            pass
        else:
            num_plus = num_plus + i
    return num_plus
print(sum_of_odds(5))
'''

'''
def sum_of_even(num):
    return sum(range(2, num + 1, 2))
print(sum_of_even(5))
'''

# Exercise 2:

'''
def evens_and_odds(num):
    even = 0
    odds = 0
    for i in range (0, num + 1):
        if i % 2 == 0:
            even += 1
        else:
            odds += 1
    result_even = "The number of even numbers are"
    result_odds = "The number of odd numbers are"
    return {result_even: even, 
            result_odds: odds}
print(evens_and_odds(100))
'''

'''
def factorial(num):
    fact = num
    for i in range(num, 1, -1):
        i = i - 1
        fact = fact * i
    return fact
print(factorial(6))
'''

'''
def is_empty(param):
    if len(param) == 0:
        return "empty parameter"
    else:
        return "parameter has value"
print(is_empty([]))
'''

'''
def calculate_mean(num):
    sort_number = sorted(num)
    acc = 0
    for i in sort_number:
        acc += i
    return acc / len(sort_number)
print(calculate_mean([1, 2]))
'''


'''
def calculate_median(num):
    sorted_num = sorted(num)
    n = len(sorted_num)
    if n % 2 != 0:
        return sorted_num[n // 2]
    else:
        middle1 = sorted_num[(n // 2) - 1]
        middle2 = sorted_num[n // 2]
        return (middle1 + middle2) / 2
print(calculate_median([1, 2, 3 ,4]))
'''


import math

def calculate_mode(nums):
    d = {}
    count = 0
    num_count = 0
    list_item = []
    item_counter = []
    for i in nums:
        d = ({"item" : i, "count" : count + 1})
        count += 1
        d.append(d)
    return d
print(calculate_mode([1, 2, 2, 3, 4]))
'''
        list_item.append(d)
    for item in list_item:
        if ["item"] in item.values():
            return item
        num_count += 1
        item_counter.append(item)
    return item_counter
print(calculate_mode([1, 2, 2, 3, 4]))

        if item["item"] == 1:
            if item in item_counter:
                return item['item']
            item_counter.append(item)
        elif item["item"] == 2:
            if item.values() in item_counter:
                return item['item']
            item_counter.append(item)
        elif item["item"] == 3:
            if item in item_counter:
                return item['item']
            item_counter.append(item)
        elif item["item"] == 4:
            if item in item_counter:
                return item['item']
            item_counter.append(item)
        else:
            pass
'''


'''
def calculate_range(list_of_number):
    number_range = max(list_of_number) - min(list_of_number)
    return number_range
print(calculate_range([1, 2, 3, 4]))
'''
'''
def calculate_variance(num):
    mean = sum(num) / len(num)
    total_sum = 0
    for i in num:
        total_sum += (i - mean)**2
    variance = (total_sum / len(num))
    return variance
print(calculate_variance([1,2,3]))
'''