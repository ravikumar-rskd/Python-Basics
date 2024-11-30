Here are **beginner-level problems** focused on **classes** and **objects** in Python.

---

## **1. Classes and Objects in Python**

### **Problem 1: Creating a Simple Class and Object**
#### **Problem Statement:**
Write a Python class called `Person` with two attributes: `name` and `age`. Then, create an object of this class, assign values to `name` and `age`, and print them.

#### **Inputs:**
```python
name = "Alice"
age = 25
```

#### **Expected Output:**
```
Name: Alice
Age: 25
```

#### **Solution Code:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of Person class
person1 = Person("Alice", 25)

# Printing the attributes
print("Name:", person1.name)
print("Age:", person1.age)
```

#### **Test Cases:**

| Input (name, age) | Expected Output     |
|-------------------|---------------------|
| ("Alice", 25)     | Name: Alice, Age: 25|
| ("Bob", 30)       | Name: Bob, Age: 30  |
| ("Charlie", 22)   | Name: Charlie, Age: 22 |

---

### **Problem 2: Adding Methods to a Class**
#### **Problem Statement:**
Write a class `Car` with attributes `make` and `model`. Also, add a method `display_info()` to print the car's details. Create an object and call this method.

#### **Inputs:**
```python
make = "Toyota"
model = "Corolla"
```

#### **Expected Output:**
```
Car Make: Toyota
Car Model: Corolla
```

#### **Solution Code:**
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print("Car Make:", self.make)
        print("Car Model:", self.model)

# Creating an object of Car class
car1 = Car("Toyota", "Corolla")

# Calling the method
car1.display_info()
```

#### **Test Cases:**

| Input (make, model) | Expected Output          |
|---------------------|--------------------------|
| ("Toyota", "Corolla")| Car Make: Toyota, Car Model: Corolla |
| ("Honda", "Civic")   | Car Make: Honda, Car Model: Civic     |
| ("Ford", "Mustang")  | Car Make: Ford, Car Model: Mustang    |

---

### **Problem 3: Modifying Attributes of an Object**
#### **Problem Statement:**
Write a class `Student` with attributes `name` and `marks`. Create an object and allow modification of the `marks` attribute after the object is created. Print the updated marks.

#### **Inputs:**
```python
name = "John"
marks = 80
```

#### **Expected Output:**
```
Name: John
Marks: 90
```

#### **Solution Code:**
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# Creating an object of Student class
student1 = Student("John", 80)

# Modifying the marks
student1.marks = 90

# Printing updated values
print("Name:", student1.name)
print("Marks:", student1.marks)
```

#### **Test Cases:**

| Input (name, marks) | Updated Marks | Expected Output            |
|---------------------|---------------|----------------------------|
| ("John", 80)        | 90            | Name: John, Marks: 90      |
| ("Alice", 85)       | 92            | Name: Alice, Marks: 92     |
| ("Bob", 78)         | 82            | Name: Bob, Marks: 82       |

---

### **Problem 4: Using `__str__()` Method for String Representation**
#### **Problem Statement:**
Write a class `Book` with attributes `title` and `author`. Implement the `__str__()` method to return a formatted string representation of the book's details. Create an object and print it.

#### **Inputs:**
```python
title = "Python Basics"
author = "John Doe"
```

#### **Expected Output:**
```
Book Title: Python Basics
Book Author: John Doe
```

#### **Solution Code:**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book Title: {self.title}\nBook Author: {self.author}"

# Creating an object of Book class
book1 = Book("Python Basics", "John Doe")

# Printing the object (calls __str__ method)
print(book1)
```

#### **Test Cases:**

| Input (title, author)       | Expected Output                |
|-----------------------------|--------------------------------|
| ("Python Basics", "John Doe")| Book Title: Python Basics, Book Author: John Doe |
| ("Advanced Python", "Jane Smith") | Book Title: Advanced Python, Book Author: Jane Smith |

---

### **Problem 5: Inheritance in Classes**
#### **Problem Statement:**
Write a class `Employee` with attributes `name` and `salary`. Create a class `Manager` that inherits from `Employee` and adds a new attribute `department`. Create an object of `Manager` and print all details.

#### **Inputs:**
```python
name = "Alice"
salary = 50000
department = "HR"
```

#### **Expected Output:**
```
Name: Alice
Salary: 50000
Department: HR
```

#### **Solution Code:**
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

# Creating an object of Manager class
manager1 = Manager("Alice", 50000, "HR")

# Printing the details
print("Name:", manager1.name)
print("Salary:", manager1.salary)
print("Department:", manager1.department)
```

#### **Test Cases:**

| Input (name, salary, department) | Expected Output            |
|----------------------------------|----------------------------|
| ("Alice", 50000, "HR")           | Name: Alice, Salary: 50000, Department: HR |
| ("Bob", 60000, "IT")             | Name: Bob, Salary: 60000, Department: IT |
| ("Charlie", 70000, "Finance")    | Name: Charlie, Salary: 70000, Department: Finance |

---

### **Problem 6: Class Method and Static Method**
#### **Problem Statement:**
Write a class `Circle` with a class method `area()` to calculate the area of a circle given its radius, and a static method `greeting()` to return a greeting message. Create an object and call these methods.

#### **Inputs:**
```python
radius = 5
```

#### **Expected Output:**
```
Area of Circle: 78.5
Greeting: Hello, Welcome to the Circle class!
```

#### **Solution Code:**
```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def area(cls, radius):
        return math.pi * (radius ** 2)

    @staticmethod
    def greeting():
        return "Hello, Welcome to the Circle class!"

# Creating an object of Circle class
circle1 = Circle(5)

# Calling the class method and static method
print(f"Area of Circle: {Circle.area(circle1.radius)}")
print(f"Greeting: {Circle.greeting()}")
```

#### **Test Cases:**

| Input (radius) | Expected Output              |
|----------------|------------------------------|
| 5              | Area of Circle: 78.5, Greeting: Hello, Welcome to the Circle class! |
| 7              | Area of Circle: 153.93804002589985, Greeting: Hello, Welcome to the Circle class! |

---

These problems focus on important **object-oriented concepts** like:

- **Creating classes and objects**
- **Attributes and methods**
- **Class and instance methods**
- **Inheritance**
- **Using `__str__()` for object representation**
- **Static and class methods**

These exercises help beginners understand the basic principles of object-oriented programming in Python.