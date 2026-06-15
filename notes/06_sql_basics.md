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

`PRIMARY KEY` uniquely identifies each row. `NOT NULL` means the column can't be left empty. `UNIQUE` means no two rows can share the same value.

## Inserting Data

`INSERT INTO` adds new rows to a table.

```sql
INSERT INTO users (name, email, age) VALUES ('Alex', 'alex@example.com', 25);
INSERT INTO users (name, email, age) VALUES ('Sam', 'sam@example.com', 30);
```

## Selecting Data

`SELECT` retrieves data. `*` means "all columns", or you can list specific ones.

```sql
SELECT * FROM users;
SELECT name, email FROM users;
```

`WHERE` filters rows based on a condition.

```sql
SELECT * FROM users WHERE age > 26;
SELECT * FROM users WHERE name = 'Alex';
```

`ORDER BY` sorts results, and `LIMIT` caps how many rows come back.

```sql
SELECT * FROM users ORDER BY age DESC LIMIT 5;
```

## Updating and Deleting
