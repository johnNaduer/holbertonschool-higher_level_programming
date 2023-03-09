# SQL - Introduction
<p>
This repository is aimed at beginners who want to learn about databases and MySQL. It covers the basics of what a database is, what a relational database is, and how to use SQL to interact with a MySQL database.
</p>

### Table of Contents

- What's a database?
- What's a relational database?
- What does SQL stand for?
- What's MySQL?
- How to create a database in MySQL
- What does DDL and DML stand for?
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries?
- How to use MySQL functions

### What's a database?
A database is an organized collection of data stored and accessed electronically. It can be as simple as a list of names and addresses or as complex as a full-fledged accounting system. Databases are used to store and manage information in a structured way.

### What's a relational database?
A relational database is a type of database that stores data in tables and relationships between those tables. It is the most common type of database used today. Each table represents a specific type of data, and the relationships between the tables are defined by the data itself. For example, a customer table might have a relationship with an order table, where each customer can have many orders.

### What does SQL stand for?
SQL stands for Structured Query Language. It is a programming language used to manage and manipulate relational databases. SQL is used to create, modify, and query databases, and is the standard language used for interacting with relational databases.

### What's MySQL?
MySQL is an open-source relational database management system. It is one of the most widely used databases in the world, and is used by many popular websites and applications. MySQL is known for its ease of use, reliability, and scalability.

### How to create a database in MySQL
To create a database in MySQL, you can use the CREATE DATABASE statement. Here's an example:
```mysql
CREATE DATABASE mydatabase;
```
This will create a new database called mydatabase.

### What does DDL and DML stand for?
DDL stands for Data Definition Language, and DML stands for Data Manipulation Language. DDL is used to create, modify, and delete database objects, such as tables, indexes, and views. DML is used to insert, update, and delete data from tables.

### How to CREATE or ALTER a table
To create a table in MySQL, you can use the CREATE TABLE statement. Here's an example:
```mysql
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
);
```
This will create a new table called customers with three columns: id, name, and email.

### How to SELECT data from a table
To retrieve data from a MySQL table, you can use the SELECT statement. Here's an example:
```mysql
SELECT * FROM users;
```
This statement selects all columns from the users table. You can also specify specific columns to select, filter the results using a WHERE clause, sort the results using ORDER BY, and aggregate data using functions like COUNT, SUM, and AVG.
```mysql
SELECT name, email FROM users WHERE id = 1 ORDER BY created_at DESC;
```
This statement selects only the name and email columns from the users table where the id is equal to 1, and orders the results by the created_at column in descending order.
### How to INSERT, UPDATE or DELETE data
To insert new data into a MySQL table, you can use the INSERT INTO statement. Here's an example:
```mysql
INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
```
This statement inserts a new row into the users table with the name and email values specified.

To update existing data, you can use the UPDATE statement. For example, to update the email address for a specific user:
```mysql
UPDATE users SET email = 'jane@example.com' WHERE name = 'Jane Doe';
```
This statement updates the email column for the row(s) where the name column equals 'Jane Doe'.

To delete data, you can use the DELETE FROM statement. For example, to delete a specific user:
```mysql
DELETE FROM users WHERE id = 5;
```
This statement deletes the row(s) from the users table where the id column equals 5.

