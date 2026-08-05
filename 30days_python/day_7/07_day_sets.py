# Sets
## Creating a set
st = set()
st = {'item1', 'item2', 'item3'}
fruits = {'banana', 'orange', 'mango', 'lemon'}

# Getting set's length
st = {'item1', 'item2', 'item3', 'item4'}
len(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)

# Accessing items in a set
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3?", 'item3' in st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)

# Adding items to a set

st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument

st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.update(['lime', 'orange', 'watermelon', 'grape'])

# Removing items from a set

st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.remove('lemon')

## If we are interested in the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()

# Clearing items in a set

st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)

## Deleting a set
st = {'item1', 'item2', 'item3', 'item4'}
del st

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# Converting list to set

lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)

fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)

# Joining sets
## Union this method returns a new set

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits.union(vegetables))
# Or use print(fruits | vegetables)

# Update this method inserts a set into a given set
st1.update(st2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# Finding Intersections Items
## Intersection returns a set of items which are in both the sets or using & symbol. 
st1 = {'items1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers)

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.intersection(dragon)

# Checking subset and super set
## A set can be a subset or super set of other sets
'''
subset: issubset()
super set: issuperset
'''

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1)
st1.issuperset(st2)

whole_numbers = {0, 1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)
whole_numbers.issuperset(even_numbers)

python.issubset(dragon)

# Checking the difference between two sets
## It returns the difference between two sets or using - symbols

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1)
st1.difference(st2)

whole_numbers = {0, 1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers)

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.difference(dragon)

# Finding symmetric difference between two sets
## It returns the items which are in either of the sets but not in both sets.

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.symmetric_difference(st1)

whole_numbers = {0, 1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.symmetric_difference(even_numbers)

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.symmetric_difference(dragon)

# Joining sets
## If two sets do not have a common item or items we call them disjoint sets. We can checkl if two sets are joint or disjoint using isdisjoint()

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.isdisjoint(st1)

whole_numbers = {0, 1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.isdisjoint(dragon)

