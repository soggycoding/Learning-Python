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