# Day 15: Python Error Types & Defensive Exception Handling - Alternative Solutions (Pass 2)

# ==============================================================================
# Exercise 1: Inspecting & Running Exceptions Programmatically (Pass 2)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Inspect an Exception):
#      Trigger any error from Pass 1 (e.g. `[][0]`). In `except Exception as err:`, print:
#        1. `type(err).__name__` -> Name of the error as a string
#        2. `err.args`           -> Tuple of arguments/message in the error
#        3. `err.__class__.__mro__` -> Tuple showing the inheritance chain
#    - Option B (Automated Error Runner):
#      Write `capture_exception(func)`:
#        - Runs `func()`.
#        - If no error: returns `(True, None, None)`
#        - If error occurs: returns `(False, type(err).__name__, str(err))`
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Why catch `Exception` instead of `BaseException`?
#      `KeyboardInterrupt` (Ctrl+C) and `SystemExit` inherit from `BaseException`,
#      NOT `Exception`. Catching `Exception` ensures you don't accidentally block exits.
#
# Target Output:
#   Option A: "IndexError", ("list index out of range",), (<class 'IndexError'>, ..., <class 'BaseException'>, <class 'object'>)
#   Option B: capture_exception(lambda: 1 / 0) -> (False, "ZeroDivisionError", "division by zero")
#             capture_exception(lambda: [][0]) -> (False, "IndexError", "list index out of range")
# ==============================================================================
'''
# Write your Exercise 1 (Pass 2) solution below:
# Option A:
try:
    print([0][1])
except Exception as err:
    print(type(err).__name__)
    print(err.args)
    print(err.__class__.__mro__)
'''
'''
def capture_exception(func):
    try:
        func()
        return(True, None, None)
    except Exception as err:
        return(False, type(err).__name__, str(err))
print(capture_exception(lambda: [][0]))
'''
# ==============================================================================
# Exercise 2: Catching Syntax Errors at Runtime (Pass 2)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Use ast.parse):
#      Write `validate_syntax(code_str)`:
#        - In `try`, run `ast.parse(code_str)`.
#        - In `except SyntaxError as err`, return `(False, err.msg)`.
#        - If valid, return `(True, None)`.
#    - Option B (Use compile):
#      Same as Option A, but use `compile(code_str, "<string>", "exec")`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Why `try...except SyntaxError:` inside a script can't catch its own syntax errors:
#      Python compiles the whole file to bytecode BEFORE running any lines. A syntax
#      error stops compilation, so the `try` block never gets to run.
#    - `ast.parse()` parses code safely as data without executing it.
#
# Function signature:
#   def validate_syntax(code_str):
#
# Adversarial Test Matrix:
#   1. Standard Case (Valid Python Code):
#      validate_syntax("x = 10 + 20") -> (True, None)
#
#   2. Boundary Case (Unclosed brackets / unexpected EOF):
#      validate_syntax("x = [1, 2,") -> (False, "unexpected EOF while parsing")
#
#   3. Trap Case (IndentationError - subclass of SyntaxError):
#      validate_syntax("def foo():\npass") -> (False, "expected an indented block after function definition on line 1")
#
#   4. Trap Case (Empty String - valid empty module in Python):
#      validate_syntax("") -> (True, None)
# ==============================================================================
'''
import ast
# Write your Exercise 2 (Pass 2) solution below:
def validate_syntax(code_str):
    try:
        ast.parse(code_str)
    except SyntaxError as err:
        return (False, err.msg)
    else:
        return (True, None)
print(validate_syntax("x = 10 + 20"))
'''
'''
def validate_syntax(code_str):
    try:
        compile(code_str, "<string>", "exec")
    except SyntaxError as err:
        return (False, err.msg)
    else:
        return (True, None)
print(validate_syntax("x = 10 + 20"))
'''
# ==============================================================================
# Exercise 3: Nested Dict Extraction (Pass 2: Functional vs Pattern Matching)
# ==============================================================================
# Starter Data:
#   payload_valid = {"user": {"profile": {"address": {"city": "Berlin"}}}}
#   payload_missing = {"user": {"profile": None}}
#   payload_empty = {}
#
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (functools.reduce):
#      Extract the path `["user", "profile", "address", "city"]` using `reduce()`:
#      `reduce(lambda acc, key: acc.get(key) if isinstance(acc, dict) else None, path, payload)`
#    - Option B (Python 3.10+ match / case):
#      Use structural pattern matching:
#        match payload:
#            case {"user": {"profile": {"address": {"city": str(city)}}}}:
#                return city.upper()
#            case _:
#                return default
#
# 2. Mechanistic Analysis & Trade-offs:
#    - `reduce`: Works with any dynamic list of keys passed at runtime.
#    - `match / case`: Clean syntax for fixed schemas; checks types automatically (`str(city)`).
#
# Function signature:
#   def extract_user_location(payload, default="UNKNOWN"):
#
# Adversarial Test Matrix:
#   1. Standard Case (Full valid payload):
#      extract_user_location({"user": {"profile": {"address": {"city": "Berlin"}}}}) -> "BERLIN"
#
#   2. Boundary Case (Empty payload):
#      extract_user_location({}) -> "UNKNOWN"
#
#   3. Trap Case (Intermediate node is None):
#      extract_user_location({"user": {"profile": None}}) -> "UNKNOWN"
#
#   4. Trap Case (City value is None or non-string):
#      extract_user_location({"user": {"profile": {"address": {"city": None}}}}) -> "UNKNOWN"
# ==============================================================================
'''
# Write your Exercise 3 (Pass 2) solution below:
from functools import reduce
from typing import final
def extract_user_location(payload, default="UNKNOWN"):
    try:
        path = ["user", "profile", "address", "city"]
        result = reduce(lambda acc, key: acc.get(key) if isinstance(acc, dict) else None, path, payload).upper()
    except (AttributeError, TypeError, KeyError):
        return default
    else:
        return result
print(extract_user_location({}))
'''
'''
def extract_user_location(payload, default="UNKNOWN"):
    match payload:
        case {"user": {"profile": {"address": {"city": str(city)}}}}:
            return city.upper()
        case _:
            return default
print(extract_user_location({"user": {"profile": {"address": {"city": "Berlin"}}}}))
'''
# ==============================================================================
# Exercise 4: Query Param Sanitization (Pass 2: Helper & Math Clamping)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Reusable Safe Int Helper + Clamping):
#      1. Write helper `safe_int(val, default)` using `try...except (ValueError, TypeError)`.
#      2. Clamp the value using `max(min_val, min(val, max_val))` instead of multiple `if`s.
#    - Option B (Loop Over Specs):
#      Define parameter rules in a dict:
#        specs = {"page": (default_page, min_page, max_page), "limit": (default_limit, min_limit, max_limit)}
#      Process each param through a single parsing loop.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - `max(low, min(val, high))` clamps a number in one line with no branching (`if/else`).
#    - Centralizing `safe_int()` keeps endpoints DRY.
#
# Function signature:
#   def parse_pagination_params(page_raw, limit_raw, default_page=1, default_limit=20, max_limit=100):
#
# Adversarial Test Matrix:
#   1. Standard Case: parse_pagination_params("2", "50") -> (2, 50)
#   2. Boundary Case (None inputs): parse_pagination_params(None, None) -> (1, 20)
#   3. Trap Case (Invalid strings / negative): parse_pagination_params("invalid", "-5") -> (1, 20)
#   4. Trap Case (Out of bounds upper): parse_pagination_params("1", "500") -> (1, 20) (or clamped to 100)
# ==============================================================================
'''
# Write your Exercise 4 (Pass 2) solution below:
def safe_int(val, default):
    try:
        return int(val)
    except (ValueError, TypeError):
        return default
def parse_pagination_params(page_raw, limit_raw, default_page=1, default_limit=20, max_limit=100):
    page = safe_int(page_raw, default_page)
    limit = safe_int(limit_raw, default_limit)
    if page < 1:
        page = default_page
    if limit < 1 or limit > max_limit:
        limit = default_limit
    return (page, limit)
print(parse_pagination_params("1", "500"))
'''

