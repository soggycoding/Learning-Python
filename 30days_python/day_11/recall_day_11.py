# ==========================================
# DAY 11 RECALL CHALLENGE: REVERSE LIST
# ==========================================
# Task: Write a function `reverse_list` from pure memory.
# Try implementing it using one of the following approaches without peeking:
#   1. Using reverse indexing/slicing
#   2. Using an index loop: range(start, stop, step)
#   3. Using a while loop with a decrementing index
#
# Once done, run your script and ask to check your work!

def reverse_list(*items):
    for item in items[::-1]:
        print(item)
reverse_list('Bing', 'Bong', 'Boop', 'Bloop')