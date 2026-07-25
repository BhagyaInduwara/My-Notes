# Data Structures & Algorithms Basics

Data structures organize data so it can be used efficiently; algorithms are step-by-step procedures for solving problems. Understanding both helps you write code that stays fast as your data grows.

## Big O Notation

Big O describes how an algorithm's time or space requirements grow as input size (`n`) grows, ignoring constant factors. It answers "what happens as the input gets huge?"

```
O(1)      constant     — array index lookup
O(log n)  logarithmic  — binary search
O(n)      linear       — scanning a list once
O(n log n) — efficient sorting (merge sort, quicksort average case)
O(n^2)    quadratic    — nested loops over the same data
```

An `O(n^2)` algorithm might be fine for 100 items but unusably slow for 1,000,000 — Big O helps you predict that before it becomes a production problem.

## Arrays

An array stores elements in contiguous memory, accessed by index. Reading by index is `O(1)`, but inserting/removing from the middle is `O(n)` because later elements must shift.

```python
numbers = [10, 20, 30, 40]
print(numbers[2])       # 30, O(1) lookup
numbers.insert(1, 15)   # O(n), shifts elements right
print(numbers)          # [10, 15, 20, 30, 40]
```

## Linked Lists

A linked list stores elements as nodes, each pointing to the next. Unlike arrays, elements aren't contiguous in memory, so inserting/removing at a known position is `O(1)`, but finding an element by position is `O(n)` (no direct indexing).

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# 1 -> 2 -> 3
head = Node(1, Node(2, Node(3)))

current = head
while current:
    print(current.value)
    current = current.next
```

## Stacks and Queues