# ==============================================================================
# Exercise 5: Analytics Metrics (Pass 2: Standard Library & Single-Pass Loop)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (statistics.fmean):
#      Use `statistics.fmean(transactions)` inside a `try...except statistics.StatisticsError:`
#      to compute the average.
#    - Option B (Single-Pass Accumulator):
#      Calculate `count`, `total`, and `latest` in a single `for` loop so the list is
#      only traversed once ($O(n)$ time, $O(1)$ space).
#
# 2. Mechanistic Analysis & Trade-offs:
#    - `len()` then `sum()` loops through the list twice. A single loop does it once and
#      can handle generators / streams that cannot be re-read.
#    - `statistics.fmean()` is implemented in C and runs faster than Python-level loops.
#
# Function signature:
#   def calculate_transaction_metrics(transactions):
#
# Adversarial Test Matrix:
#   1. Standard Case: calculate_transaction_metrics([10.0, 20.0, 30.0]) -> {"count": 3, "total": 60.0, "average": 20.0, "latest": 30.0}
#   2. Boundary Case (Empty list): calculate_transaction_metrics([]) -> {"count": 0, "total": 0.0, "average": 0.0, "latest": None}
#   3. Trap Case (Cancelling negatives): calculate_transaction_metrics([-50.0, 50.0]) -> {"count": 2, "total": 0.0, "average": 0.0, "latest": 50.0}
# ==============================================================================
'''
# Write your Exercise 5 (Pass 2) solution below:
from ast import Return
def calculate_transaction_metrics(transactions):
    count = 0
    total = 0.0
    average = 0.0
    latest = None
    try:
        count = len(transactions)
        total = sum(transactions)
        average = total/len(transactions)
        latest = transactions[-1]
    except ZeroDivisionError:
        pass
    return {
    "count": count,
    "total": float(total),
    "average": float(average),
    "latest": latest  # float if exists, or None if empty
    }
print(calculate_transaction_metrics([]))
'''
# ==============================================================================
# Exercise 6: LBYL vs EAFP (Pass 2: Chained .get() vs Pattern Matching)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Chained .get() with `or {}` fallback):
#      Fetch role in one line:
#        role = (cache.get(token) or {}).get("role", "GUEST")
#    - Option B (Structural Pattern Matching):
#        match cache.get(token):
#            case {"role": str(role)}:
#                return role
#            case _:
#                return "GUEST"
#
# 2. Mechanistic Analysis & Trade-offs:
#    - In Python 3.11+, `try` has zero overhead when NO error happens. But when an
#      error does happen, it is slower than `if`.
#      - If misses are rare: EAFP (`try/except`) is fastest.
#      - If misses are common: `.get()` or `if` avoids exception overhead.
#    - The `or {}` pattern prevents `AttributeError` when a key exists but holds `None`.
#
# Function signature:
#   def get_user_role(cache, token):
#
# Adversarial Test Matrix:
#   1. Standard Case: get_user_role({"tok_1": {"role": "admin"}}, "tok_1") -> "admin"
#   2. Boundary Case (Missing token): get_user_role({}, "bad_token") -> "GUEST"
#   3. Trap Case (Session value is None): get_user_role({"t": None}, "t") -> "GUEST"
#   4. Trap Case (Missing 'role' key): get_user_role({"t": {"user_id": 5}}, "t") -> "GUEST"
# ==============================================================================
'''
# Write your Exercise 6 (Pass 2) solution below:
def get_user_role(cache, token):
    role = (cache.get(token) or {}).get("role", "GUEST")
    return role

print(get_user_role({"tok_1": {"role": "admin"}}, "tok_1"))
'''


