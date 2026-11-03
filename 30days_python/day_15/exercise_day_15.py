# Day 15: Python Error Types & Defensive Exception Handling Exercises

# ==============================================================================
# LEVEL 1: ERROR RECOGNITION & ROOT CAUSE ANALYSIS
# ==============================================================================

# ==============================================================================
# Exercise 1: Trigger and Identify Core Built-in Errors
# ==============================================================================
# Challenge:
#   For each of the following 10 built-in Python error types, write a minimal
#   reproducing code snippet (1-3 lines) that intentionally triggers the error.
#   Comment out or wrap snippets in functions so the script remains runnable.
#
# Error Types to Trigger:
#   1. SyntaxError
#   2. NameError
#   3. IndexError
#   4. ModuleNotFoundError
#   5. AttributeError
#   6. KeyError
#   7. TypeError
#   8. ImportError
#   9. ValueError
#   10. ZeroDivisionError
#
# Requirements:
#   - Provide a 1-sentence note for each explaining *why* CPython raised it.
# ==============================================================================
'''
# Write your Exercise 1 solution below:
hello = ['hio
'''
# ==============================================================================
# Exercise 2: Compile-Time (Parsing) vs Runtime Errors
# ==============================================================================
# Challenge:
#   Answer the following architectural questions in a comment block:
#   1. Why does a `SyntaxError` in a Python script prevent ANY code in that file
#      from running, even lines located before the error?
#   2. Why can't a `try...except SyntaxError:` block inside `my_script.py` catch a
#      syntax error written directly in `my_script.py`?
#   3. How can you catch a `SyntaxError` dynamically at runtime?
# ==============================================================================
'''
1. Since the python checks the whole code first before running
2. Because the syntax error prevents the code from finishing making it never executes
3. When the code is compiled during an execution
'''
# ==============================================================================
# LEVEL 2: REAL-WORLD BUG DIAGNOSIS & REFACTORING
# ==============================================================================

