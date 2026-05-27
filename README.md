# Geometry Shapes Area & Perimeter Calculator

A Python-based object-oriented programming (OOP) system designed to calculate the area and perimeter of various geometric shapes.

## Features
* **OOP Architecture:** Built using a base `Shape` class and specific sub-classes for each geometric form.
* **Supported Shapes:** Rectangle, Square, Triangle, Circle, and Regular Hexagon.
* **Input Validation:** Strict error handling for data types, negative numbers, and zeros.
* **Polymorphism:** Utilizing standard dunder methods (`__str__`) for output display, and advanced dunder methods (`__eq__`, `__gt__`, `__lt__`, `__add__`) for shape comparison and area summation.

## Project Structure
```text
area_calculator/
│
├── main.py          # Application entry point & test cases
├── calculator.py    # Base Shape class & input validation
├── rectangle.py     # Rectangle class
├── square.py        # Square class (inherits from Rectangle)
├── triangle.py      # Triangle class
├── circle.py        # Circle class
└── hexagon.py       # Regular Hexagon class