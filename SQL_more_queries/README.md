# SQL - More queries

This document covers some advanced SQL queries and concepts, including creating users, managing privileges, primary and foreign keys, constraints, retrieving data from multiple tables, subqueries, and JOIN and UNION operations.

### How to create a new MySQL user

To create a new MySQL user, you can use the CREATE USER statement:

```mysq
CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
```

**username:**  the name of the new user.
**hostname: ** the hostname from which the user can connect to the MySQL server.
**password: ** the password for the new user.

You can also specify additional options, such as account lockout, password expiration, and more. See the MySQL documentation for more information.

### How to manage privileges for a user to a database or table

To grant privileges to a user for a database or table, you can use the GRANT statement:

```mysql
GRANT privilege ON database.table TO 'user'@'hostname';
```
**privilege:** the privilege to grant (e.g. SELECT, INSERT, UPDATE, DELETE, etc.).
**database.table:** the database and table for which to grant the privilege.
**user@hostname: ** the user and hostname for which to grant the privilege.

To revoke privileges, you can use the REVOKE statement:

```mysql
REVOKE privilege ON database.table FROM 'user'@'hostname';
```
###  What’s a PRIMARY KEY
A PRIMARY KEY is a column or set of columns that uniquely identifies each row in a table. It is used to enforce data integrity and to enable efficient indexing and querying of the table.

To create a PRIMARY KEY, you can use the PRIMARY KEY constraint in the CREATE TABLE statement:
```mysql
CREATE TABLE table_name (
  column1 datatype PRIMARY KEY,
  column2 datatype,
  ...
);
```
### What’s a FOREIGN KEY
A FOREIGN KEY is a column or set of columns that refers to a PRIMARY KEY or UNIQUE constraint in another table. It is used to enforce referential integrity between tables.

To create a FOREIGN KEY, you can use the FOREIGN KEY constraint in the CREATE TABLE statement:

```mysql
CREATE TABLE table_name1 (
  column1 datatype PRIMARY KEY,
  column2 datatype,
  ...
);

CREATE TABLE table_name2 (
  column1 datatype,
  column2 datatype,
  column3 datatype,
  FOREIGN KEY (column1) REFERENCES table_name1(column1)
);
```
### How to use NOT NULL and UNIQUE constraints
The NOT NULL constraint specifies that a column must contain a value, while the UNIQUE constraint specifies that each value in a column must be unique.

To add a NOT NULL constraint, you can use the NOT NULL keyword in the CREATE TABLE statement:

```mysql
CREATE TABLE table_name (
  column1 datatype NOT NULL,
  column2 datatype,
  ...
);
```
To add a UNIQUE constraint, you can use the UNIQUE keyword in the CREATE TABLE statement:

```mysql
CREATE TABLE table_name (
  column1 datatype,
  column2 datatype UNIQUE,
  ...
);
```
### How to retrieve data from multiple tables in one request

To retrieve data from multiple tables in one request, you can use JOIN operations. There are several types of JOIN operations, including INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN.

Here is an example of an INNER JOIN:
```mysql
SELECT *
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```
This query returns all rows from both tables where the values in the specified column(s) match.

