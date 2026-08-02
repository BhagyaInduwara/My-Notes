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

A stack is Last-In-First-Out (LIFO) — think of a stack of plates, you take from the top. A queue is First-In-First-Out (FIFO) — think of a checkout line.

```python
# Stack using a Python list
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())  # 3 (last in, first out)

from collections import deque

# Queue using deque (efficient at both ends)
queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())  # 1 (first in, first out)
```

Stacks are used for undo history and function call tracking; queues are used for task scheduling and breadth-first traversal.

## Hash Maps

A hash map (dictionary in Python) stores key-value pairs and offers average `O(1)` lookup, insertion, and deletion by hashing the key to a memory location.

```python
ages = {"Alex": 25, "Sam": 30}
ages["Jordan"] = 28

print(ages["Alex"])       # 25, O(1) average
print("Sam" in ages)      # True, O(1) average
```

Hash maps trade some memory overhead for that speed, and are one of the most commonly used data structures in real code.

## Trees

A tree is a hierarchical structure of nodes, each with a value and references to child nodes. A binary search tree (BST) keeps values ordered: everything in a node's left subtree is smaller, everything in its right subtree is larger.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):
    if node is None:
        return TreeNode(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

root = None
for v in [5, 3, 8, 1, 4]:
    root = insert(root, v)
```

A balanced BST gives `O(log n)` search, insert, and delete — much better than a linear scan.
