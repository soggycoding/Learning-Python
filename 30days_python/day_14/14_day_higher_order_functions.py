# Day 14: Higher Order Functions, Closures & Decorators - Interactive Walkthrough

import functools
import time

# ==============================================================================
# SECTION 1: Functions as First-Class Citizens
# ==============================================================================
# In Python, functions can be assigned to variables, passed as arguments,
# and returned from other functions just like any other object.

# Example 1A: Passing a function as a parameter (Callback Pattern)
def apply_operation(func, values):
    """Higher order function that applies `func` to every item in `values`."""
    return [func(x) for x in values]

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

numbers = [1, 2, 3, 4, 5]
print("1A. Applying square:", apply_operation(square, numbers))
print("1A. Applying cube:  ", apply_operation(cube, numbers))


# Example 1B: Function as a return value (Function Factory)
def create_greeting(salutation):
    """Returns a customized greeting function."""
    def greet(name):
        return f"{salutation}, {name}!"
    return greet

formal_greeting = create_greeting("Good evening")
casual_greeting = create_greeting("Hey there")

print("\n1B. Formal:", formal_greeting("Alice"))
print("1B. Casual:", casual_greeting("Bob"))


# ==============================================================================
# SECTION 2: Python Closures & Encapsulated State
# ==============================================================================
# A closure remembers values from its enclosing lexical scope even after
# the outer function has completed execution.

def make_counter(start=0, step=1):
    """Creates a stateful counter function using closure and `nonlocal`."""
    current = start

    def next_val():
        nonlocal current  # Bind to outer scope variable
        current += step
        return current

    return next_val

counter_by_1 = make_counter(start=0, step=1)
counter_by_5 = make_counter(start=100, step=5)

print("\n2. Counter by 1 (call 1):", counter_by_1())
print("2. Counter by 1 (call 2):", counter_by_1())
print("2. Counter by 5 (call 1):", counter_by_5())
print("2. Counter by 5 (call 2):", counter_by_5())


# ==============================================================================
# SECTION 3: Decorators Fundamentals
# ==============================================================================
# A decorator wraps another function to extend its behavior non-invasively.

# Example 3A: Basic Decorator with *args, **kwargs and functools.wraps
def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_output = func(*args, **kwargs)
        if isinstance(original_output, str):
            return original_output.upper()
        return original_output
    return wrapper

@uppercase_decorator
def get_welcome_message(name):
    """Returns a greeting message."""
    return f"welcome to python, {name}"

print("\n3A. Decorated message:", get_welcome_message("jethro"))
print("3A. Preserved metadata - name:", get_welcome_message.__name__)
print("3A. Preserved metadata - doc: ", get_welcome_message.__doc__)


# ==============================================================================
# SECTION 4: Stacking / Chaining Multiple Decorators
# ==============================================================================
# Decorators execute from the bottom up (inside-out).

def bracket_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"[{func(*args, **kwargs)}]"
    return wrapper

def exclamation_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"{func(*args, **kwargs)}!"
    return wrapper

# exclamation_decorator runs first, then bracket_decorator wraps around it
@bracket_decorator
@exclamation_decorator
def shout_word(word):
    return word

print("\n4. Chained decorators:", shout_word("SUCCESS"))


# ==============================================================================
# SECTION 5: Decorators Accepting Arguments (Decorator Factories)
# ==============================================================================
# 3 nested functions: factory(params) -> decorator(func) -> wrapper(*args, **kwargs)

def repeat(times):
    """Decorator factory repeating function execution `times` times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_result = None
            for i in range(times):
                last_result = func(*args, **kwargs)
            return last_result
        return wrapper
    return decorator

@repeat(times=3)
def log_heartbeat(service_name):
    print(f"   [Heartbeat] Service '{service_name}' is healthy.")

print("\n5. Executing @repeat(times=3):")
log_heartbeat("auth-service")


# ==============================================================================
# SECTION 6: Practical Engineering Decorators
# ==============================================================================

# Example 6A: Execution Timer Decorator
def time_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"   [Profiler] '{func.__name__}' took {duration:.6f} seconds.")
        return result
    return wrapper

@time_execution
def compute_sum_of_squares(n):
    return sum(i ** 2 for i in range(n))

print("\n6A. Performance Profiling:")
total_squares = compute_sum_of_squares(100_000)
print("    Result:", total_squares)


# ==============================================================================
# SECTION 7: Built-in Higher Order Functions: map()
# ==============================================================================
# map(func, iterable) returns a lazy iterator. Wrap in list() to materialize.

raw_numbers = ["10", "20", "30", "40", "50"]

# 7A: Mapping with built-in type caster
integers = list(map(int, raw_numbers))
print("\n7A. map(int, str_list):", integers)

# 7B: Mapping with lambda transformation
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: round((c * 9/5) + 32, 1), celsius))
print("7B. Celsius to Fahrenheit:", fahrenheit)

# 7C: Mapping across multiple iterables in parallel
base_nums = [2, 3, 4]
powers = [3, 2, 2]
power_results = list(map(pow, base_nums, powers))  # 2^3, 3^2, 4^2
print("7C. map(pow, bases, powers):", power_results)


# ==============================================================================
# SECTION 8: Built-in Higher Order Functions: filter()
# ==============================================================================
# filter(predicate_func, iterable) keeps items where predicate evaluates to True.

mixed_data = [-10, 15, 0, -3, 42, -99, 8]

# 8A: Filter positive numbers
positives = list(filter(lambda x: x > 0, mixed_data))
print("\n8A. Filter positives:", positives)

# 8B: Filtering string elements by condition
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
land_countries = list(filter(lambda c: 'land' in c, countries))
print("8B. Countries containing 'land':", land_countries)

# 8C: Using None as predicate (filters out falsy values: 0, "", False, None, etc.)
sparse_list = ["apple", "", None, 0, "banana", False, 42]
truthy_values = list(filter(None, sparse_list))
print("8C. filter(None, ...):", truthy_values)


# ==============================================================================
# SECTION 9: Built-in Higher Order Functions: functools.reduce()
# ==============================================================================
# reduce(func, iterable[, initializer]) folds an iterable down into a single scalar value.

seq = [1, 2, 3, 4, 5]

# 9A: Cumulative Product
product = functools.reduce(lambda acc, x: acc * x, seq)
print("\n9A. Cumulative product:", product)

# 9B: Finding Maximum Value via reduce
find_max = functools.reduce(lambda a, b: a if a > b else b, [45, 12, 89, 34, 76])
print("9B. Maximum via reduce:", find_max)

# 9C: Reducing strings into a formatted sentence
words = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# Join items into a comma-delimited sentence
sentence = functools.reduce(lambda acc, curr: f"{acc}, {curr}", words)
print("9C. Formatted string reduction:", sentence)
