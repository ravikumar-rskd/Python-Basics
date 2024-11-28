# Defining and Calling a Function
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!

# Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# Function with Multiple Parameters
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Bob", 30)  # Output: Hello, Bob! You are 30 years old.

# Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# Function with Default Parameter Value
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!

# Function with Keyword Arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(name="Alice", age=25)  # Output: Hello, Alice! You are 25 years old.