# ==============================================================================
# Exercise 3: Defensive Payload Extraction (Preventing KeyError & AttributeError)
# ==============================================================================
# Challenge:
#   In web APIs (e.g. Flask/FastAPI), incoming JSON payloads often have missing keys,
#   unexpected null values, or bad structure.
#
#   The following function crashes when given real-world dirty payloads:
#
#   def extract_user_location(payload):
#       # Buggy version:
#       city = payload["user"]["profile"]["address"]["city"]
#       return city.upper()
#
#   Declare a resilient `extract_user_location(payload, default="UNKNOWN")` function that:
#   - Extracts the nested city string and returns it uppercase.
#   - If any dictionary key along the path is missing or if any intermediate node is `None`
#     (e.g. `"profile": None`), returns `default` without raising `KeyError` or `AttributeError`.
#
# Function signature:
#   def extract_user_location(payload, default="UNKNOWN"):
#
# Adversarial Test Matrix:
#   1. Standard Case: `{"user": {"profile": {"address": {"city": "Berlin"}}}}` -> `"BERLIN"`
#   2. Boundary Case: `{}` or `{"user": {}}` -> `"UNKNOWN"`
#   3. Trap Case: `{"user": {"profile": None}}` -> `"UNKNOWN"` (must NOT raise `AttributeError: 'NoneType' object has no attribute 'get'`)
#   4. Trap Case: `{"user": {"profile": {"address": {"city": None}}}}` -> `"UNKNOWN"`
# ==============================================================================
'''
# Write your Exercise 3 solution below:
from typing import final
def extract_user_location(payload, default="UNKNOWN"):
    try:
        city = payload["user"]["profile"]["address"]["city"]
        result = city.upper()
    except (AttributeError, TypeError, KeyError):
        return default
    else:
        return result
print(extract_user_location({"user": {"profile": {"address": {"city": None}}}}))
'''
# ==============================================================================
# Exercise 4: Query Parameter Sanitization (Preventing TypeError & ValueError)
# ==============================================================================
# Challenge:
#   Query string parameters in web requests always arrive as strings or `None`.
#   Write a sanitization function `parse_pagination_params(page_raw, limit_raw)` that:
#   - Parses `page_raw` into a positive integer $\ge 1$ (default: 1).
#   - Parses `limit_raw` into a positive integer between 1 and 100 inclusive (default: 20).
#   - If an input cannot be converted to integer (e.g. `"abc"`, `None`, `[]`), or if the value
#     is negative or out of bounds, gracefully falls back to the default without raising
#     `ValueError` or `TypeError`.
#
# Function signature:
#   def parse_pagination_params(page_raw, limit_raw, default_page=1, default_limit=20, max_limit=100):
#       # Returns tuple: (page: int, limit: int)
#
# Adversarial Test Matrix:
#   1. Standard Case: `parse_pagination_params("2", "50")` -> `(2, 50)`
#   2. Boundary Case: `parse_pagination_params(None, None)` -> `(1, 20)`
#   3. Trap Case: Invalid strings `parse_pagination_params("invalid", "-5")` -> `(1, 20)`
#   4. Trap Case: Limit capping `parse_pagination_params("1", "500")` -> `(1, 20)` (or clamped to 100)
# ==============================================================================
'''
# Write your Exercise 4 solution below:
def parse_pagination_params(page_raw, limit_raw, default_page=1, default_limit=20, max_limit=100):
    try:
        int_page = int(page_raw)
        if int_page <= 0:
            int_page = default_page
    except (ValueError, TypeError):
        int_page = default_page
    try:
        limit_int_page = int(limit_raw)
        if limit_int_page < 1:
            limit_int_page = default_limit
        if limit_int_page > max_limit:
            limit_int_page = default_limit
    except (ValueError, TypeError):
        limit_int_page = default_limit
    return (int_page, limit_int_page)
print(parse_pagination_params("1", "invalid"))
'''
# ==============================================================================
# Exercise 5: Analytics Metrics (Preventing ZeroDivisionError & IndexError)
# ==============================================================================
# Challenge:
#   Write a metric calculator `calculate_transaction_metrics(transactions)` that accepts
#   a list of numeric transaction amounts (floats or ints) and returns a summary dict:
#     {
#       "count": int,
#       "total": float,
#       "average": float,
#       "latest": float
#     }
#   - If `transactions` is empty `[]`:
#       - `count` is 0
#       - `total` is 0.0
#       - `average` is 0.0 (must NOT raise `ZeroDivisionError`)
#       - `latest` is `None` (must NOT raise `IndexError`)
#
# Function signature:
#   def calculate_transaction_metrics(transactions):
#
# Adversarial Test Matrix:
#   1. Standard Case: `[10.0, 20.0, 30.0]` -> `{"count": 3, "total": 60.0, "average": 20.0, "latest": 30.0}`
#   2. Boundary Case: `[]` -> `{"count": 0, "total": 0.0, "average": 0.0, "latest": None}`
#   3. Trap Case: `[-50.0, 50.0]` -> `{"count": 2, "total": 0.0, "average": 0.0, "latest": 50.0}`
# ==============================================================================
'''
# Write your Exercise 5 solution below:
from functools import partialmethod
def calculate_transaction_metrics(transactions):
    try:
        sum_trans = sum(transactions)
        len_trans = len(transactions)
        result = {
            "count" : len_trans,
            "total" : float(sum_trans),
            "average" : float(sum_trans / len_trans),
            "latest" : transactions[-1]
        }
    except (ZeroDivisionError, IndexError):
        result = {
                "count": 0,
                "total": 0.0,
                "average": 0.0,
                "latest": None
            }
    return result
print(calculate_transaction_metrics([10.0, 20.0, 30.0]))
'''
# ==============================================================================
# LEVEL 3: PRODUCTION ARCHITECTURE & EXCEPTION PATTERNS
# ==============================================================================

