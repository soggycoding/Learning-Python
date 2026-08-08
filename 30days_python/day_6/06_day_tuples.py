# Creating a tuple
## Empty tuple
import types
from _typeshed import _type_checker_internals
empty_tuple =()
empty_tuple = tuple()

# Tuple with initial values
tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

# Tuple length
## We can use the len() method to get the length of a tuple
tpl = ('item1', 'item2', 'item3')
len(tpl)

# Accessing Tuple Items
## Positive Indexing
tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
first_item = tpl[0]
second_item = tpl[1]
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

## Negative indexing
tpl = ('item1', 'item2', 'item3', 'item4')
first_item = tpl[-4]
second_item = tpl[-3]
fruits = ['banana', 'ornage', 'mango', 'lemon']
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

# Slicing tuples
## Range of Positive Indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]
all_items = tpl[0:]
middle_two_items = tpl[1:3]

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_mango = fruits[1:3]
orange_to_the_rest = fruits[1:]

## Range of Negative Indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]
middle_two_items = tpl[-3:-1]

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]
middle_two_fruits = fruits[-3:-1]

# Convert tuple to list
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)
fruits = tuple(fruits)
print(fruits)

# Checking an item in a tuple
tpl = ('item1', 'item2', 'item3', 'item4')
'item2' in tpl

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)
fruits[0] = 'apple'

# Joining Tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

# Deleting Tuples
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits