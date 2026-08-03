# Creating a tuple
## Empty tuple
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