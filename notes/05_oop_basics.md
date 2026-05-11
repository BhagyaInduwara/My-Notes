# Object-Oriented Programming (OOP) Basics

Object-oriented programming organizes code around **objects** — bundles of data (attributes) and behavior (methods) — instead of just functions acting on raw data. It helps model real-world entities and keeps related code together.

## Classes and Objects

A class is a blueprint; an object (or instance) is a concrete thing built from that blueprint. You can create many objects from one class, each with its own state.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

rex = Dog("Rex", "Labrador")
bella = Dog("Bella", "Poodle")

print(rex.bark())    # Rex says Woof!
print(bella.bark())  # Bella says Woof!
```

`__init__` is the constructor — it runs automatically when a new object is created and sets up its initial state. `self` refers to the specific instance the method is being called on.

## The Four Pillars of OOP

### 1. Encapsulation

Encapsulation means bundling data and the methods that operate on it together, and restricting direct access to internal details. In Python, a leading underscore signals "internal use only" by convention.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # "protected" by convention

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150
```
