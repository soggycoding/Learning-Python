from re import sub
from collections import abc
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercise 1:
it_len = len(it_companies)
print(it_len)
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['GMA', 'ABSCBN', 'TV5'])
print(it_companies)
it_companies.remove('GMA')
print(it_companies)

# Exercise 2:
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
AB = A.union(B)
BA = B.union(A)
print(AB)
print(BA)
print(A.symmetric_difference(B))
del A
del B

# Exercise 3:
age_set = set(age)
print(len(age) >= len(age_set))
print(len(age) <= len(age_set))
'''
2. Explain the difference between the following data types: string, list, tuple, and set
- String = sequence of characters
- List = Sequence of items that are changeable
- tuple = Sequence of items that is not changeable
- set = Sequence of items that are changeable and has no duplicates
'''
sentence = "I am a teacher and I love to inspire and teach people."
print(list(sentence.split()))
