# Python Basics

Python is a general-purpose, readable programming language popular for scripting, web backends, data science, and automation. It uses indentation (not curly braces) to define code blocks, which forces consistently readable code.

## Variables and Types

Python is dynamically typed — you don't declare a type, but every value still has one.

```python
name = "Alex"       # str
age = 25             # int
height = 1.75        # float
is_student = True    # bool

print(type(age))     # <class 'int'>
```

## Basic Operators

Arithmetic, comparison, and logical operators work as you'd expect, with a few Python-specific extras like `**` for exponents and `//` for floor division.

```python
print(7 // 2)   # 3  (floor division)
print(7 % 2)    # 1  (remainder)
print(2 ** 5)   # 32 (exponent)
print(5 == 5 and 3 < 4)  # True
```

## Strings

Strings support slicing, formatting, and many built-in methods.

```python
greeting = "Hello, World!"

print(greeting.lower())        # hello, world!
print(greeting[7:12])          # World
print(f"Length: {len(greeting)}")  # Length: 13
```

f-strings (`f"..."`) are the preferred way to build strings with embedded expressions.

## Lists, Tuples, and Dictionaries

A list is an ordered, mutable collection. A tuple is ordered but immutable. A dictionary maps keys to values.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")

point = (3, 4)  # tuple, cannot be changed after creation

person = {"name": "Sam", "age": 30}
print(person["name"])  # Sam
```

List comprehensions offer a concise way to build lists from an iterable.

```python
squares = [n ** 2 for n in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

evens = [n for n in range(10) if n % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

## Control Flow

`if`/`elif`/`else` for branching, `for` and `while` for loops. Blocks are defined purely by indentation.

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(grade)  # B

for fruit in fruits:
    print(fruit)

count = 0
while count < 3:
    print(count)
    count += 1
```

## Functions

Functions are defined with `def` and can have default arguments, keyword arguments, and type hints.

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

print(greet("Alex"))               # Hello, Alex!
print(greet("Sam", greeting="Hi")) # Hi, Sam!
```

Type hints (`name: str`, `-> str`) are optional and not enforced at runtime, but they help tools catch bugs and make code self-documenting.

## Error Handling

`try`/`except` catches exceptions so a program can recover instead of crashing.

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # None
```

## Modules and Packages

Code can be split across files (modules) and imported where needed. Python's standard library and PyPI packages extend this further.

```python
import math
from datetime import date

print(math.sqrt(16))   # 4.0
print(date.today())    # today's date
```

## Reading Files

Use `with` (a context manager) so files are automatically closed even if an error occurs.

```python
with open("notes.txt", "w") as f:
    f.write("Hello, file!")

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)  # Hello, file!
```
