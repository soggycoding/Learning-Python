# List
There are four collection data types in Python:
- List is a collection which is ordere and changeable(modifiable), Allows duplicate members.
- Tuple : is a collection which is ordered and unchangeable or unmodifieable, but we can add new items to the set. Duplicate members are not allowed.
- Dictionary : is a collection which is unordered, changeable and indexed. No duplicate members.

A list is a collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

## Slicing items from a list
Positive Indexing: WE can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list.
(default values for start = 0, end len(lst) - 1 (last item), step = 1)

Negative Indexing: We cab specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.

## Modifying lists
List is a mutable or modifiable ordered collection of items.

## Checking items in a list
Checking an item if it is a member of a list using in operator

## Adding items to a list
To add item to the end of an existing list we use the method append()

## Inserting items into a list
We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. THe insert() methods takes two arguments:index and an item to insert

## Removing items from a list
The remove method removes a specified item from a list

## Removing items using del
The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely

## Clearing list items
The clear() method empties the list:

## Copying a list
It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. Now, list2 is a reference of list1, any changes we make in list 2 will also be modify the original, list1. But there are lots of case in which we do not like to modify the original insteadwe like to have a different copy. One way of avoiding the problem above is using copy().

## Joining Lists
there are several ways to join, or concatenate, two or more lists in python.

## Counting items in a list
The count() method returns the number of times an item appears in a list

## Finding Index of an item
The index() method returns the index of an item in the list

## Reversing a list
The reverse() method reverses the order of a list

# Sorting list items
To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.