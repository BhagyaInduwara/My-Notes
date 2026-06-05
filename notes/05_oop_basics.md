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

By exposing `deposit` and `get_balance` instead of letting code freely modify `_balance`, the class can enforce rules (like rejecting negative deposits).

### 2. Abstraction

Abstraction means hiding complex implementation details behind a simple interface. The caller of `deposit()` doesn't need to know how the balance is validated or stored — they just call the method.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2
```

`Shape` defines *what* every shape must be able to do (`area()`) without saying *how*. Each subclass fills in the how.

### 3. Inheritance

Inheritance lets a class (the subclass) reuse and extend behavior from another class (the superclass).

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

whiskers = Cat("Whiskers")
print(whiskers.speak())  # Whiskers says Meow!
```

`Cat` inherits `__init__` from `Animal` and overrides `speak` with its own version.

### 4. Polymorphism

Polymorphism means objects of different classes can be used through the same interface, each responding in its own way.

```python
animals = [Cat("Whiskers"), Animal("Generic")]

for animal in animals:
    print(animal.speak())
# Whiskers says Meow!
# ...
```

The calling code doesn't need to know the exact type — it just calls `.speak()` and lets each object decide how to respond.

## Overriding vs Overloading

**Overriding** happens when a subclass provides its own version of a method already defined in its superclass (as `Cat.speak` did above). It's resolved at runtime based on the object's actual type.

**Overloading** means having multiple versions of a function/method that differ by parameters (same name, different signatures). Python doesn't support true overloading — a later `def` with the same name replaces the earlier one — so it's usually simulated with default arguments or `*args`.

```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(1))        # 1
print(calc.add(1, 2))     # 3
print(calc.add(1, 2, 3))  # 6
```

Languages like Java or C++ support real overloading, where the compiler picks the matching method based on argument types at compile time.

## Composition over Inheritance

Composition means building complex objects by combining simpler ones, instead of inheriting from a base class. It's often more flexible because it avoids deep, rigid class hierarchies.

```python
class Engine:
    def start(self):
        return "Engine starting..."

class Car:
    def __init__(self):
        self.engine = Engine()  # Car "has-a" Engine

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Engine starting...
```

The rule of thumb: use inheritance for a true "is-a" relationship (a `Cat` is an `Animal`), and composition for a "has-a" relationship (a `Car` has an `Engine`).

## Dunder (Magic) Methods

"Dunder" means double underscore. These special methods let your objects work with Python's built-in syntax like `+`, `len()`, `print()`, and comparisons.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

Common dunder methods: `__init__` (constructor), `__repr__` (developer-facing string), `__str__` (user-facing string), `__eq__` (equality), `__len__` (used by `len()`), `__add__`/`__sub__` (operators).

## Classes in JavaScript

JavaScript classes are syntactic sugar over its prototype-based object system, but they read similarly to classes in Python or Java.

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} makes a sound.`;
  }
}

class Dog extends Animal {
  speak() {
    return `${this.name} barks.`;
  }
}

const rex = new Dog("Rex");
console.log(rex.speak()); // Rex barks.
```

`extends` sets up inheritance, and calling `super()` inside a subclass constructor runs the parent class's constructor.

```javascript
class Cat extends Animal {
  constructor(name, indoor) {
    super(name);
    this.indoor = indoor;
  }
}
```

## SOLID Principles

SOLID is a set of five design guidelines for writing maintainable object-oriented code.

**S — Single Responsibility Principle**: a class should have only one reason to change. A `ReportGenerator` shouldn't also handle emailing the report — split those into two classes.

**O — Open/Closed Principle**: classes should be open for extension but closed for modification. Add new behavior by adding new code (e.g., a new subclass), not by editing existing, tested code.

**L — Liskov Substitution Principle**: a subclass should be usable anywhere its superclass is expected, without breaking correctness. If `Square extends Rectangle` but changing width unexpectedly changes height too, it violates this principle.

**I — Interface Segregation Principle**: prefer many small, specific interfaces over one large general-purpose interface, so classes don't depend on methods they don't use.

**D — Dependency Inversion Principle**: depend on abstractions, not concrete implementations. High-level code should not need to know the details of low-level code — both should depend on an interface.

```python
class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Emailing: {message}")

class OrderService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender  # depends on the abstraction, not EmailSender directly

    def place_order(self):
        self.sender.send("Order placed!")
```

`OrderService` can work with any `NotificationSender` (email, SMS, push notification) without changing its own code — that's dependency inversion in practice.

## Key takeaways

- Classes are blueprints; objects are instances with their own state.
- The four pillars are encapsulation, abstraction, inheritance, and polymorphism.
- Overriding replaces a parent's method in a subclass; overloading (simulated in Python) means multiple signatures for one name.
- Prefer composition ("has-a") over inheritance ("is-a") when relationships aren't strictly hierarchical.
- Dunder methods let custom objects integrate with built-in Python syntax.
- SOLID principles guide maintainable, extensible object-oriented design.