# ==============================================================================
# Exercise 6: LBYL vs EAFP Comparison
# ==============================================================================
# Challenge:
#   In web services, session caches map a session token to a user session object:
#     cache = {
#         "session_token_1": {"user_id": 99, "role": "admin"},
#         "session_token_2": {"user_id": 101, "role": "member"}
#     }
#
#   Write TWO separate functions to look up a given `token` in `cache` and return its `"role"`:
#   1. `get_user_role_lbyl(cache, token)`:
#      - Uses Look-Before-You-Leap: strictly use conditional checks (`if key in dict`, `isinstance`).
#      - Do NOT use `try...except`.
#   2. `get_user_role_eafp(cache, token)`:
#      - Uses Easier-to-Ask-for-Forgiveness: directly access `cache[token]["role"]` inside a `try` block.
#      - Handle potential exceptions (`KeyError`, `TypeError`, etc.) in the `except` block.
#      - Do NOT use preventative `if` key checks.
#
# Requirements:
#   - Both functions must return the role string (e.g. `"admin"`) if valid.
#   - If `token` is not found, or if the stored session is malformed (e.g. `None`, not a dict,
#     or missing the `"role"` key), return `"GUEST"`.
#   - Include a short docstring in each function explaining the concurrency / race condition
#     trade-off between LBYL and EAFP (specifically TOCTOU: Time-Of-Check to Time-Of-Use).
#
# Function signatures:
#   def get_user_role_lbyl(cache, token):
#   def get_user_role_eafp(cache, token):
#
# Adversarial Test Matrix:
#   1. Standard Case:
#      cache = {"tok_1": {"user_id": 1, "role": "admin"}}
#      get_user_role_*(cache, "tok_1") -> "admin"
#   2. Boundary Case (Token not in cache):
#      get_user_role_*(cache, "unknown_tok") -> "GUEST"
#   3. Trap Case (Session value is None / not a dict):
#      cache = {"tok_none": None}
#      get_user_role_*(cache, "tok_none") -> "GUEST"
#   4. Trap Case (Session is a dict but missing "role"):
#      cache = {"tok_norole": {"user_id": 42}}
#      get_user_role_*(cache, "tok_norole") -> "GUEST"
# ==============================================================================

# Write your Exercise 6 solution below:
from sys import call_tracing
cache = {"session_token_1": {"user_id": 99, "role": "admin"}}
'''
def get_user_role_lbyl(cache, token):
    if token in cache:
        user_info = cache[token]
        if isinstance(user_info, dict):
            if "role" in user_info:
                return user_info["role"]
    return "GUEST"
print(get_user_role_lbyl(cache, "session_token_2"))
'''
'''
def get_user_role_eafp(cache, token):
    try:
        return cache[token]["role"]
    except (KeyError, TypeError):
        return "GUEST"
print(get_user_role_eafp(cache,"session_token_2"))
'''
'''
Doing lBYl is inefficient when being used in a big server and it will check and wait everytime unlike EAFP 
Doing EAFP on the other hand is more efficient since there is less code, handles error well with except. It also leaps through the dict and go straight to the user to check if there is a role in it
'''

