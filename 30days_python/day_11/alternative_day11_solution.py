'''
def reverse_list(*items):
    for item in items[::-1]:
        print(item)

reverse_list('bing', 'bong', 'doot', 'bloop')
'''

'''
def capitalize_list_items(*items):
    item_list = []
    for item in items:
        if isinstance(item, int):
            pass
        else:
            item = str(item)
            item_upper = item.upper()
            item_list.append(item_upper)
    return item_list

# def capitalize_list_items(*items):
#     return [str(item).upper() for item in items]

print(capitalize_list_items('bong', 'beep', 'bloop'))
'''

'''
def add_item(item_list, item):
    item = str(item)
    item_list.insert(1, item)
    return item_list
item_list = ['Bing', 'Bong', 'Boom']
print(add_item(item_list, 'Bagang'))

def add_number(number_list, num):
    num = int(num)
    number_list.append(num)
    return number_list
number_list = [ 3, 4, 5]
print(add_number(number_list, 7))
'''

'''
def remove_item(item_list, item):
    if item in item_list:
        item_list.remove(item)
        return item_list
    else:
        return "Item not found"

print(remove_item(['Bing', 'Bong', 'Bloop'], 'Bloop'))
'''

'''
def sum_of_numbers(num):
    num_plus = 0
    for i in range(1, num + 1):
        num_plus += i
    return num_plus

print(sum_of_numbers(5))
'''

'''
def sum_of_odds(num):
    return sum(range(1, num + 1, 2))

print(sum_of_odds(5))
'''

'''
def sum_of_even(num):
    return sum(range(2, num + 1, 2))

print(sum_of_even(5))
'''

'''
def evens_and_odds(num):
    even_count = (num // 2) + 1
    odd_count = (num + 1) // 2
    return f"The number of even numbers are: {even_count}\nThe number of odd numbers are: {odd_count}"

print(evens_and_odds(100))
'''

'''
def factorial(num):
    acc = 1
    for i in range(1, num + 1):
        acc *= i
    return acc

print(factorial(6))
print(factorial(0))
'''

'''
def is_empty(param=None):
    if param is None:
        return True
    return len(param) == 0

print(is_empty(None))
print(is_empty([]))
print(is_empty(['apple']))
'''

'''
def calculate_mean(num):
    return sum(num) / len(num)

print(calculate_mean([25, 55, 35]))
'''

'''
# Pattern 1: Standard Library
import statistics

def calculate_median(arr):
    return statistics.median(arr)

# Pattern 2: Manual Ternary One-Liner
def calculate_median_ternary(arr):
    s = sorted(arr)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 != 0 else (s[mid - 1] + s[mid]) / 2

print(calculate_median([1, 4, 2]))
print(calculate_median_ternary([1, 2, 3, 4]))
'''

'''
def calculate_range(nums):
    if not nums:
        return "Empty"
    return max(nums) - min(nums)

print(calculate_range([]))
print(calculate_range([1, 2, 3, 4]))
'''

'''
# Pattern 1: Generator Expression
def calculate_variance(num):
    mean = sum(num) / len(num)
    return sum((i - mean) ** 2 for i in num) / len(num)

# Pattern 2: Built-in Statistics
import statistics
def calculate_variance_lib(num):
    return statistics.pvariance(num)

print(calculate_variance([1, 2, 3]))
'''

'''
import statistics
def calculate_mode(nums):
    return statistics.multimode(nums) # Can tally up multiple modes
    #return statistics.mode(nums) # Can tally up to one only
print(calculate_mode([1,2,2,3,4,4,3,5,6,7,8]))
'''
'''
import collections
def calculate_mode(nums):
    c = collections.Counter(nums) # Tally up the code into a one liner without the only result itself
    return c.most_common(1) # Returns specific tally
print(calculate_mode([1,2,3,3,4]))
'''
'''
import collections
def calculate_mode(nums):
    c = collections.Counter(nums)
    return max(c,key=c.get) # Gets the highest number tallied 
print(calculate_mode([1,2,3,3,4]))
'''

