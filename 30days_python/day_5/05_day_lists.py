# Creating a list

lst = list()
empty_list = list()
print(len(empty_list))

lst = []
empty_list = []
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']

print('Fruits:', fruits)
print('Number of fruits: ', len(fruits))
print('Vegetables: ', vegetables)
print('Number of vegetables: ', len(vegetables))
print('Animal products: ', animal_products)
print('Number of animals: ', len(animal_products))

# List can have items of different data types
lst = ['Asabeneh', 250, True, {'country': 'Findland', 'city' : 'Helsinki'}]

 # Accessing list items using positive indexing
 
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)
# last index
last_index = len(fruits) -1
last_fruit = fruits[last_index]

# Accessing list items using negative indexing

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_fruit = fruits[-2]
print(first_fruit)
print(last_fruit)
print(second_fruit)

# Unpacking list items
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

# First Example
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)
# Second example about unpacking list
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)
# Third example about unpacking list
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Positive Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # Returns all the fruits
all_fruits = fruits[0:] # If we do not set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # Does not include the first index
orange_mango_lemon = fruits[1:] 
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item

# Negative Indexing
all_fruits = fruits[-4:] # It returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end
reverse_fruits = fruits[::-1] # Negative step will take the list in reverse order

# Modifying lists
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)

# Checking Items in a list
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime'
print(does_exist)

# Adding items to a list

'''lst = list()
lst.append()'''

fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

# Inserting items into a list

'''lst = ['item1', 'item2']
lst.insert(index, item)'''

fruits.insert(2, 'apple') # Insert apple between orange and mango
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

# Removing items from a list

'''lst = ['item1', 'item2']
lst.remove(item)'''

fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

# Removing Items using pop

''' lst = ['item1', 'item2]
del lst[index]
del lst '''

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3] # This deleted items between given indexes, so it does not delete the item with index 3!
print(fruits)
del fruits
print(fruits) # This should give: NameError: name 'fruits' is not defined

# Clearing list items
''' lst = ['item1', 'item2']
lst.clear()'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

# Copying a list
''' lst = ['item1', 'item2']
lst_copy = lst.copy()'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining lists
# list3 = list1 + list2

positive_number = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + positive_number
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegatables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veggies = fruits + vegetables
print(fruits_and_veggies)

# Joining using extend() method the extend() method allows to append list in a list.]
''' list1 = ['item1', 'item2]
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)'''

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers: ', num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_number = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_number)
print('Integers: ', negative_numbers)

# Counting items in a list
'''lst = ['item1', 'item2']
lst.count(item)'''

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = ['22', '19', '24', '25', '26',' 24', '25', '24']
print(ages.count(24))

# Finding index of an item
'''lst = ['item1', 'item2']
lst.index(item)'''

print(fruits.index('orange'))
print(ages.index(24))

# Reversing a list
'''lst = ['item1', 'item2']
lst.reverse()'''

fruits.reverse
print(fruits)
ages.reverse
print(ages)

# Sorting list items
# sort() modifies the original list
'''lst = ['item1', 'item2']
lst.sort()
lst.sort(reverse=True)'''

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

# sorted() returns the ordered list without modifying the original list
print(sorted(fruits))
# reverse order
fruits = sorted(fruits,reverse=True)
print(fruits)