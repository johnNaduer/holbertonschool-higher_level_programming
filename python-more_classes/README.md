#Python - More Classes and Objects

###Introduction
This guide is a continuation of the basics of classes and objects in Python programming language. If you are new to classes and objects, we recommend that you check out the Python classes and objects guide first.

###Class Variables

A class variable is a variable that belongs to a class, rather than an instance of the class. In other words, it is shared among all instances of the class. You can define class variables using the class keyword and they are usually defined outside of any method.

###Instance Variables

Instance variables are variables that belong to an instance of a class. They can be different for each instance of the class. You can define instance variables inside a method and they are usually set in the __init__ method.

### __str__ and __repr__

The __str__ method is used to define the human-readable representation of an object. It is used when you call the print function on an instance of the class. The __repr__ method is used to define the unambiguous representation of an object. It is used when you use the repr function on an instance of the class or when you display the instance in the interactive console.

###__del__
The __del__ method is used to define what should happen when an instance of the class is deleted. It is called when the reference count of the object reaches zero.

### Conclusion
Classes and objects are a powerful tool for organizing and structuring your code in Python. With the information covered in this guide, you should now have a deeper understanding of classes and objects and how to use them to write better code.

###Illustrative example
![](https://pythondiario.com/wp-content/uploads/2014/10/Definiendo2Bclase2BMascota2Ben2BPython.png)
*reference: pythondiario.com*
