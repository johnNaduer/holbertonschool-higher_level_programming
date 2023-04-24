# JavaScript - Objects, Scopes and Closures

## Why JavaScript programming is amazing
JavaScript is a versatile and powerful programming language that has become ubiquitous in modern web development. Here are just a few reasons why it's amazing:

- JavaScript runs natively in web browsers, allowing you to create dynamic, interactive web pages with ease.
- It can also be used on the server side with platforms like Node.js, enabling full-stack development with a single language.
- JavaScript has a huge and active developer community, with an abundance of libraries and frameworks available for any task you can imagine.
- The language is constantly evolving, with new features and updates being added regularly to improve the language and its capabilities.
## How to create an object in JavaScript
In JavaScript, you can create objects using either the Object() constructor or the literal notation. Here's an example of each:
```javascript
let myObject = new Object();
myObject.prop1 = "Hello";
myObject.prop2 = "World";
let myOtherObject = {
  prop1: "Goodbye",
  prop2: "World"
 ```
## What this means
In JavaScript, this refers to the current object that the code is being executed in. It can be used in a number of contexts, such as in object methods to refer to the object itself, or in event handlers to refer to the element that triggered the event.
For example:

```javascript
let myObject = {
  name: "John",
  sayName: function() {
    console.log("My name is " + this.name);
  }
};
myObject.sayName(); 
```
## What undefined means
In JavaScript, undefined is a primitive value that is assigned to a variable that has been declared but has not been initialized with a value. It can also be returned by a function that does not explicitly return a value.

For example:
```javascript
let myVar;
console.log(myVar); // Output: undefined

function myFunction() {
  // no return statement
}

console.log(myFunction()); // Output: undefined
```
## Why variable type and scope is important
In JavaScript, variable type and scope are important because they affect how the code behaves and can prevent unexpected errors.

Variable type refers to whether a variable is a string, number, boolean, object, or other data type. This can affect how the variable is used and the operations that can be performed on it.

Variable scope refers to where a variable can be accessed in the code. Global variables can be accessed from anywhere, while local variables are only accessible within the block or function where they are defined. Proper scoping of variables can prevent issues like naming conflicts and data corruption.
## What is a closure
A closure is a function that has access to variables in its outer (enclosing) scope, even after the outer function has returned. This allows for powerful and flexible programming techniques, such as creating private variables and functions.

For example:
```javascript
function counter() {
  let count = 0;

  function increment() {
    count++;
    console.log(count);
  }

  return increment;
}

let myCounter = counter();
myCounter(); // Output: 1
myCounter(); // Output: 2
```
