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

# Write your Exercise 3 solution below:


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

# Write your Exercise 4 solution below:


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

# Write your Exercise 5 solution below:


# ==============================================================================
# LEVEL 3: PRODUCTION ARCHITECTURE & EXCEPTION PATTERNS
# ==============================================================================

# ==============================================================================
# Exercise 6: LBYL vs EAFP Comparison
# ==============================================================================
# Challenge:
#   Given a cache dictionary `cache = {"session_token_1": {"user_id": 99, "role": "admin"}}`:
#   Write TWO separate functions to fetch the `"role"`:
#   1. `get_user_role_lbyl(cache, token)`: Uses Look-Before-You-Leap (`if key in dict: ...`)
#   2. `get_user_role_eafp(cache, token)`: Uses Easier-to-Ask-for-Forgiveness (`try...except KeyError: ...`)
#
#   Both functions must return the role string if found, or `"GUEST"` if missing or malformed.
#   Include a short docstring explaining the concurrency / race condition trade-off between the two.
# ==============================================================================

# Write your Exercise 6 solution below:


# ==============================================================================
# Exercise 7: Robust Resource Lifecycle (`try / except / else / finally`)
# ==============================================================================
# Challenge:
#   Implement a simulated database transaction worker `execute_database_job(job_func, connection)`.
#   The lifecycle must strictly follow:
#   - `try`: Run `job_func(connection)`.
#   - `except DatabaseError as err`: Log the error and call `connection.rollback()`.
#   - `else`: Executed ONLY if `job_func` succeeded without exceptions; call `connection.commit()`.
#   - `finally`: Executed under ALL circumstances; call `connection.close()`.
#
#   Return a status dict: `{"status": "SUCCESS" | "FAILED", "error": Optional[str]}`.
# ==============================================================================

# Write your Exercise 7 solution below:


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
#      - If `user_id` is missing from `user_db` (which raises `KeyError`), catch the `KeyError`
#        and explicitly raise `EntityNotFoundError(f"User {user_id} does not exist") from err`.
#      - Verify using `__cause__` that original exception context is preserved!
# ==============================================================================

# Write your Exercise 8 solution below:
