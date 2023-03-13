# Python - Object-relational mapping

Certainly! Object-Relational Mapping (ORM) is a popular technique used to interact with databases from Python code. In simple terms, an ORM maps the structure of a database to the structure of Python objects, allowing you to work with data in a more natural way.

There are several popular ORM libraries available for Python, such as SQLAlchemy, Django ORM, and Peewee. These libraries provide a range of features to make working with databases easier and more intuitive, including:

Creating database tables from Python classes and vice versa
Mapping object attributes to database columns
Generating SQL queries automatically based on Python method calls
Caching and optimizing queries for improved performance
Using an ORM can have several benefits, such as:

Reducing the amount of boilerplate code needed to interact with the database
Improving the readability and maintainability of the code by providing a more intuitive interface
Making it easier to switch between different database systems, since the ORM abstracts away some of the differences in syntax and behavior
When using an ORM, it's important to understand the underlying database structure and SQL syntax, as well as the limitations and trade-offs of the ORM itself. However, for many projects, an ORM can be a powerful tool for managing database interactions and simplifying development.


## Connecting to a MySQL database from a Python script

In order to connect to a MySQL database from a Python script, you will need to use a connector module. One popular choice is the mysql-connector-python module, which can be installed using pip:

```python
pip install mysql-connector-python
```
Once the module is installed, you can use it in your script to establish a connection to the MySQL database. Here is an example:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

print(mydb)
```
This code creates a connection to a MySQL database running on the same machine, using the specified username and password. The database parameter specifies which database to use. You can then use the mydb object to execute queries on the database.

## SELECTing rows from a MySQL table using Python

Once you have established a connection to a MySQL database using Python, you can use SQL queries to retrieve data from tables in the database. Here is an example of how to retrieve all rows from a table using a SELECT statement:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM yourtable")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```
This code creates a cursor object, which is used to execute SQL queries. The execute() method is used to execute a SELECT statement, and the fetchall() method is used to retrieve all rows returned by the query. The rows are then printed one by one in a loop.

## INSERTing rows into a MySQL table using Python

To insert rows into a MySQL table using Python, you can use the INSERT statement. Here is an example:

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO yourtable (column1, column2, column3) VALUES (%s, %s, %s)"
val = ("value1", "value2", "value3")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```
This code creates an INSERT statement that inserts values into the specified columns in the table. The execute() method is used to execute the query, with the values to be inserted provided as a tuple. The commit() method is used to commit the changes to the database, and the rowcount attribute of the cursor object is used to print the number of rows that were inserted.

 ### What is an ORM?
 An ORM, or Object-Relational Mapping, is a programming technique that allows you to work with databases using an object-oriented interface. It provides a way to map the structure of a database to the structure of objects in your code, so you can work with the data in a more natural way.

With an ORM, you define classes in your code that represent tables in the database. Each instance of the class represents a row in the table, and the properties of the instance correspond to the columns of the row. You can then use methods on the instances to perform CRUD operations on the database.

ORMs can make it easier to work with databases in many ways, such as:

- Providing a more natural, object-oriented interface to the data
- Abstracting away some of the details of the underlying SQL queries


