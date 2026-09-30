# Debugging & Testing Basics

Writing code is only half the job — sooner or later something won't work the way you expect, and you need a reliable way to find out why. Debugging is the process of locating and fixing that problem; testing is how you catch it automatically next time, before it reaches anyone else.

## Reading Error Messages

A traceback (Python) or stack trace (JavaScript) tells you exactly where and why something failed, read from the bottom up: the last line is usually the actual error, and the lines above it show the chain of function calls that led there.

```python
def divide(a, b):
    return a / b

divide(10, 0)
# Traceback (most recent call last):
#   File "main.py", line 4, in <module>
#     divide(10, 0)
#   File "main.py", line 2, in divide
#     return a / b
# ZeroDivisionError: division by zero
```

The error type (`ZeroDivisionError`) and message tell you *what* went wrong; the file and line number tell you *where*. Resist the urge to guess — read the actual message first.
