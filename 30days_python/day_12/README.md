# Day 12: Modules

A **module** is a file containing a set of codes or functions that can be included and reused across different Python applications. A module can contain variables, functions, classes, or even an entire library.

---

## 1. What is a Module?

Writing all code in a single file quickly becomes messy and unmaintainable. Modules allow us to organize code logically into separate `.py` files and import them wherever needed.

---

## 2. Creating and Importing Custom Modules

### Creating a Module
To create a module, write Python functions or variables in a `.py` file (e.g. `mymodule.py`):

```python
# mymodule.py
def generate_full_name(firstname, lastname):
    return f"{firstname} {lastname}"

gravity = 9.81
```

### Importing a Module
To use code from `mymodule.py` in another file in the same directory:

```python
# main.py
import mymodule

print(mymodule.generate_full_name('Soggy', 'Coder'))
print(mymodule.gravity)
```

---

## 3. Import Styles and Renaming

### Importing Specific Functions
Instead of importing the entire module namespace:

```python
from mymodule import generate_full_name, gravity

print(generate_full_name('Soggy', 'Coder'))
```

### Renaming / Aliasing with `as`
When a module or function name is long or conflicts with local names:

```python
import mymodule as mm
from mymodule import generate_full_name as full_name

print(mm.gravity)
print(full_name('Soggy', 'Coder'))
```

---

## 4. Built-in Modules in the Standard Library

Python comes with an extensive standard library of pre-built modules:

* **`random`**: Pseudo-random number generator for simulations, games, and non-security tasks (`random.random()`, `random.randint()`, `random.choice()`, `random.choices()`, `random.sample()`, `random.shuffle()`).
* **`secrets`**: Cryptographically secure random number generator designed for security tokens, passwords, authentication keys, and sensitive data (`secrets.choice()`, `secrets.randbelow()`, `secrets.token_hex()`, `secrets.token_urlsafe()`, `secrets.compare_digest()`).
* **`string`**: Predefined character constants (`string.ascii_letters`, `string.digits`, `string.punctuation`, `string.hexdigits`).
* **`math`**: Mathematical functions and constants (`math.pi`, `math.sqrt()`, `math.floor()`, `math.ceil()`).
* **`os`**: Operating system interactions (directories, environment variables, paths).
* **`sys`**: System-specific parameters and functions (`sys.argv`, `sys.exit()`, `sys.version`).
* **`statistics`**: Mathematical statistics functions (`statistics.mean()`, `statistics.median()`, `statistics.mode()`).

---

## 5. Security Note: `random` vs `secrets`

| Feature | `random` Module | `secrets` Module |
| :--- | :--- | :--- |
| **Engine** | Mersenne Twister (PRNG) | OS Cryptographic Entropy (CSPRNG) |
| **Predictability** | **Predictable**: State can be reversed after seeing 624 outputs | **Non-predictable**: Cryptographically secure |
| **Best Used For** | Games, simulations, statistical modeling, shuffling playlists | Passwords, account recovery tokens, session IDs, API keys |
| **Multi-Item Sampling** | `random.choices(seq, k=n)` (with replacement) | Pick 1 item at a time with `secrets.choice(seq)` |

