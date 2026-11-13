
# Library Management System

## How to Run

Run the following command from the project folder:

```bash
python3 main.py
```

## Reflection Questions

### 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is an abstract class because it provides a common structure and behaviour for all library items. It requires every child class to implement the `late_fee()` method. If DVD does not implement `late_fee()`, Python considers DVD an abstract class and raises a `TypeError` when we try to create a DVD object.

### 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

When we try to access `item.__available` from outside the class, Python raises an `AttributeError` because the double underscore makes the attribute private through name mangling. We use `is_available()` instead because it provides controlled access to check whether an item is available without directly accessing its private attribute.

### 3. What is the difference between LibraryItem.total_items and self.title?

`LibraryItem.total_items` is a class attribute shared by all objects of the LibraryItem class and its child classes. It keeps track of the total number of library items created. On the other hand, `self.title` is an instance attribute, meaning each object has its own title value.
