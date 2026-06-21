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

`UPDATE` changes existing rows, and `DELETE` removes them. Both should almost always be paired with a `WHERE` clause — without one, they affect every row in the table.

```sql
UPDATE users SET age = 26 WHERE name = 'Alex';

DELETE FROM users WHERE name = 'Sam';
```

## Joins

Real data is usually split across multiple related tables. A `JOIN` combines rows from two tables based on a matching column.

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

SELECT users.name, orders.product
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

An `INNER JOIN` returns only rows that match in both tables. A `LEFT JOIN` returns all rows from the left table, filling in `NULL` for unmatched columns from the right table.

```sql
SELECT users.name, orders.product
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

## Aggregate Functions and GROUP BY

Aggregate functions compute a single value from many rows: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`. `GROUP BY` buckets rows before aggregating.

```sql
SELECT COUNT(*) FROM users;

SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id;
```

`HAVING` filters groups after aggregation (whereas `WHERE` filters individual rows before grouping).

```sql
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 1;
```

## Indexes

An index speeds up lookups on a column, much like an index in a book helps you find a topic without reading every page.

```sql
CREATE INDEX idx_users_email ON users(email);
```
