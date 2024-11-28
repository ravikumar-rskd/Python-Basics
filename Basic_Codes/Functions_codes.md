Here are **basic Python codes** to help understand the **Functions** topic, including defining and calling functions, parameters and arguments, return values, lambda functions, and using `*args` and `**kwargs`. I'll also provide **fill-in-the-blank exercises** for each concept.

---

### **Functions**

**1. Defining and Calling a Function**
```python
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!
```

**2. Function with Parameters**
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

**3. Function with Multiple Parameters**
```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Bob", 30)  # Output: Hello, Bob! You are 30 years old.
```

**4. Function with Return Value**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

**5. Function with Default Parameter Value**
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!
```

**6. Function with Keyword Arguments**
```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(name="Alice", age=25)  # Output: Hello, Alice! You are 25 years old.
```

---

### **Lambda Functions**

**7. Basic Lambda Function**
```python
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8
```

**8. Lambda Function with Conditional Expression**
```python
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(4))  # Output: Even
print(check_even(5))  # Output: Odd
```

---

### **Using *args and **kwargs**

**9. Using *args (Variable Number of Arguments)**
```python
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3)  # Output: 1 2 3
print_numbers(10, 20, 30, 40)  # Output: 10 20 30 40
```

**10. Using **kwargs (Keyword Arguments)**
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)  
# Output:
# name: Alice
# age: 25
```

**11. Using *args and **kwargs Together**
```python
def greet_info(*args, **kwargs):
    for arg in args:
        print(f"Hello, {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet_info("Alice", "Bob", age=25, city="New York")  
# Output:
# Hello, Alice
# Hello, Bob
# age: 25
# city: New York
```
Here are **10 additional basic codes** to further practice the concepts related to **functions**, **lambda functions**, and **args/kwargs**.

---

### **Functions - More Practice**

**12. Function with Multiple Return Values**
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([5, 2, 9, 1, 7])
print(min_val, max_val)  # Output: 1 9
```

**13. Recursive Function (Factorial)**
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120
```

**14. Function with Variable Number of Keyword Arguments**
```python
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Alice", age=30, city="New York")
# Output: 
# name: Alice
# age: 30
# city: New York
```

**15. Function with Default Arguments**
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))  # Output: 9 (default exponent is 2)
print(power(3, 3))  # Output: 27 (exponent is 3)
```

**16. Function as an Argument**
```python
def multiply(a, b):
    return a * b

def calculate(func, x, y):
    return func(x, y)

result = calculate(multiply, 4, 5)
print(result)  # Output: 20
```

---

### **Lambda Functions - More Practice**

**17. Sorting with Lambda Function**
```python
students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
students.sort(key=lambda x: x[1])  # Sort by second element (score)
print(students)  # Output: [('Bob', 75), ('Charlie', 85), ('Alice', 90)]
```

**18. Using Lambda to Filter Even Numbers**
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

**19. Using Lambda for Map Operation**
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```

**20. Sorting a List of Strings with Lambda**
```python
words = ["apple", "orange", "banana", "kiwi"]
words.sort(key=lambda x: len(x))  # Sort by length of the word
print(words)  # Output: ['kiwi', 'apple', 'banana', 'orange']
```

---

### **Using *args and **kwargs - More Practice**

**21. Using *args with Additional Arguments**
```python
def sum_numbers(first, *args):
    total = first
    for num in args:
        total += num
    return total

result = sum_numbers(10, 5, 20, 30)
print(result)  # Output: 65 (10 + 5 + 20 + 30)
```

**22. Using **kwargs to Collect Arbitrary Keyword Arguments**
```python
def describe_pet(pet_name, **kwargs):
    print(f"Pet Name: {pet_name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_pet("Buddy", type="Dog", breed="Golden Retriever", age=3)
# Output:
# Pet Name: Buddy
# type: Dog
# breed: Golden Retriever
# age: 3
```

**23. Using *args and **kwargs in a Function**
```python
def display_info(*args, **kwargs):
    for arg in args:
        print(f"Argument: {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info("Alice", "Bob", city="Paris", age=30)
# Output:
# Argument: Alice
# Argument: Bob
# city: Paris
# age: 30
```

**24. Function Returning a Lambda Using *args**
```python
def create_multiplier(*args):
    return lambda x: x * sum(args)

multiply_by_sum = create_multiplier(2, 3, 4)
print(multiply_by_sum(5))  # Output: 45 (2 + 3 + 4 = 9, 9 * 5 = 45)
```

---

These **10 additional codes** give you more examples and exercises to understand **functions**, **lambda functions**, and the use of `*args` and `**kwargs`. The examples cover a variety of use cases, 
from recursion to higher-order functions and sorting. You can experiment with these codes to solidify your understanding. Let me know if you need more examples or further clarification!

---

### **Fill in the blanks to practice**

---

### **Defining and Calling Functions**

**1. Defining a Function**
```python
def ____():
    print("Hello, Python!")
    
____()  # Should print: Hello, Python!
```

**2. Function with Parameters**
```python
def greet(name):
    print(f"Hello, ____!")

greet("Charlie")  # Should print: Hello, Charlie!
```

**3. Function with Return Value**
```python
def multiply(a, b):
    return a ____ b

result = multiply(4, 3)
print(result)  # Should print: 12
```

---

### **Lambda Functions**

**4. Basic Lambda Function**
```python
add = lambda x, y: x ____ y
print(add(7, 2))  # Should print: 9
```

**5. Lambda with Conditional Expression**
```python
check_odd_even = lambda x: "Even" if x ____ 2 == 0 else "Odd"
print(check_odd_even(6))  # Should print: Even
```

---

### **Using *args and **kwargs**

**6. Using *args**
```python
def print_elements(*args):
    for element in ____:
        print(element)

print_elements(1, 2, 3, 4)  # Should print: 1 2 3 4
```

**7. Using **kwargs**
```python
def print_data(**kwargs):
    for key, value in kwargs.____():
        print(f"{key}: {value}")

print_data(name="David", age=28)  # Should print:
# name: David
# age: 28
```

**8. Using *args and **kwargs Together**
```python
def show_details(*args, **kwargs):
    for arg in args:
        print(f"Argument: {arg}")
    for key, value in kwargs.____():
        print(f"{key}: {value}")

show_details("Alice", "Bob", city="Paris", age=30)  
# Should print:
# Argument: Alice
# Argument: Bob
# city: Paris
# age: 30
```

---

These examples cover **functions**, **lambda functions**, and the use of `*args` and `**kwargs`. The **fill-in-the-blank** exercises allow you to practice defining functions, using variable-length arguments, and understanding function return values. Let me know if you would like solutions or further explanations!
