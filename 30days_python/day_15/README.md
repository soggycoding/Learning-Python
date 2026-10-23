# 📘 Day 15: Python Error Types & Exception Handling

Welcome to **Day 15**! Today we tackle Python's built-in error types and exception mechanics. In backend engineering, understanding how Python represents, propagates, and raises exceptions is fundamental to writing resilient, self-healing services and clean API error boundaries.

> [!NOTE]
> All executable code implementations and interactive walkthroughs for these error types are located in [15_day_python_type_errors.py](file:///c:/Users/Jeth/Desktop/Learning-Python/30days_python/day_15/15_day_python_type_errors.py).
> Pass 1 exercises are set up in [exercise_day_15.py](file:///c:/Users/Jeth/Desktop/Learning-Python/30days_python/day_15/exercise_day_15.py).

---

## 1. The Python Exception Hierarchy

In Python, all exceptions are instances of classes derived from `BaseException`. However, built-in non-system exceptions inherit from `Exception`:

```text
BaseException
 ├── SystemExit                   # Raised by sys.exit()
 ├── KeyboardInterrupt            # Raised by Ctrl+C
 ├── GeneratorExit                # Raised when a generator terminates
 └── Exception                    # Base class for ALL application-level exceptions
      ├── ArithmeticError
      │    └── ZeroDivisionError  # Division/modulo by zero
      ├── LookupError
      │    ├── IndexError         # Sequence index out of range
      │    └── KeyError           # Dict key not found
      ├── AttributeError          # Attribute reference or assignment failure
      ├── NameError               # Local/global identifier not found
      │    └── UnboundLocalError  # Local variable referenced before assignment
      ├── SyntaxError             # Parser syntax grammar failure
      │    └── IndentationError   # Malformed indentation
      ├── TypeError               # Inappropriate argument type or unsupported operand
      ├── ValueError              # Inappropriate argument value (valid type)
      └── ImportError
           └── ModuleNotFoundError # Module does not exist
```

> [!WARNING]
> **Never catch `BaseException` or use a bare `except:`!**
> Catching `BaseException` swallows `KeyboardInterrupt` (Ctrl+C) and `SystemExit`, preventing the program or container from shutting down cleanly. Always catch `Exception` or, ideally, specific exceptions.

---

## 2. Compile-Time (Parsing) vs Runtime Errors

Python is interpreted, but it compiles source code into bytecode before executing it. This creates two distinct error categories:

1. **Parsing Phase (Compile-Time)**:
   * Errors like `SyntaxError` and `IndentationError` happen during Python's tokenizing and parsing stage before any bytecode runs.
   * A syntax error in a file prevents the entire module from executing, even code located before the line with the syntax error.
   * `try...except` inside the same module cannot catch a `SyntaxError` originating in that same module's uncompiled source text.

2. **Execution Phase (Runtime)**:
   * Errors like `TypeError`, `KeyError`, `IndexError`, and `ValueError` occur while bytecode instructions are running.
   * These exceptions travel up the call stack until intercepted by an enclosing `try...except` block or terminating the program with an unhandled traceback.

---

## 3. The 10 Core Error Types

### 1. `SyntaxError` (and `IndentationError`)
* **Trigger**: Invalid Python syntax that violates grammar rules (e.g., missing colons, mismatched brackets, invalid keywords).
* **Fix**: Review syntax highlighting and interpreter line indicators.

### 2. `NameError` (and `UnboundLocalError`)
* **Trigger**: Referencing a variable or function name that has not been defined in the current local, enclosing, global, or built-in scope.
* **Special Case (`UnboundLocalError`)**: Assigning to a variable inside a function makes it local to that function. Referencing it before the assignment statement raises `UnboundLocalError`.

### 3. `IndexError`
* **Trigger**: Accessing an index of a sequence (list, tuple, string) outside `[-len(seq), len(seq) - 1]`.
* **Note**: Slicing (`seq[start:stop]`) never raises `IndexError`; it truncates boundaries gracefully. Direct indexing (`seq[i]`) does raise `IndexError`.

### 4. `ModuleNotFoundError`
* **Trigger**: Importing a module name that cannot be located in `sys.path` or installed environment packages. Subclass of `ImportError`.

### 5. `AttributeError`
* **Trigger**: Attempting to access an attribute or method that does not exist on an object.
* **Backend Gotcha**: The classic `'NoneType' object has no attribute '...'` occurs when a database query, dictionary `.get()`, or function returns `None` unexpectedly and subsequent code treats it as an object.

### 6. `KeyError`
* **Trigger**: Accessing a dictionary using a key that does not exist (`dict[key]`).
* **Fix**: Use `dict.get(key, default)`, `dict.setdefault()`, or `collections.defaultdict`.

### 7. `TypeError`
* **Trigger**: Applying an operation, function call, or subscript to an incompatible type (e.g., `'str' + 42`, calling a non-callable `x = 5; x()`, passing the wrong number of arguments to a function).

### 8. `ImportError`
* **Trigger**: The module is found, but the specific attribute, class, or function specified in `from module import name` does not exist inside that module, or circular imports exist.

### 9. `ValueError`
* **Trigger**: A function receives an argument that has the correct *type* but an invalid *value* (e.g., `int("abc")`, `math.sqrt(-1)`).

### 10. `ZeroDivisionError`
* **Trigger**: The divisor in a division (`/`, `//`) or modulo (`%`) operation evaluates to zero.

---

## 4. Defensive Engineering: LBYL vs EAFP

Python strongly embraces **EAFP**:

| Paradigm | Philosophy | Python Idiom | Trade-offs |
| :--- | :--- | :--- | :--- |
| **LBYL** (Look Before You Leap) | Explicitly verify preconditions before performing an action. | `if "key" in data: val = data["key"]` | Extra checks; susceptible to race conditions (TOCTOU: Time of Check to Time of Use). |
| **EAFP** (Easier to Ask for Forgiveness than Permission) | Assume validity, execute the operation, and handle exceptions. | `try: val = data["key"] except KeyError: val = default` | Fast when exceptions are rare (happy path); clean; thread-safe against state changes between check and execution. |

---

## 5. Structured Exception Handling: `try / except / else / finally`

```python
try:
    # 1. Risky code that may raise an exception
    result = perform_action()
except SpecificError as e:
    # 2. Executed ONLY if SpecificError occurred inside `try`
    handle_error(e)
else:
    # 3. Executed ONLY if NO exception was raised in `try`
    # Keep the `try` block minimal; put downstream dependent code here
    process_result(result)
finally:
    # 4. ALWAYS executed, regardless of whether an exception occurred,
    # was handled, or even if `return` was encountered.
    # Ideal for cleanup: closing DB sessions, files, network sockets.
    cleanup_resources()
```

---

## 6. Exception Chaining (`raise ... from err`)

In backend services (e.g., Flask APIs), low-level database or network errors should often be translated into high-level domain exceptions. Python provides explicit exception chaining with `from`:

```python
try:
    user = db_session.query(User).filter_by(id=user_id).one()
except NoResultFound as err:
    raise UserNotFoundError(f"User {user_id} not found in database") from err
```

Using `from err` populates `__cause__` and outputs `The above exception was the direct cause of the following exception:`, preserving full debugging context for error monitoring systems like Sentry or Datadog.

---

## 7. Key Takeaways
1. Catch specific exceptions; never swallow `BaseException` or leave unhandled bare `except:`.
2. Differentiate between compile-time syntax failures and runtime exceptions.
3. Use EAFP for idiomatic, race-condition-safe Python code.
4. Keep `try` blocks tightly scoped around only the code capable of raising the expected exception. Use `else:` for follow-up code.
5. Use `raise DomainException(...) from original_error` to maintain clear exception lineage.
