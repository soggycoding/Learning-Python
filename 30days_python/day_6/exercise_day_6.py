# Exercise 1:

# Create an empty tuple
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

tpl = ()
brothers = ('ben', 'bong', 'boop')
sisters = ('soraka', 'rafaela', 'lucy')
siblings = brothers + sisters
print(len(siblings))
parents = ('beep', 'boop')
family_members = siblings + parents
print(family_members)

# Exercise 2:

# Unpack siblings and parents from family_members
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# Change the about food_stuff_tp tuple to a food_stuff_lt list
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_stuff_lt list
# Delete the food_stuff_tp tuple completely
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country

bn, bng, bp, srk, rfl, lcy, *rst = parents = family_members
print(family_members)
fruits = ('Lemon', 'Mango', 'Banana')
vegetables = ('Potato', 'Carrot', 'Onion')
animal_products = ('Monkey', 'Cow', 'Cat')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
middle_item = food_stuff_lt[::2]
print(middle_item)
frst_three_items = food_stuff_lt[0:3]
print(frst_three_items)
last_three_items = food_stuff_lt[-3:]
print(last_three_items)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print("Estonia is a nordic country")
else:
    print("Estonia is not a nordic country")

if 'Iceland' in nordic_countries:
    print('Iceland is a nordic country')
else:
    print('Iceland is not a nordic country')