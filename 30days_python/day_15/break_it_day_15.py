# Day 15: Break-It Challenges (Quick Error Recognition Tour)

# ==============================================================================
# How this file works
# ==============================================================================
# - Every snippet below WORKS as written.
# - Your goal: trigger each error once so you recognize it instantly when it
#   pops up in terminal or server logs.
# - No essays or formal templates. Just 1-2 quick sentences of what you noticed.
# - Work on ONE challenge at a time: remove the ''' ''', run it, test it,
#   then put the ''' ''' back and move to the next.
# ==============================================================================


# ==============================================================================
# Break-It 1: SyntaxError & IndentationError
# ==============================================================================
# What it is:
#   Python can't even start running the code because the code grammar is broken.
#
# How to break it:
#   (a) Break the grammar: remove a colon, bracket, or quote.
#   (b) Mess up the indentation: indent a line too far or not far enough.
#
# Quick question:
#   Does "Checking inventory..." still print if the error is on the last line? Why?
# ==============================================================================
'''
print("Checking inventory...")
inventory = {
    "apples": 5,
    "bananas": 0,
    "cherries": 12,
}
for item, qty in inventory.items():
    if qty == 0:
        print(f"{item} is out of stock")
        print("Reorder it today"
'''
# Your notes:
# SyntaxError = Happens when there is a missing Parenthesis, brackets, curly braces, and colons. Also extra or wrong characters causes a syntax error too
# IndentationError = Self explanatory the indents on the code are mismatched/ not aligned properly
#  Removed the curly on line 40, causing a SyntaxError because of it
# 1. it doesnt since python reads the whole file first and if it sees the error. It immediately sends the error


# ==============================================================================
# Break-It 2: NameError & UnboundLocalError
# ==============================================================================
# What it is:
#   Python is looking for a variable name that hasn't been defined in scope.
#
# How to break it:
#   (a) NameError: change a variable name so Python can't find it.
#   (b) UnboundLocalError: inside the function, try to reassign visit_count
#       without declaring it global.
# ==============================================================================
'''
visit_count = 3

def show_visits():
    print(f"Visits so far: {visit_count}")
    global visit_count
    
show_visits()
'''
# Your notes:
# Happens when  a variables name is different or doesnt match a already declared one.
# only copied the function and not the declared variable inside the function causing a NameError since the variable doesnt have a value in it nor it is declared
# 1. Yes when I put a new line above the function works but if I put a new line below the function doesnt work, because the print tries to read the whole function before printing
# 2. the declared variable or the visit count is outside the function making it global and can be accessed by the function. When I added the global visit_count it made a syntaxerror because the global is used prior to global declaration


# ==============================================================================
# Break-It 3: IndexError
# ==============================================================================
# What it is:
#   You asked for an item at an index that doesn't exist in a list or sequence.
#
# How to break it:
#   Leave the function alone. Change ONLY what you pass into print(first_and_last(...)):
#   (a) Pass an empty list: []
#   (b) Pass an empty tuple: () or empty string: ""
#
# Key Concept to notice (Indexing vs Slicing):
#   - Direct indexing: `items[0]` crashes with IndexError on empty data.
#   - Slicing: `items[:1]` and `items[-1:]` NEVER crash! Python safely returns []
#     Try it: change items[0], items[-1] to slices, pass [], and see what happens.
#
# Your quick notes:
#   (a) What happened when passing []?
#   (b) What happened when passing () or ""?
#   Takeaway: Why are slices safer than direct index [0] on empty data?
# ==============================================================================

def first_and_last(items):
    return items[0], items[-1]

print(first_and_last(['Estonia', 'Finland', 'Sweden']))

# Your notes:


# ==============================================================================
# Break-It 4: ModuleNotFoundError
# ==============================================================================
# What it is:
#   Python tried to import a module or package that doesn't exist in sys.path.
#
# How to break it:
#   (a) Misspell the module name: change `random` to `randm`.
#   (b) Try to import a module name that doesn't exist on your computer.
#
# Your quick notes:
#   What was the error message?
# ==============================================================================
'''
import random

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print(random.choice(countries))
'''
# Your notes:


# ==============================================================================
# Break-It 5: AttributeError (The #1 Backend Bug: 'NoneType' has no attribute)
# ==============================================================================
# What it is:
#   You tried to call a method or property on something that doesn't have it.
#   In Flask/backend APIs, this almost always happens when a database query or
#   dictionary lookup returns `None`, and subsequent code treats it like an object!
#
# How to break it:
#   (a) User doesn't exist: call get_display_name(99).
#       users.get(99) returns None. What error does None.get("name") give?
#   (b) Name is None: change user 1's name to None in users: {"name": None, ...}.
#       What error does None.title() give?
#
# Your quick notes:
#   (a) Error when user doesn't exist:
#   (b) Error when name is None:
#   Takeaway: Why should we always check `if user is not None` before using it?
# ==============================================================================
'''
users = {
    1: {"name": "alice", "email": "alice@mail.com"},
    2: {"name": "bob", "email": "bob@mail.com"},
}

def get_display_name(user_id):
    user = users.get(user_id)
    return user.get("name").title()

print(get_display_name(1))
'''
# Your notes:


