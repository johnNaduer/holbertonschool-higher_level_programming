# Python Input/Output
Python provides a simple way to work with input and output data in files. Files can be text or binary, and Python provides tools for reading and writing to both types of files.

<p align="center">
<img src="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/Basic-Input-Output-and-String-Formatting-in-Python_Watermarked.65ba5b535841.jpg&w=960&sig=e5e7029a0e36ca9d8123c7b47cfe8ce9075d653e">
</p>
> "reference image", [realpython](https://realpython.com/python-input-output/)。

### Opening and writing files
You can open a file in Python using the open() function. The open()function takes two arguments: the file name and the access mode of the file. The access modes include "r "for read, "w "for write and "a "for append to the end of the file.

Here is an example of code that opens a text file in write mode and writes a string to the file:

```python
file = open("output.txt", "w")
file.write("Hello, World!")
file.close()
```
In this example, the file "output.txt" is opened in write mode ("w") and the string "Hello, World!" is written to the file. It is important to close the file after you have finished working with it to free up system resources.

### File reading
You can read a file in Python using the read()method on the file object. The read()method will read the entire contents of the file and return it as a single string.

Here is an example of code that opens a text file in read mode and displays its contents in the console:

```python
file = open("input.txt", "r")
contents = file.read()
print(contents)
file.close()
```
In this example, the file "input.txt" is opened in read mode ("r") and all contents of the file are read. The contents are then printed on the console.
