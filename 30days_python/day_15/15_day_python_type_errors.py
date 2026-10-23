# Day 15: Python Error Types & Exception Handling - Interactive Walkthrough

"""
Day 15: Interactive Walkthrough
Demonstrates the 10 core built-in Python error types, why they occur,
how CPython reports them, and how to prevent or handle them cleanly.
Note: Trigger functions use dynamic execution (eval/exec/getattr/importlib)
to keep static language servers (e.g. Pylance/VS Code) clean while still
reliably generating each exact runtime exception for demonstration.
"""

import importlib
import operator
import traceback

def demonstrate_error(error_name, error_func):
    """Helper to safely demonstrate an error, printing its exception type and message."""
    print(f"\n{'='*70}")
    print(f" DEMONSTRATION: {error_name}")
    print(f"{'='*70}")
    try:
        error_func()
    except BaseException as e:
        print(f"[CAUGHT] {type(e).__name__}: {e}")
        print("[TRACEBACK SNIPPET]:")
        tb_lines = traceback.format_exception_only(e)
        for line in tb_lines:
            print(f"  {line.strip()}")

# ==============================================================================
# 1. SyntaxError
# ==============================================================================
# SyntaxError is detected during parsing, BEFORE any bytecode executes.
# To demonstrate it safely at runtime without breaking file compilation,
# we parse invalid source dynamically with `eval()`.
def trigger_syntax_error():
    # Missing closing parenthesis and invalid print syntax
    eval("print 'Hello World'")

# ==============================================================================
# 2. NameError & UnboundLocalError
# ==============================================================================
# NameError occurs when an identifier is evaluated without being bound to an object.
def trigger_name_error():
    # Evaluating undefined identifier at runtime
    return eval("non_existent_variable + 10")

def trigger_unbound_local_error():
    # If a variable is assigned anywhere inside a function, Python marks it local!
    # Referencing it before the assignment triggers UnboundLocalError.
    code = """
counter = 1
def increment():
    counter += 1
increment()
"""
    exec(code)

# ==============================================================================
# 3. IndexError
# ==============================================================================
# Occurs when accessing an index outside sequence boundaries.
def trigger_index_error():
    languages = ["Python", "Rust", "Go"]
    out_of_bounds_index = 5
    return languages[out_of_bounds_index]

# ==============================================================================
# 4. ModuleNotFoundError
# ==============================================================================
# Subclass of ImportError; occurs when importing a module that does not exist.
# Using importlib dynamically triggers the error without breaking IDE static analyzers.
def trigger_module_not_found_error():
    importlib.import_module("non_existent_database_driver")

# ==============================================================================
# 5. AttributeError
# ==============================================================================
# Occurs when attempting to access a non-existent attribute or method on an object.
def trigger_attribute_error():
    number = 42
    # Integers do not have a .upper() method
    return getattr(number, "upper")()

# ==============================================================================
# 6. KeyError
# ==============================================================================
# Occurs when accessing a dictionary with a key that is missing.
def trigger_key_error():
    user = {"id": 1, "username": "alice"}
    missing_key = "email"
    return user[missing_key]

# ==============================================================================
# 7. TypeError
# ==============================================================================
# Occurs when an operation or callable is invoked on an incompatible type.
def trigger_type_error():
    # Cannot concatenate str and int with +
    return operator.add("Status code: ", 200)

# ==============================================================================
# 8. ImportError
# ==============================================================================
# Occurs when a module exists, but the requested symbol inside it does not.
def trigger_import_error():
    # 'math' exists, but 'non_existent_function' does not
    exec("from math import non_existent_function")

# ==============================================================================
# 9. ValueError
# ==============================================================================
# Occurs when an argument has the right type, but an unacceptable value.
def trigger_value_error():
    # 'int' accepts strings, but 'abc' cannot be parsed as a base-10 integer
    invalid_number_string = "not_a_number"
    return int(invalid_number_string)

# ==============================================================================
# 10. ZeroDivisionError
# ==============================================================================
# Occurs when the denominator of division or modulo is zero.
def trigger_zero_division_error():
    denominator = 0
    return 100 / denominator

# ==============================================================================
# Defensive Patterns Walkthrough
# ==============================================================================
def defensive_patterns_demo():
    print(f"\n{'='*70}")
    print(" DEFENSIVE PATTERNS: LBYL vs EAFP")
    print(f"{'='*70}")

    payload = {"user_id": 42, "role": "admin"}

    # Pattern A: LBYL (Look Before You Leap)
    if "email" in payload:
        email_lbyl = payload["email"]
    else:
        email_lbyl = "default@domain.com"
    print(f"[LBYL] Extracted email: {email_lbyl}")

    # Pattern B: EAFP (Easier to Ask for Forgiveness than Permission)
    try:
        email_eafp = payload["email"]
    except KeyError:
        email_eafp = "default@domain.com"
    print(f"[EAFP] Extracted email: {email_eafp}")

    # Pattern C: Idiomatic Python Dict Access (.get)
    email_get = payload.get("email", "default@domain.com")
    print(f"[dict.get] Extracted email: {email_get}")

if __name__ == "__main__":
    demonstrate_error("1. SyntaxError", trigger_syntax_error)
    demonstrate_error("2. NameError", trigger_name_error)
    demonstrate_error("2B. UnboundLocalError (subclass of NameError)", trigger_unbound_local_error)
    demonstrate_error("3. IndexError", trigger_index_error)
    demonstrate_error("4. ModuleNotFoundError", trigger_module_not_found_error)
    demonstrate_error("5. AttributeError", trigger_attribute_error)
    demonstrate_error("6. KeyError", trigger_key_error)
    demonstrate_error("7. TypeError", trigger_type_error)
    demonstrate_error("8. ImportError", trigger_import_error)
    demonstrate_error("9. ValueError", trigger_value_error)
    demonstrate_error("10. ZeroDivisionError", trigger_zero_division_error)
    defensive_patterns_demo()
