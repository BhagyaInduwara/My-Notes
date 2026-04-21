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
