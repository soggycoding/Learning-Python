'''
def apply_operation(func, val):
    return func(val)

def square(n):
    return n * n

result = apply_operation(square, 5)
print(result)
'''
'''
def apply_operation(func, lst):
    return func(lst)

def joining_list(value):
    return ' '.join(value)

result = apply_operation(joining_list, ['1', '2', '3', '4', '5'])
print(result)
'''

def make_multiplier(factor):
    # 'factor' is in the outer enclosing scope
    def multiply(n):
        return n * factor  # 'factor' is remembered here
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(2))  # 10 (remembers factor=2)
print(triple(5))  # 15 (remembers factor=3)