# ==============================================================================
# Exercise 7: Robust Resource Lifecycle (`try / except / else / finally`)
# ==============================================================================
# Challenge:
#   Implement a simulated database transaction worker `execute_database_job(job_func, connection)`.
#   The lifecycle must strictly follow:
#   - `try`: Run `job_func(connection)`.
#   - `except DatabaseError as err`: Log/capture the error and call `connection.rollback()`.
#   - `else`: Executed ONLY if `job_func` succeeded without exceptions; call `connection.commit()`.
#   - `finally`: Executed under ALL circumstances; call `connection.close()`.
#
# Function signature:
#   def execute_database_job(job_func, connection):
#       # Returns: {"status": "SUCCESS" | "FAILED", "error": Optional[str]}
#
# Simulation Setup:
#   class DatabaseError(Exception):
#       pass
#
#   class MockConnection:
#       def __init__(self):
#           self.committed = False
#           self.rolled_back = False
#           self.closed = False
#       def commit(self): self.committed = True
#       def rollback(self): self.rolled_back = True
#       def close(self): self.closed = True
#
# Adversarial Test Matrix:
#   1. Standard Case (Transaction Success):
#      Job: lambda conn: "OK"
#      Output: {"status": "SUCCESS", "error": None}
#      Lifecycle State: committed == True, rolled_back == False, closed == True
#
#   2. Boundary Case (Handled Database Failure):
#      Job: lambda conn: (_ for _ in ()).throw(DatabaseError("Deadlock detected"))
#      Output: {"status": "FAILED", "error": "Deadlock detected"}
#      Lifecycle State: committed == False, rolled_back == True, closed == True
#
#   3. Trap Case (Unexpected Critical Error - e.g. KeyError):
#      Job: lambda conn: 1 / 0  (ZeroDivisionError)
#      Output / Behavior: ZeroDivisionError is NOT swallowed (bubbles up)
#      Lifecycle State: committed == False, rolled_back == False, closed == True (must still close!)
# ==============================================================================
'''
class DatabaseError(Exception):
    pass

class MockConnection:
    def __init__(self):
        self.committed = False
        self.rolled_back = False
        self.closed = False
    def commit(self): self.committed = True
    def rollback(self): self.rolled_back = True
    def close(self): self.closed = True
# Write your Exercise 7 solution below:
def execute_database_job(job_func, connection):
    status = {"status" : "SUCCESS", "error" : None}
    try:
        job_func(connection)
    except DatabaseError as e:
        connection.rollback()
        status["status"] = "FAILED"
        status["error"] = str(e)
        return status
    else:
        connection.commit()
        return status
    finally:
        connection.close()
conn1 = MockConnection()
def successful_job(conn):
    return "insert record"

result1 = execute_database_job(successful_job, conn1)
print(result1)
print("Committed:", conn1.committed, "Rolled back:", conn1.rolled_back, "Closed:", conn1.closed)

conn2 = MockConnection()
def failing_job(conn):
    raise DatabaseError("Deadlock detected")
result2 = execute_database_job(failing_job, conn2)
print(result2)  
print("Committed:", conn2.committed, "Rolled back:", conn2.rolled_back, "Closed:", conn2.closed)

conn3 = MockConnection()
def crash_job(conn):
    return 10 / 0  # ZeroDivisionError!
try:
    execute_database_job(crash_job, conn3)
except ZeroDivisionError:
    print("Caught unexpected error - it bubbled up properly!")
print("Closed:", conn3.closed)
'''

# ==============================================================================
# Exercise 8: Custom Exception Hierarchy & Explicit Chaining (`from err`)
# ==============================================================================
# Challenge:
#   In backend services, internal low-level errors (like `KeyError`, `sqlite3.IntegrityError`,
#   or `ValueError`) should be wrapped into domain-specific exceptions before reaching the HTTP layer.
#
#   1. Define a base domain exception `AppException(Exception)`.
#   2. Define a specialized subclass `EntityNotFoundError(AppException)`.
#   3. Implement `find_user_by_id(user_db, user_id)`:
#      - If `user_id` is missing from `user_db` (which raises `KeyError`), catch the `KeyError as err`
#        and explicitly raise `EntityNotFoundError(f"User {user_id} does not exist") from err`.
#      - Verify using `__cause__` that original exception context is preserved!
#
# Function signature:
#   def find_user_by_id(user_db, user_id):
#
# Adversarial Test Matrix:
#   1. Standard Case (User Found):
#      find_user_by_id({101: {"username": "ada"}}, 101) -> {"username": "ada"}
#
#   2. Boundary Case (User Missing -> Wrapped Domain Exception):
#      find_user_by_id({}, 999) -> raises EntityNotFoundError("User 999 does not exist")
#
#   3. Trap Case (Explicit Exception Chaining Preserved):
#      try:
#          find_user_by_id({}, 999)
#      except EntityNotFoundError as e:
#          assert isinstance(e.__cause__, KeyError)  # Original KeyError MUST be attached via 'from err'!
#          assert isinstance(e, AppException)       # Must inherit from base domain AppException!
# ==============================================================================
'''
# Write your Exercise 8 solution below:
class AppException(Exception):
    pass

class EntityNotFoundError(AppException):
    pass

def find_user_by_id(user_db, user_id):
    try:
        return user_db[user_id]
    except KeyError as err:
        raise EntityNotFoundError(f"User {user_id} does not exist") from err

user = find_user_by_id({101: {"username": "ada"}}, 101)
print("Found:", user)
# 2 & 3. Boundary & Trap Cases (Testing error raising & exception chaining)
try:
    find_user_by_id({}, 999)
except EntityNotFoundError as e:
    print("Caught domain exception:", e)
    assert isinstance(e.__cause__, KeyError)  # Verifies 'from err' worked!
    assert isinstance(e, AppException)       # Verifies inheritance worked!
    print("All assertions passed! __cause__ is:", repr(e.__cause__))
'''