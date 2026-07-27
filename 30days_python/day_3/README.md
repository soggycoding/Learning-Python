# Day 3 : Operators

## Boolean

A boolean data type represents one of the two values: True or False. The use of these data types will be clear once we start using the comparison operator.

## Operators

Python language supports several types of operators

# Assignment Operators

Assignment operators are used to assign values to variables. Let us take '=' as an example. Equal sign in mathematics shows that two values are equal, however in Python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable.

### Operator    
= - x = 5 
+= - x += 3
-= - x -= 3
*= - x *= 3
/= - x /= 3
%= - x %= 3
//= - x //= 3
**= - x **= 3
&= - x &= 3
|= - x |= 3
^= - x ^= 3
>>= - x >>= 3
<<= - x <<= 3

### Arithmetic Operators:
Addition(+): a + b
Subtraction(-): a - b
Multiplication(*): a * b
Division(/): a / b
Modulus(%): a % b
Floor division(//): a // b

### Operator
+ = Addition  x + y
- = Subtraction  x - y
* = Multiplication x * y
/ = Division x / y
% = Modulus x % y
** = Exponentiation x ** y
// = Floor division x // y

# Comparision Operators
== - Equal
!= - Not equal
> - Greater than
< - Less than
>= - Greater than or equal to
<= - Less than or equal to

### In addition to the above comparison operator Python uses:
- is : Returns true if both variables are the same objects(x is y)
- is not : Return true if both variables are not the same objects(x is not y)
- in : Returns True if the queried list contains a certain item (x in y)
- not in: Returns True if the queried list doesn't have a certain item (x not in y)

## Logical Operators
- Unlike other programming languages python uses keywords and, or and not for logical operators. Logical operators are used to combine conditional statements:

and - Returns True if both statements are true - x < 5 and x < 10
or - Returns True if one of the statements is true - x < 5 or x > 4
not - Reverse the result, returns False if the result is true - not(x < 5 and x < 10)