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

# =======================================================
# DAY 11 - PASS 2: ALTERNATIVE EXPLORATION
# Exercise: sum_of_odds
# =======================================================
# Your Pass 1 baseline worked using modulo checking (i % 2)!
#
# PASS 2 CHALLENGE & RANGE POWER:
#
# 1. The Step Parameter in range():
#    - `range(start, stop, step)` can skip even numbers entirely:
#      `range(1, num + 1, 2)` -> yields 1, 3, 5, 7...
#    - No `if / else` condition needed!
#
# 2. Pythonic sum() with range step:
#    - `return sum(range(1, num + 1, 2))`
#
# 3. Direct Modulo Condition:
#    - Instead of `if i % 2 == 0: pass else:`, write:
#      `if i % 2 != 0: num_plus += i`
#
# Write your alternative implementation below:

def sum_of_odds(num):
    odd_sum = 0
    for i in range(1, num + 1, 2):
        print(i)
        return i
print(sum_of_odds(7))