'''
import statistics
def calculate_std(nums):
    # std = statistics.pstdev(nums) # Divides by count of items in list then raise the result to the power of 0.5
    std = statistics.stdev(nums) # divides the sum by n-1
    return std
print(calculate_std([1,2,3]))
'''

'''
def calculate_variance(nums):
    mean = sum(nums) / len(nums)
    var = 0
    for i in nums:
        x = (i - mean)**2
        var += x
    total = var / len(nums)
    return total

def calculate_std(nums):
    return calculate_variance(nums) ** 0.5

print(calculate_std([1,2,3]))
'''

'''
def greet(name="Guest"):
    #print(f"Welcome, {name or 'Guest'}!") # Short circuting Idiom
    resolved = name or "Guest"
    print(f"Welcome, {resolved}!")
greet()
'''

'''
def show_args(**user):
    if not user:
        return "No arguments received"
    return "Received: " + ", ".join(f"{k}: {v}" for k, v in user.items())
print(show_args(name="Soggy", age=23, city="Bingbong"))
'''

'''
def is_prime(num):
    if num <= 1:
        return False
    limit = int(num ** 0.5) + 1
    return all(num % i != 0 for i in range(2, limit))
print(is_prime(15))
'''

'''
def check_unique(items):
    # return len(items) == len(set(items)) # Alternative Pattern 1
    tracker = set()
    for item in items:
        if item in tracker:
            return False
        tracker.add(item)
    return True
print(check_unique([1,2,3,4,4]))
'''

# =====================================================================
# STAGE 2: ALTERNATIVE EXPLORATION - same_data_type
# =====================================================================
# Goal: Short-Circuiting Generators vs. Set Comprehensions & Big-O Analysis.
#
# Big-O Complexity Analysis:
# - Baseline:
#   * Guard clause + loop checking type(val) != ref.
#   * Time Complexity: O(N) worst-case, O(1) best-case (early return on first mismatch).
#   * Space Complexity: O(1) auxiliary space.
#
# - Alternative Pattern 1: Generator Expression with all(...)
#   * Extract reference type, then evaluate equality lazily:
#   * all(type(val) == ref for val in seq)
#   * Time Complexity: O(N) worst-case, O(1) best-case (stops on first mismatch).
#   * Space Complexity: O(1).
#
# - Alternative Pattern 2: Set Comprehension of Types (The 1-Liner)
#   * Concept: A set comprehension collapses duplicate elements.
#   * What happens if you collect the type of every element into a set: {type(val) for val in seq}?
#     - If all items share the exact same type: len(types_set) is 1.
#     - If the list is empty: len(types_set) is 0.
#     - If items have mixed types: len(types_set) >= 2.
#   * Condition: len({type(val) for val in seq}) <= 1
#   * Time Complexity: O(N) (must evaluate the full list to construct the set).
#   * Trade-off: Extremely concise, handles empty list without guard clauses, but does not early-exit.
#
# Task:
# 1. Implement same_data_type using the set comprehension pattern (len(...) <= 1).
# 2. Implement same_data_type using all(...).
# 3. Test both against the Adversarial Test Matrix with Ctrl+F5.
#
# ADVERSARIAL TEST MATRIX:
# 1. Standard Cases:
#    same_data_type([1, 2, 3, 4])     -> True
#    same_data_type(['a', 'b', 'c'])   -> True
#    same_data_type([1, 'two', 3])     -> False (mixed int and str)
# 2. Boundary Cases:
#    same_data_type([])                -> True  (empty list)
#    same_data_type([3.14])            -> True  (single element)
# 3. Trap Cases:
#    same_data_type([1, 1.0, 2])       -> False (int vs float)
#    same_data_type([1, True, 0])      -> False (int vs bool)

'''
# Pattern 1: Set Comprehension (Pure 1-liner, zero guard clauses needed)
def same_data_type(data):
    return len({type(val) for val in data}) <= 1

# Pattern 2: Generator Expression with all() (Short-circuiting O(1) best case)
def same_data_type(data):
    if not data:
        return True
    ref = type(data[0])
    return all(type(val) == ref for val in data)

print(same_data_type([1, 2, 3]))
print(same_data_type([1, '2', 3]))
print(same_data_type([]))
'''