# Day 11: Functions

So far we have used many built-in Python functions (such as `print()`, `len()`, `type()`, `int()`, `input()`, `sum()`, etc.). In this section, we will learn how to create custom functions (user-defined functions).

A **function** is a reusable block of code or programming statements designed to perform a specific task. Functions make code modular, reusable, organized, and easier to debug and test.

---

## 1. Defining and Calling a Function

A function is defined using the `def` keyword followed by the function name, parentheses `()`, and a colon `:`. The block of code inside the function must be indented.

### Syntax:
```python
def function_name():
    # code goes here
    # code goes here
```

### Calling a Function:
To execute the code inside a function, call it by using its name followed by parentheses `()`.

```python
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name() # Calling the function
```

```python
def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)

add_two_numbers()
```

---

## 2. Function Returning a Value

Functions can return values using the `return` keyword. If a function does not have a `return` statement, it returns `None` by default. Returning a value allows us to store the output of a function in a variable and use it elsewhere in our code.

### Syntax:
```python
def function_name():
    # code goes here
    return value
```

### Example:
```python
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
```

```python
def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total

print(add_two_numbers())
```

---

## 3. Function with Parameters

Parameters are variables declared inside the function definition parentheses. When calling the function, we pass values (called **arguments**) for those parameters.

### Single Parameter Syntax:
```python
def function_name(parameter):
    # code goes here
    return value
```

### Example:
```python
def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))
```

```python
def square_number(x):
    return x * x

print(square_number(2))
print(square_number(5))
```

```python
def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area

print(area_of_circle(10))
```

### Two or Multiple Parameters Syntax:
```python
def function_name(param1, param2):
    # code goes here
    return value
```

### Example:
```python
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print('Full Name: ', generate_full_name('Asabeneh', 'Yetayeh'))
```

```python
def add_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum

print('Sum of numbers: ', add_two_numbers(1, 9))
```

```python
def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2026, 1819))
```

---

## 4. Passing Arguments with Key and Value (Keyword Arguments)

If we pass arguments with key and value, the order of the arguments does not matter.

### Syntax:
```python
def function_name(para1, para2):
    # code goes here
    return value

function_name(para1='val1', para2='val2') # order does not matter
function_name(para2='val2', para1='val1')
```

### Example:
```python
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name

print(print_fullname(firstname='Asabeneh', lastname='Yetayeh'))
print(print_fullname(lastname='Yetayeh', firstname='Asabeneh'))
```

```python
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

print(add_two_numbers(num2=3, num1=2)) # Order does not matter
```

---

## 5. Function with Default Parameters

Sometimes we pass default values to parameters. If we do not pass arguments when calling the function, the default values will be used.

### Syntax:
```python
def function_name(para1='default_val1', para2='default_val2'):
    # code goes here
    return value
```

### Example:
```python
def greetings(name='Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings())          # Uses default value 'Peter'
print(greetings('Asabeneh')) # Uses argument 'Asabeneh'
```

```python
def generate_full_name(first_name='Asabeneh', last_name='Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David', 'Beckham'))
```

```python
def calculate_weight(mass, gravity=9.81):
    weight = str(mass * gravity) + ' N'
    return weight

print('Weight of an object in N: ', calculate_weight(100))        # 981 N
print('Weight of an object in N: ', calculate_weight(100, 1.62))  # 162 N (Moon gravity)
```

---

## 6. Arbitrary Number of Arguments (`*args`)

If we do not know the number of arguments passed to a function, we can pass a parameter with an asterisk `*` before the parameter name. The arguments are packed into a **tuple**.

### Syntax:
```python
def function_name(*args):
    # code goes here
    return value
```

### Example:
```python
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums(2, 3, 5))       # Output: 10
print(sum_all_nums(2, 3, 5, 6, 7)) # Output: 23
```

### Default and Arbitrary Number of Parameters:
```python
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)

generate_groups('Team 1', 'Asabeneh', 'Brook', 'David', 'Eyob')
```

---

## 7. Arbitrary Number of Keyword Arguments (`**kwargs`)

If we do not know how many keyword arguments will be passed, we use double asterisks `**` before the parameter name. The arguments are packed into a **dictionary**.

### Syntax:
```python
def function_name(**kwargs):
    # code goes here
    return value
```

### Example:
```python
def show_user_info(**user):
    for key, value in user.items():
        print(f'{key}: {value}')

show_user_info(name='Asabeneh', age=250, country='Finland', job='Teacher')
```

---

## 8. Function as a Parameter to Another Function

In Python, functions are first-class objects, meaning they can be passed as arguments to other functions just like any other variable.

### Example:
```python
def square_number(n):
    return n * n

def do_something(f, x):
    return f(x)

print(do_something(square_number, 3)) # Output: 9
```