# ==============================================================================
# Exercise 7: Database Lifecycle (Pass 2: Context Manager Protocol)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (@contextmanager Generator):
#      Write `transaction_scope(connection)` using `contextlib.contextmanager`:
#        try: yield connection
#        except DatabaseError as err: connection.rollback()
#        else: connection.commit()
#        finally: connection.close()
#    - Option B (Class with __enter__ and __exit__):
#      Implement a `Transaction` class that handles the same lifecycle using
#      `__enter__` and `__exit__`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Context managers replace repetitive `try / except / else / finally` boilerplate
#      with a clean `with transaction_scope(conn):` block.
#    - This is the exact pattern used by SQLAlchemy (`session.begin()`).
#
# Adversarial Test Matrix:
#   1. Standard Case (Success):
#      with transaction_scope(conn): pass
#      conn.committed == True, conn.rolled_back == False, conn.closed == True
#
#   2. Boundary Case (DatabaseError):
#      try:
#          with transaction_scope(conn): raise DatabaseError("Deadlock")
#      except DatabaseError: pass
#      conn.committed == False, conn.rolled_back == True, conn.closed == True
#
#   3. Trap Case (Unexpected exception bubbles up):
#      try:
#          with transaction_scope(conn): 1 / 0
#      except ZeroDivisionError: pass
#      conn.closed == True (must still close!)
# ==============================================================================

# Write your Exercise 7 (Pass 2) solution below:
from contextlib import contextmanager

class DatabaseError(Exception):
    pass

class MockConnection:
    def __init__(self):
        self.committed = False
        self.rolled_back = False
        self.closed = False
    def commit(self):
        self.committed = True
    def rollback(self):
        self.rolled_back = True
    def close(self):
        self.closed = True
        
@contextmanager
def transaction_scope(connection):
    try:
        yield connection
    
    except DatabaseError as err:
        connection.rollback()
        raise
    else:
        connection.commit()
    finally:
        connection.close()

# ==============================================================================
# Exercise 8: Domain Exceptions (Pass 2: Traceback Suppression & .to_dict())
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Suppress Traceback with `from None`):
#      Raise `EntityNotFoundError(...) from None` so internal file paths / database
#      details are hidden from public API responses.
#    - Option B (Exception with .to_dict()):
#      Give `EntityNotFoundError` attributes (`self.entity_type`, `self.entity_id`,
#      `self.status_code = 404`) and a `to_dict()` method for direct JSON serialization.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - `raise ... from err`: Keeps full cause chain in `__cause__` (for internal logging).
#    - `raise ... from None`: Strips internal causes (for public security).
#    - A `.to_dict()` method lets Flask's `@app.errorhandler` return clean JSON in 1 line.
#
# Adversarial Test Matrix:
#   1. Standard Case (.to_dict() output):
#      err = EntityNotFoundError("User", 999)
#      err.to_dict() -> {"error": "User with ID '999' not found.", "entity": "User", "status": 404}
#
#   2. Boundary Case (Inheritance hierarchy):
#      issubclass(EntityNotFoundError, AppException) == True
#      issubclass(AppException, Exception) == True
#
#   3. Trap Case (Traceback suppression with 'from None'):
#      try:
#          try: {}["missing"]
#          except KeyError: raise EntityNotFoundError("User", 1) from None
#      except EntityNotFoundError as e:
#          e.__cause__ is None
#          e.__suppress_context__ is True
# ==============================================================================

# Write your Exercise 8 (Pass 2) solution below:
