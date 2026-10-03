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

## Print/Console Debugging

The simplest debugging technique is printing values at key points to see what the program is actually doing versus what you assumed it was doing.

```python
def total_price(items):
    print(f"items: {items}")  # temporary debug line
    return sum(item["price"] for item in items)
```

This is quick but easy to forget to remove, and doesn't let you pause execution — for anything non-trivial, a real debugger is faster.

## Using a Debugger

A debugger lets you pause execution at a specific line (a breakpoint) and inspect variables at that exact moment, instead of guessing from printed output.

```python
def total_price(items):
    breakpoint()  # execution pauses here; inspect `items` interactively
    return sum(item["price"] for item in items)
```

Most editors (VS Code, PyCharm) let you click in the margin to set a breakpoint instead of editing code, then step through line by line, watching variables change.

## Writing a Simple Unit Test
