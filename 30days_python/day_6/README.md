# Tuples
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable(mutable), unlike list, tuple has few methods. 

- tuple(): to create an empty tuple
- count() : to count the number of a specified item in a tuple
- index() : to find the index of a specified item in a tuple
+ operator : to join two or more tuples and to create a new tuple

## Positive indexing similar to the list data type we use positive or negative indexing to access tuple items.
```python
tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
first_item = tpl[0]
second_item = tpl[1]
last_index = len(tpl) - 1
last_item = tpl[last_index]
```

## Negative Indexing - means beginning from the end, -1 refers to the last item, -2 refers to the second last and the negative of the list/tuple length refers to the first item
```python
tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
first_item = tpl[-1]
second_item = tpl[-2]
last_index = len(tpl) - 1
last_item = tpl[last_index]
```

## Slicing tuples - We can slice out a sub-tuple by specifying range of indexes where to start and where to end in a tuple, the return value will be a new tuple with the specified items.

# Changing Tuples to lists - We can change tuples to list