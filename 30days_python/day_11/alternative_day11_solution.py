'''
def reverse_list(*items):
    for item in items[::-1]:
        print(item)

reverse_list('bing', 'bong', 'doot', 'bloop')
'''

'''
def capitalize_list_items(*items):
    item_list = []
    for item in items:
        if isinstance(item, int):
            pass
        else:
            item = str(item)
            item_upper = item.upper()
            item_list.append(item_upper)
    return item_list

# def capitalize_list_items(*items):
#     return [str(item).upper() for item in items]

print(capitalize_list_items('bong', 'beep', 'bloop'))
'''

'''
def add_item(item_list, item):
    item = str(item)
    item_list.insert(1, item)
    return item_list
item_list = ['Bing', 'Bong', 'Boom']
print(add_item(item_list, 'Bagang'))

def add_number(number_list, num):
    num = int(num)
    number_list.append(num)
    return number_list
number_list = [ 3, 4, 5]
print(add_number(number_list, 7))
'''

'''
def remove_item(item_list, item):
    if item in item_list:
        item_list.remove(item)
        return item_list
    else:
        return "Item not found"

print(remove_item(['Bing', 'Bong', 'Bloop'], 'Bloop'))
'''

'''
def sum_of_numbers(num):
    num_plus = 0
    for i in range(1, num + 1):
        num_plus += i
    return num_plus

print(sum_of_numbers(5))
'''

'''
def sum_of_odds(num):
    return sum(range(1, num + 1, 2))

print(sum_of_odds(5))
'''

'''
def sum_of_even(num):
    return sum(range(2, num + 1, 2))

print(sum_of_even(5))
'''

'''
def evens_and_odds(num):
    even_count = (num // 2) + 1
    odd_count = (num + 1) // 2
    return f"The number of even numbers are: {even_count}\nThe number of odd numbers are: {odd_count}"

print(evens_and_odds(100))
'''

'''
def factorial(num):
    acc = 1
    for i in range(1, num + 1):
        acc *= i
    return acc

print(factorial(6))
print(factorial(0))
'''

'''
def is_empty(param=None):
    if param is None:
        return True
    return len(param) == 0

print(is_empty(None))
print(is_empty([]))
print(is_empty(['apple']))
'''

'''
def calculate_mean(num):
    return sum(num) / len(num)

print(calculate_mean([25, 55, 35]))
'''

'''
# Pattern 1: Standard Library
import statistics

def calculate_median(arr):
    return statistics.median(arr)

# Pattern 2: Manual Ternary One-Liner
def calculate_median_ternary(arr):
    s = sorted(arr)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 != 0 else (s[mid - 1] + s[mid]) / 2

print(calculate_median([1, 4, 2]))
print(calculate_median_ternary([1, 2, 3, 4]))
'''

'''
def calculate_range(nums):
    if not nums:
        return "Empty"
    return max(nums) - min(nums)

print(calculate_range([]))
print(calculate_range([1, 2, 3, 4]))
'''

'''
# Pattern 1: Generator Expression
def calculate_variance(num):
    mean = sum(num) / len(num)
    return sum((i - mean) ** 2 for i in num) / len(num)

# Pattern 2: Built-in Statistics
import statistics
def calculate_variance_lib(num):
    return statistics.pvariance(num)

print(calculate_variance([1, 2, 3]))
'''