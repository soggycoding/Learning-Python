# Day 15: Break-It Challenges (warm-up while reading README.md)

# ==============================================================================
# How this file works
# ==============================================================================
#   - Every snippet below WORKS as written. Your job is to break it with the
#     target error.
#   - Take the `'''` off ONE challenge at a time, run it, then put the `'''` back.
#   - Follow each challenge's Rules. No `raise` statements. Break it the way
#     real code breaks: bad data, a missing check, a moved line, a wrong import.
#   - Read the README section named in "Read first" BEFORE you start breaking.
#   - For every break, fill in this template under "Your notes":
#       (a) Changed:   what you changed
#           Predicted: the error you expect, written BEFORE you run it
#           Got:       the last line of the traceback
#           Why:       one sentence, your own words
#     If Predicted and Got don't match, reread that README section.
#   - Mark a challenge "— verified <date>" when every part is done.
# ==============================================================================


# ==============================================================================
# Break-It 1: SyntaxError & IndentationError
# ==============================================================================
# Read first: README section 2 (Compile-Time vs Runtime), section 3 -> 1. SyntaxError
# Rules:
#   - Add, change, or delete exactly ONE character per attempt.
# Breaks to find:
#   (a) SyntaxError
#   (b) IndentationError
#   (c) Delete one character so the error points at a DIFFERENT line than the
#       one you changed.
# Questions:
#   1. When your break is on the LAST line, does "Checking inventory..." still
#      print? Why? (This is exercise_day_15.py Exercise 2, question 1.)
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
# Read first: README section 3 -> 2. NameError (and UnboundLocalError)
# Rules & breaks to find:
#   (a) NameError: change ONE name in ONE place.
#   (b) NameError: don't type anything. Only MOVE one existing line.
#   (c) UnboundLocalError: undo (a) and (b). ADD one line inside the function.
#       Don't change or delete the existing lines.
# Questions:
#   1. For (c), put your new line ABOVE the print, then BELOW it. Did the
#      position matter? Why?
#   2. Research: the `global` keyword. How does it relate to (c)?
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
# Read first: README section 3 -> 3. IndexError
# Rules:
#   - Don't touch the function. Only change what is passed in.
# Breaks to find:
#   (a) IndexError with a list.
#   (b) IndexError with something that is NOT a list.
# Questions:
#   1. Can you find an input where `items[0]` works but `items[-1]` crashes?
#      Why or why not?
#   2. Change the function to use slices (`items[:1]`, `items[-1:]`) and rerun
#      your (a) input. What happens now?
# ==============================================================================

def first_and_last(items):
    return (items[:1], items[-10:])

print(first_and_last(['Estonia', 'Finland', 'Sweden']))

# Your notes:
# IndexError list of index out of range, I tried doing a -10 on the index that is only 3 sequences
# I IndexError with a tuple
# 1. I made the 2nd item be out of index making the 2nd crash while the first go through
# 2. It does not error it separates the two items  making it do the first item as the first in the index and the 2nd one as a new index


# ==============================================================================
# Break-It 4: ModuleNotFoundError
# ==============================================================================
# Read first: README section 3 -> 4. ModuleNotFoundError
# Breaks to find:
#   (a) Change one character in the import line.
#   (b) No typos this time. Import a module that DOES exist on your computer
#       (you have `countries_data.py` in day_11 and day_14) and still get
#       ModuleNotFoundError.
# Questions:
#   1. Add `import sys` and `print(sys.path[0])`. Which folder does it print?
#      Use that to explain (b).
# ==============================================================================
'''
import random

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print(random.choice(countries))
'''
# Your notes:


