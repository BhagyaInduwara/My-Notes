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
