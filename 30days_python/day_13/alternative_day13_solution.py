# Exercise 1 (Pass 2): Functional Filtering (filter + lambda)
'''
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = list(filter(lambda x: x <= 0, numbers))
print(filtered)
'''

# Exercise 2 (Pass 2): Flattening with Recursion
'''
list_of_lists = [[[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]]]
def deep_flatten(element):
    flatten = []
    for item in element:
        if isinstance(item, list):
            flatten.extend(deep_flatten(item))
        else:
            flatten.append(item)
    return flatten
print(deep_flatten(list_of_lists))
'''

# Exercise 3 (Pass 2): Nested Dynamic Tuple Generation
'''
nested_dynamic_tuple = [(i,) + tuple(i**p for p in range(6)) for i in range(11)]
print(nested_dynamic_tuple)
'''

