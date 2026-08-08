# Dictionaries

# Creating a dictionary
empty_dict = {}
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3', 'key4' : 'value4'}

person = {
    'first_name' : 'Soggy',
    'last_name' : 'Waggy',
    'age' : 24,
    'is_married': False,
    'skills': ['JavaScript', 'Python'],
    'address': {
        'street' : 'Bahay ko',
        'zipcode' : '2210'
    }
}

# Dictionary length

dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3', 'key4' : 'value4'}
print(len(dct))

print(len(person))

# Accessing Dictionary Items
## We can access Dictionary items by referring to its key name

dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3', 'key4' : 'value4'}
print(dct['key1'])
print(dct['key2'])

print(person['first_name'])
print(person['last_name'])
print(person['skills'])
print(person['address'])
print(person['address']['zipcode'])

# Using get() method
## Accessing an item by using get() method does not raise an error if the key does not exist. It returns None by default

print(person.get('first_name'))
print(person.get('skills'))
print(person.get('address'))
print(person.get('address')['zipcode'])
print(person.get('non_existent_key'))

# Adding Items to a dictionary
## We can add items to a dictionary by referring to its key name
dct = {'key1' : 'value1', 'key2' : 'value2'}
dct['key3'] = 'value3'
print(dct)

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

# Modifying Items in a dictionary
## We can modify items in a dictionary

dct = {'key1' : 'value1', 'key2' : 'value2'}
dct['key1'] = 'value-one'

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Ethiopia',
    'is_marred': False,
    'skills': ['Java', 'C++', 'JavaScript'],
    'address': {
        'street': 'Feeling Awesome street',
        'zipcode': '0000'
    }
}

person['first_name'] = 'Eyob'
person['age'] = 252

# Checking keys in a dictionary
## We use the in operator to check if a key exist in a dictionary

dct = {'key1' : 'value1', 'key2' : 'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct)
print('key5' in dct)

# Removing key and value pairs from a dictionary
## pop(key): removes the item with the specified key name
## popitem(): removes the last item
## del: removes an item with specified key name

dct.pop('key1')
dct.popitem()
del dct['key2']

person = {
    'name': 'John', 
    'age': 30,
    'city': 'New York'
}
person.pop('name')
person.popitem()
del person['age']
print(person)

# Changing Dictionary to a list of items
## The items() method changes dictionary to a list of tuples

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())

# Clearing a dictionary
## If we don't want the items in a dictionary we can clear them using clear() method

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.clear()
print(dct)

# Deleting a dictionary
## We can use del to delete a dictionary

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copy a dictionary
## We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.copyright

dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
dct_copy = dct.copy()

# Getting Dictionary Keys as a List
## The keys() method returns the keys of a dictionary as a list

dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
keys = dct.keys()
print(keys)

# Getting Dictionary Values as a List
## The values() method returns the values of a dictionary as a list

dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
values = dct.values()
print(values)
