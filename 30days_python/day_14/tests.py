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
'''
'''
import functools

def announce_execution(target_func):
    @functools.wraps(target_func)  # Critical: preserves original function metadata!
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing {target_func.__name__}...")
        result = target_func(*args, **kwargs)
        print(f"[LOG] {target_func.__name__} finished.")
        return result
    return wrapper

# Using @ syntax (syntactic sugar for: compute = announce_execution(compute))
@announce_execution
def compute(x, y):
    return x + y

print(compute(10, 20))
'''
print("Jonathan")
print("test")
    print("hello")