# ==============================================================================
# Break-It 5: AttributeError
# ==============================================================================
# Read first: README section 3 -> 5. AttributeError (read the "Backend Gotcha")
# Rules:
#   - Don't touch the function. Only change the `users` data or the call's argument.
# Breaks to find (each message must be different):
#   (a) the message mentions 'get'
#   (b) the message mentions 'title' AND 'NoneType'
#   (c) the message mentions 'title' but NOT 'NoneType'
# Questions:
#   1. In a Flask app, where could a `None` sneak in like it does in (a)?
#   2. Change `user.get("name")` to `user["name"]` and redo break (a). The error
#      type changes. Which one, and why isn't it AttributeError anymore?
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
# Read first: README section 3 -> 6. KeyError, and section 4 (LBYL vs EAFP)
# This is the counting pattern you wrote on Day 14.
# Rules:
#   (a) KeyError: delete lines only, then fix the indentation. Don't type new code.
#   (b) Undo (a). Now only change the list passed in, and break it with a
#       DIFFERENT error type (not KeyError).
# Questions:
#   1. Predict before running (a): does it crash on the FIRST name, or only when
#      a letter repeats ('Abraham')? Then check.
#   2. What does the KeyError message show: the name, or the letter?
#   3. Is the original `if letter in result` version LBYL or EAFP?
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
# Read first: README section 3 -> 7. TypeError
# TypeError has a few "flavors". Find one break for each:
#   (a) Bad data: change ONE value inside the prices list.
#   (b) Wrong number of arguments: change only the call line.
#   (c) Calling something that isn't a function: ADD one ordinary variable
#       assignment line above the print. Change nothing else.
#       (Research: "shadowing built-in names".)
#   (d) Delete one argument from the `reduce(...)` call, then call
#       `total_price([], 0.12)`. (You wrote about this in Day 14 Exercise 1.)
# Questions:
#   1. For (a), the message names two types. Which one is on the left of the
#      `+` and which on the right? Look at the lambda to explain the order.
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
# Break-It 8: ImportError
# ==============================================================================
# Read first: README section 1 (the hierarchy tree), section 3 -> 8. ImportError
# Rules:
#   - Keep `collections` exactly as written. Change only the name after `import`.
# Breaks to find:
#   (a) ImportError (NOT ModuleNotFoundError) using a made-up name.
#   (b) ImportError using a REAL tool you've used before, imported from the wrong
#       module. (Day 14 used tools from `functools` and `operator`.)
# Questions:
#   1. Wrap your (a) import in `try:` / `except ModuleNotFoundError:`. Is it caught?
#      Then wrap Break-It 4 (a) in `try:` / `except ImportError:`. Is that caught?
#      Explain both answers using the hierarchy tree.
# Bonus (optional):
#   Make two scratch files, `circ_a.py` and `circ_b.py`, where each one does
#   `from <the other> import <something>`. Run one and read the message.
#   Delete both files when you're done.
# ==============================================================================
'''
from collections import Counter

languages = ['English', 'French', 'English', 'Arabic', 'French', 'English']
print(Counter(languages).most_common(2))
'''
# Your notes:


# ==============================================================================
# Break-It 9: ValueError
# ==============================================================================
# Read first: README section 3 -> 9. ValueError (compare with 7. TypeError)
# Rules:
#   - Only change the value passed to `parse_age`, or the tuple on the last line.
# Breaks to find:
#   (a) ValueError through `parse_age`.
#   (b) TypeError through `parse_age`. Same function, same line crashes.
#       Explain the type-vs-value difference in one sentence.
#   (c) ValueError on the last line by changing only the tuple.
# Questions:
#   1. Predict, then check: which of these crash, and which run?
#      " 25 "    "25.0"    "-25"    "1_000"    25.9
#   2. Some of those run with NO error but give an answer that makes no sense
#      for an age. Which ones? Why is that worse than a crash in a backend?
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
# Read first: README section 3 -> 10. ZeroDivisionError
# Rules:
#   - Only change the list. Your list must NOT be empty.
# Questions:
#   1. Is `[]` also a break? Which line does the traceback point to?
#   2. Change `/` to `//`, then to `%`, and rerun your break. Same error type?
#      Same message?
#   3. Predict: does `5 / 0.0` crash, or does it give something like infinity?
# ==============================================================================
'''
def average_positive(numbers):
    positives = [n for n in numbers if n > 0]
    return sum(positives) / len(positives)

print(average_positive([3, -1, 5, 0, 7]))
'''
# Your notes:


# ==============================================================================
# Wrap-up (after all 10)
# ==============================================================================
#   1. Which errors did you predict WRONG? List them here. Reread those sections.
#   2. Then do exercise_day_15.py Exercise 1 from memory. Don't look at this file.
# ==============================================================================
