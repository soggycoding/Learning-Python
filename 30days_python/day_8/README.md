# Day 8: Dictionaries

A dictionary is a collection of unordered, changeable (mutable), and paired (`key: value`) data types.

## Creating a Dictionary
To create an empty dictionary, we can use empty curly brackets `{}` or the `dict()` built-in function:

```python
# Empty dictionary
empty_dict = {}
# or
empty_dict = dict()
```

Dictionary with initial values:

```python
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
```

## Dictionary Length
Checks the number of `key: value` pairs in the dictionary using `len()`:

```python
len(person)
```

## Accessing Dictionary Items
We can access dictionary items by referring to their key name inside square brackets `[]` or using the `get()` method. The `get()` method returns `None` if the key does not exist instead of raising a `KeyError`.

```python
person['first_name']  # 'Asabeneh'
person.get('country') # 'Finland'
```

## Adding Items to a Dictionary
We can add new key and value pairs to a dictionary by assigning a value to a new key:

```python
person['job'] = 'Instructor'
person['skills'].append('HTML')
```

## Modifying Items in a Dictionary
We can modify existing items by reassigning a new value to an existing key:

```python
dct = {'key1': 'value1', 'key2': 'value2'}
dct['key1'] = 'value-one'

person['first_name'] = 'Eyob'
person['age'] = 252
```

## Checking Keys in a Dictionary
We use the `in` operator to check if a key exists in a dictionary:

```python
print('first_name' in person) # True
print('gender' in person)     # False
```

## Removing Key and Value Pairs
- `pop(key)`: Removes the item with the specified key name.
- `popitem()`: Removes the last item inserted into the dictionary.
- `del`: Removes an item with a specified key name or deletes the dictionary completely.

```python
person.pop('first_name') # Removes 'first_name' key
person.popitem()        # Removes last item
del person['is_marred'] # Removes 'is_marred' key
```

## Changing Dictionary to a List of Items
The `items()` method converts a dictionary to a list of `(key, value)` tuples:

```python
person.items()
```

## Copying a Dictionary
We can copy a dictionary using the `copy()` method to avoid modifying the original dictionary:

```python
person_copy = person.copy()
```

## Getting Dictionary Keys as a List
The `keys()` method gets all keys in a dictionary as a list:

```python
keys = person.keys()
```

## Getting Dictionary Values as a List
The `values()` method gets all values in a dictionary as a list:

```python
values = person.values()
```

## Clearing a Dictionary
The `clear()` method empties the dictionary:

```python
person.clear() # {}
```

## Deleting a Dictionary
The `del` statement deletes the dictionary completely:

```python
del person
```