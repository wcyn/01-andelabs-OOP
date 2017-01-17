# Endangered Species - Python OPP Demonstration

Solving the problem of tracking endangered animals in an animal park using OOP. Demonstrates inheritance, encapsulation, polymorphism and various OOP concepts.

## Getting Started
These instructions should help you run the code on your machine.

### Prerequisites
The code is written in Python3. Some functionality may not work with Python2

### Running the code
In order to run the code, change directory into the project directory and type in this line at the terminal

```
$ python elephant.py
```

## The Base Class

The Base Class or the Parent Class is the `Animal` Class. This class holds generic information concerning animals. Other classes inherit its attributes and methods.

## The Subclass

The Subclass or child class is the `Elephant` Class. This class inherits the basic attributes of an Animal from the `Animal` parent class.

## Inheritance
This is when a Class takes up the non-private attributes and methods of another class. It prevents a lot of repetition, especially when different object with some similar properties need to be used. In this case, the Elephant Class takes up the properties of the `Animal` base class.

## Encapsulation
This is done in order to prevent sensitive data from being accessed by outer classes. In python, this is done by prefixing the attribute or method with a `__`. 

For example, in  the `Animal` class, the `name` and `animal_class` attributes are private attributes and can only be accessed by the `Animal` class, but not by its subclass `Elephant`. 
The method `testEncapsulation()` has been used to demonstrate this.

## Polymorphism
This is achieved when a Subclass overrides the attributes of the Base class when an instance is created. 
The method `showPolymorphism()` demonstrates this behaviour

