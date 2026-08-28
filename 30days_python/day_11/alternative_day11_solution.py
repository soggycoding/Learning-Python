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

# =======================================================
# DAY 11 - PASS 2: ALTERNATIVE EXPLORATION
# Exercise: factorial
# =======================================================
# Your Pass 1 baseline worked by counting down and shifting i - 1!
#
# PASS 2 CHALLENGE: CLEAN ACCUMULATION & RECURSION
#
# Explore these two foundational programming paradigms:
#
# 1. Forward Accumulation (Clean & handles 0! = 1):
#    - Initialize an accumulator to 1: `acc = 1`
#    - Iterate forward from 1 to `n`: `for x in range(1, n + 1):`
#    - Multiply in place: `acc *= x`
#
# 2. Recursion (Function calling itself):
#    - Base case: If input is 0 or 1, return 1.
#    - Recursive step: return input * function_name(input - 1)
#    - e.g. f(6) = 6 * f(5) = 6 * 5 * f(4) ...
#
# 3. Edge Case Stress Test:
#    - What does your function return for input = 0? (Mathematically 0! = 1).
#
# Write your alternative implementation below:
