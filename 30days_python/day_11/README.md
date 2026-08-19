# Day 11: Functions

So far we have used many built-in Python functions (such as `print()`, `len()`, `type()`, `int()`, `input()`, `sum()`, etc.). In this section, we will learn how to create custom functions (user-defined functions).

A **function** is a reusable block of code or programming statements designed to perform a specific task. Functions make code modular, reusable, organized, and easier to debug and test.

---

## 1. Defining and Calling a Function

A function is defined using the `def` keyword followed by the function name, parentheses `()`, and a colon `:`. The block of code inside the function must be indented.

### Calling a Function
To execute the code inside a function, call it by using its name followed by parentheses `()`.

---

## 2. Function Returning a Value

Functions can return values using the `return` keyword. If a function does not have a `return` statement, it returns `None` by default. Returning a value allows us to store the output of a function in a variable and use it elsewhere in our code.

---

## 3. Function with Parameters

Parameters are variables declared inside the function definition parentheses. When calling the function, we pass values (called **arguments**) for those parameters. A function can take a single parameter or multiple parameters separated by commas.

---

## 4. Passing Arguments with Key and Value (Keyword Arguments)

If we pass arguments with key and value (keyword arguments), the order of the arguments does not matter when calling the function.

---

## 5. Function with Default Parameters

Sometimes we pass default values to parameters during function definition. If we do not pass arguments when calling the function, the default values will be used automatically.

---

## 6. Arbitrary Number of Arguments (`*args`)

If we do not know in advance how many positional arguments will be passed to a function, we can prefix a parameter with an asterisk `*` (commonly named `*args`). The arguments passed will be packed into a **tuple**.

---

## 7. Arbitrary Number of Keyword Arguments (`**kwargs`)

If we do not know how many keyword arguments will be passed, we prefix a parameter with double asterisks `**` (commonly named `**kwargs`). The keyword arguments passed will be packed into a **dictionary**.

---

## 8. Function as a Parameter to Another Function

In Python, functions are first-class objects (first-class citizens), meaning they can be assigned to variables, passed as arguments to other functions, and returned from other functions just like any other data type.