# ==============================================================================
# Break-It 6: KeyError
# ==============================================================================
# What it is:
#   Accessing a dictionary key that doesn't exist using square brackets: dict["missing"].
#
# How to break it:
#   In count_first_letters, remove the `if letter in result:` check so it directly runs:
#       result[letter] += 1
#   Run it on the names list.
#
# Your quick notes:
#   Why did it crash on the very first name?
#   Takeaway: Why do we use `dict.get(key, default)` or `if key in dict` in backend code?
# ==============================================================================
'''
def count_first_letters(names):
    result = {}
    for name in names:
        letter = name[0].upper()
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

print(count_first_letters(['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']))
'''
# Your notes:


# ==============================================================================
# Break-It 7: TypeError
# ==============================================================================
# What it is:
#   Using the wrong data type for an operation, or calling a function with the wrong arguments.
#
# How to break it (try any of these):
#   (a) Bad data: put a string inside prices: [10, "20", 30]. (Can't add int + str).
#   (b) Wrong argument count: call total_price(10) with only 1 argument instead of 2.
#   (c) Calling a non-function: add `print = 42` before print(), then try to call print().
#
# Your quick notes:
#   Which one did you test, and what was the error message?
# ==============================================================================
'''
from functools import reduce

def total_price(prices, tax_rate):
    subtotal = reduce(lambda acc, price: acc + price, prices, 0)
    return round(subtotal * (1 + tax_rate), 2)

print(total_price([10, 20, 30], 0.12))
'''
# Your notes:


# ==============================================================================
# Break-It 8: ImportError (Module exists, but attribute doesn't)
# ==============================================================================
# What it is:
#   Python found the module (e.g. collections), but the specific tool you asked for
#   isn't inside it.
#   (ModuleNotFoundError = whole file missing. ImportError = file found, but item inside missing).
#
# How to break it:
#   Keep `from collections import ...`, but import a name that doesn't exist:
#       from collections import SuperCounter
#
# Your quick notes:
#   What was the error message?
# ==============================================================================
'''
from collections import Counter

languages = ['English', 'French', 'English', 'Arabic', 'French', 'English']
print(Counter(languages).most_common(2))
'''
# Your notes:


# ==============================================================================
# Break-It 9: ValueError (Right type, invalid content)
# ==============================================================================
# What it is:
#   The function accepts that type, but the specific value cannot be converted or unpacked.
#   Example: int() accepts strings, but int("hello") can't be converted into a number!
#
# How to break it:
#   (a) Pass "hello" or "25.5" to parse_age("hello").
#   (b) Tuple unpack mismatch: change ('Finland', 'Helsinki') to have 3 items:
#       country, capital = ('Finland', 'Helsinki', 'Europe')
#
# Your quick notes:
#   (a) What error does parse_age("hello") give?
#   (b) What error does tuple unpacking mismatch give?
# ==============================================================================
'''
def parse_age(age_raw):
    age = int(age_raw)
    return f"In 10 years you will be {age + 10}"

print(parse_age("25"))

country, capital = ('Finland', 'Helsinki')
print(country, capital)
'''
# Your notes:


# ==============================================================================
# Break-It 10: ZeroDivisionError
# ==============================================================================
# What it is:
#   Dividing or doing modulo by zero (x / 0).
#   In backend APIs, this happens when computing averages or percentages on empty lists!
#
# How to break it:
#   Pass a list with NO positive numbers: [-1, -5, 0].
#   positives becomes [], len(positives) is 0, and sum / 0 crashes!
#
# Your quick notes:
#   What was the traceback line?
#   Takeaway: Why must we always guard with `if len(positives) > 0:` before dividing?
# ==============================================================================
'''
def average_positive(numbers):
    positives = [n for n in numbers if n > 0]
    return sum(positives) / len(positives)

print(average_positive([3, -1, 5, 0, 7]))
'''
# Your notes:


# ==============================================================================
# Wrap-up
# ==============================================================================
# Once you've seen these 10 errors, you're ready for exercise_day_15.py!
# In exercise_day_15.py, you'll write real defensive code to handle dirty payloads,
# query parameters, and custom backend exceptions.
# ==============================================================================
