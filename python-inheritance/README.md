#  Python - Inheritance

Inheritance is a fundamental concept in object-oriented programming that allows us to create new classes that are derived from existing classes. The derived class inherits all the attributes and methods of the existing class and can also add new attributes and methods of its own.

In Python, inheritance is implemented using the class keyword. The base class is specified as an argument in the derived class definition, and the derived class inherits all the attributes and methods of the base class.

<p align="center">
  <img src="https://files.realpython.com/media/ic-basic-inheritance.f8dc9ffee4d7.jpg">
</p>
> reference image:
[realpython](https://realpython.com/python3-object-oriented-programming/)



###  Defining a Base Class

A base class can be defined using the class keyword and providing a name for the class. For example:
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic animal sound")
```
###  Defining a Derived Class

A derived class is defined using the class keyword, followed by the name of the derived class, and the name of the base class in parentheses. For example:

```python
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        print("Bark")
```
### Using the Derived Class
Once the derived class has been defined, you can create objects of the derived class and use the attributes and methods of both the base class and the derived class. For example:

```python
dog = Dog("Fido", "Labrador")
print(dog.name) # Output: Fido
print(dog.species) # Output: Dog
print(dog.breed) # Output: Labrador
dog.make_sound() # Output: Bark

cat = Cat("Fluffy", "Persian")
print(cat.name) # Output: Fluffy
print(cat.species) # Output: Cat
print(cat.breed) # Output: Persian
cat.make_sound() # Output: Meow
```
###   dir() function in Python
Prints a list of the module names available in the local namespace. The list will include the names of functions and variables defined in the current script, as well as Python's built-in modules.

### what is isinstance ?
Es una función built-in de Python que permite verificar si un objeto es una instancia de una clase o de una de sus subclases. La función toma dos argumentos: el objeto y la clase que queremos comparar.
