Here are problems based on the **data types concept** in Python, complete with problem statements, inputs, expected outputs, solutions, and test cases for beginners.

---

### **1. Identify Data Types**
#### **Problem Statement:**
Write a program that takes inputs of different data types (integer, float, string, boolean) and prints their types.

#### **Inputs:**
```python
value1 = 42
value2 = 3.14
value3 = "Python"
value4 = True
```

#### **Expected Output:**
```
42 is of type <class 'int'>
3.14 is of type <class 'float'>
Python is of type <class 'str'>
True is of type <class 'bool'>
```

#### **Solution Code:**
```python
value1 = 42
value2 = 3.14
value3 = "Python"
value4 = True

values = [value1, value2, value3, value4]
for val in values:
    print(f"{val} is of type {type(val)}")
```

#### **Test Cases:**
| Input Value | Expected Type      |
|-------------|--------------------|
| 42          | `<class 'int'>`   |
| 3.14        | `<class 'float'>` |
| "Python"    | `<class 'str'>`   |
| True        | `<class 'bool'>`  |

---

### **2. Convert Data Types**
#### **Problem Statement:**
Write a program that converts:
1. Integer to float.
2. Float to integer.
3. String to integer.
4. Integer to string.

#### **Inputs:**
```python
num1 = 5
num2 = 3.14
num3 = "42"
```

#### **Expected Output:**
```
Integer to float: 5.0
Float to integer: 3
String to integer: 42
Integer to string: "5"
```

#### **Solution Code:**
```python
num1 = 5
num2 = 3.14
num3 = "42"

print(f"Integer to float: {float(num1)}")
print(f"Float to integer: {int(num2)}")
print(f"String to integer: {int(num3)}")
print(f"Integer to string: \"{str(num1)}\"")
```

#### **Test Cases:**
| Input Value | Conversion       | Expected Output |
|-------------|------------------|-----------------|
| 5           | int → float      | 5.0             |
| 3.14        | float → int      | 3               |
| "42"        | str → int        | 42              |
| 5           | int → str        | "5"             |

---

### **3. Length of a String**
#### **Problem Statement:**
Write a program to find the length of a given string.

#### **Inputs:**
```python
text = "Hello, Python!"
```

#### **Expected Output:**
```
The length of the string is: 14
```

#### **Solution Code:**
```python
text = "Hello, Python!"
length = len(text)
print(f"The length of the string is: {length}")
```

#### **Test Cases:**
| Input String       | Expected Length |
|---------------------|-----------------|
| "Hello, Python!"    | 14              |
| "Data Types"        | 10              |

---

### **4. Find the Largest Number**
#### **Problem Statement:**
Write a program to find the largest number among three numbers.

#### **Inputs:**
```python
a = 15
b = 27
c = 12
```

#### **Expected Output:**
```
The largest number is: 27
```

#### **Solution Code:**
```python
a = 15
b = 27
c = 12
largest = max(a, b, c)
print(f"The largest number is: {largest}")
```

#### **Test Cases:**
| Input Values      | Expected Output |
|-------------------|-----------------|
| 15, 27, 12        | 27              |
| 5, 10, 20         | 20              |

---

### **5. String Operations**
#### **Problem Statement:**
Write a program to perform the following string operations:
1. Convert the string to uppercase.
2. Find if a substring exists in the string.
3. Replace a word in the string.

#### **Inputs:**
```python
string = "I love Python programming"
substring = "Python"
word_to_replace = "Python"
replacement_word = "JavaScript"
```

#### **Expected Output:**
```
Uppercase: I LOVE PYTHON PROGRAMMING
Substring exists: True
Modified string: I love JavaScript programming
```

#### **Solution Code:**
```python
string = "I love Python programming"
substring = "Python"
word_to_replace = "Python"
replacement_word = "JavaScript"

print(f"Uppercase: {string.upper()}")
print(f"Substring exists: {substring in string}")
print(f"Modified string: {string.replace(word_to_replace, replacement_word)}")
```

#### **Test Cases:**
| Input String                      | Substring | Expected Output                            |
|-----------------------------------|-----------|--------------------------------------------|
| "I love Python programming"       | "Python"  | True, "I LOVE PYTHON PROGRAMMING"          |
| "Learning is fun"                 | "Python"  | False, "LEARNING IS FUN"                   |

---

### **6. Check Even or Odd**
#### **Problem Statement:**
Write a program to check whether a given number is even or odd.

#### **Inputs:**
```python
number = 42
```

#### **Expected Output:**
```
42 is an even number.
```

#### **Solution Code:**
```python
number = 42
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
```

#### **Test Cases:**
| Number | Expected Output          |
|--------|--------------------------|
| 42     | 42 is an even number.    |
| 15     | 15 is an odd number.     |

---

### **7. Float Operations**
#### **Problem Statement:**
Write a program to calculate the square and square root of a float.

#### **Inputs:**
```python
num = 4.0
```

#### **Expected Output:**
```
Square: 16.0
Square root: 2.0
```

#### **Solution Code:**
```python
num = 4.0
square = num ** 2
square_root = num ** 0.5

print(f"Square: {square}")
print(f"Square root: {square_root}")
```

#### **Test Cases:**
| Number | Square | Square Root |
|--------|--------|-------------|
| 4.0    | 16.0   | 2.0         |
| 9.0    | 81.0   | 3.0         |

---

### **8. Boolean Operations**
#### **Problem Statement:**
Write a program to check if two numbers are equal and if the first number is greater than the second.

#### **Inputs:**
```python
num1 = 10
num2 = 20
```

#### **Expected Output:**
```
Are numbers equal? False
Is the first number greater? False
```

#### **Solution Code:**
```python
num1 = 10
num2 = 20

print(f"Are numbers equal? {num1 == num2}")
print(f"Is the first number greater? {num1 > num2}")
```

#### **Test Cases:**
| num1 | num2 | Equal | Greater |
|------|------|-------|---------|
| 10   | 20   | False | False   |
| 30   | 30   | True  | False   |


---

These advanced problems cover nested data structures, list comprehensions, set operations, and more. Let me know if you need any further elaboration! 😊
