# Strings
Text is a string data type. Any data type written as a text is a string. Any data under single, double or triple quote are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.

### Multiline string is created by using (''') or triple double quotes (""")

## String Concatenation
We can connect strings together. Merging or connecting strings is called concatenation.

### Escape sequences in Strings
In python and other programming alnguages \ followed by a character is an escape sequence.

\n: new line
\t: Tab means (8 spaces)
\\: Back slash
\': Single quote
\": Double quote

## String Formatting

### Old stype string formatting (% Operator)
In python there are many ways of formatting strings. In this section, we will cover some of them. The "%" Operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digitsf".

%s - String (Or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision

## Python Strings as a sequences of Characters
Python strings are sequences of characters, and share their basic methods of access with other python ordered sequences of objects - lists and tuples. The simplest way of extracting single characters from trings (and individual members from any sequence) is to unpack them into corresponding variables.

# Accessing Characters in String by Index
In programming counting starts from zero. Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one.
['P', 'y', 't', 'h', 'o', 'n']
  0    1    2    3    4    5

## String methods
There are many string methods which allow us to format strings. 
capitalize(): Converts the first character of the string to capital letter
count(): Returns occurrences of substring in string count(substring, start=.., end=..) The start is indexing for counting and end is the last index to count
endswith(): Checks if a string ends with a specified ending
expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
find(): Returns the index of the first occurrence of a substring, if not found returns -1
rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
format(): Formats string into a nicer output
index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length -1). If the substring is not found it raises a valueError.
rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index(default 0 and string length -1)
isalnum(): Checks alphanumeric characters
isalpha(): Checks if all string elements are alphabet characters
isdecimal(): Checks if all characters in a string are decimal