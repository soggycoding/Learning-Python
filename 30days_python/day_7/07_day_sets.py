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
fruits.remove('lime')

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

fruits = {}