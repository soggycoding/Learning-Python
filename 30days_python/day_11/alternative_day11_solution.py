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

# =======================================================
# DAY 11 - PASS 2: ALTERNATIVE EXPLORATION
# Exercise: remove_item
# =======================================================
# Your Pass 1 baseline worked using .remove(item)!
#
# PASS 2 CHALLENGE & PYTHON MECHANICS:
#
# 1. The Missing Item Trap (ValueError):
#    - What happens if you run: `remove_item(['Apple', 'Banana'], 'Orange')`?
#    - Try wrapping your removal in `if item in item_list:` or `try/except ValueError`
#      so your program doesn't crash!
#
# 2. Single Occurrence vs. All Occurrences:
#    - `.remove()` only deletes the FIRST occurrence of an item.
#    - How can you remove ALL matching items if duplicates exist?
#      (Hint: List Comprehension -> `[x for x in item_list if x != item]`)
#
# 3. Removing by Index:
#    - Explore `.pop(index)` or `del item_list[index]` if you knew the index position.
#
# Write your alternative implementation below:

'''
def remove_item(item_list, item):
    if item in item_list:
        item_list.remove(item)
        return item_list
    else:
        return "Item not found"

print(remove_item(['Bing', 'Bong', 'Bloop'], 'Bloop'))
'''

def remove_item(item_list, item):
    for items in item_list:
        if items != item:
            item_list.remove(item)
            return item_list
        else:
            item_list.remove(item)
            return item_list
print(remove_item(['Bing', 'Bong', 'Bloop', 'Bloop'], 'Bloop'))