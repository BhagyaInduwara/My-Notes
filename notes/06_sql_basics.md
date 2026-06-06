# SQL Basics

SQL (Structured Query Language) is how you talk to relational databases: creating tables, inserting data, and asking questions about it. Data is organized into tables made of rows and columns.

## Creating a Table

`CREATE TABLE` defines a table's columns and their types.

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER
);
```
