'''
def reverse_list(*items):
    for item in items[::-1]:
        print(item)

reverse_list('Bing', 'Bong', 'Boop', 'Bloop')
'''

'''
def capitalize_list_items(*items):
    return [str(item).upper() for item in items]

print(capitalize_list_items("bing", 'bong', 'boop'))
'''

'''
def add_item(item_list, item):
    item_list.append(item)
    return item_list

print(add_item(['iiting', 'biting'], 'wingwing'))
'''

'''
def remove_item(item_list, item):
    if item not in item_list:
        return "Item not in list"
    else:
        item = str(item)
        item_list.remove(item)
        return item_list

item_list = ['Banana', 'Apple', 'Mangga']
print(remove_item(item_list, 'Mangga'))
'''

'''
def sum_of_numbers(num):
    return (num * (num + 1)) // 2

print(sum_of_numbers(10))
'''

'''
def sum_of_odds(num):
    return sum(range(1, num + 1, 2))

print(sum_of_odds(5))
'''

'''
def sum_of_even(num):
    k = num // 2
    return k * (k + 1)

print(sum_of_even(5))
'''

'''
def evens_and_odds(num):
    even_counter = (num // 2) + 1
    odd_counter = (num + 1) // 2
    return f"Even numbers: {even_counter} \nOdd numbers: {odd_counter}"

print(evens_and_odds(100))
'''