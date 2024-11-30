Here are some beginner-level problems to help you practice and understand the concept of variables in Python:

---

### **1. Simple Variable Assignment**
**Problem:** Assign your name to a variable `name`, your age to a variable `age`, and your city to a variable `city`. Then, print a sentence like:  
*"Hello, my name is [name], I am [age] years old, and I live in [city]."*

---

### **2. Swapping Variables**
**Problem:** Given two variables `a = 5` and `b = 10`, swap their values so that `a = 10` and `b = 5`, and print the result.

---

### **3. Variable Types**
**Problem:** Assign different types of data to variables:  
- `integer_num` = 42 (integer)  
- `float_num` = 3.14 (float)  
- `string_text` = "Python" (string)  
- `boolean_val` = True (boolean)  

Print the values and their types using `type()`.

---

### **4. Arithmetic with Variables**
**Problem:**  
Assign two numbers to variables `x` and `y`. Perform the following operations and print the results:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus (remainder)

---

### **5. Updating Variables**
**Problem:**  
Write a program where a variable `count` starts at `0`.  
1. Increment it by 5.  
2. Multiply it by 2.  
3. Subtract 3.  
Print the final value of `count`.

---

### **6. User Input and Variables**
**Problem:** Write a program that asks the user for their name and favorite number. Store them in variables and print a message like:  
*"Hi [name]! Your favorite number is [number]."*

---

### **7. String Concatenation**
**Problem:**  
Create two variables `first_name` and `last_name`, and assign them your first and last names. Combine them into a single variable `full_name` and print it.

---

### **8. Reassigning Variables**
**Problem:**  
Assign a value of `10` to a variable `number`. Then reassign it with `number = number + 5`. Print the updated value of `number`.

---

### **9. Calculating the Area of a Circle**
**Problem:**  
Assign a radius to a variable `radius`. Calculate the area of the circle using the formula \( \text{Area} = \pi \times \text{radius}^2 \), and print the result. Use `3.14` as the value of π.

---

### **10. Temperature Conversion**
**Problem:**  
Write a program where the user enters a temperature in Celsius. Store it in a variable `celsius`. Convert it to Fahrenheit using the formula:  
\[ \text{Fahrenheit} = (\text{Celsius} \times 9/5) + 32 \]  
Print the result.

---

### **11. Multiple Assignments**
**Problem:**  
Assign values `10`, `20`, and `30` to variables `a`, `b`, and `c` in one line using multiple assignment. Print their values.

---

### **12. Using Variables in Conditions**
**Problem:**  
Write a program that assigns a number to a variable `num`. Check if `num` is greater than 10. If true, print `"Number is greater than 10"`; otherwise, print `"Number is 10 or less"`.

---



Here’s a detailed version of the problems with inputs, expected outputs, solutions, and test cases for deeper testing.

---

### **1. Simple Variable Assignment**
#### **Problem:**
Assign your name, age, and city to variables and print a formatted sentence.

#### **Inputs:**
- `name = "Ravi"`
- `age = 23`
- `city = "Vizag"`

#### **Expected Output:**
```
Hello, my name is Ravi, I am 23 years old, and I live in Vizag.
```

#### **Solution Code:**
```python
name = "Ravi"
age = 23
city = "Vizag"
print(f"Hello, my name is {name}, I am {age} years old, and I live in {city}.")
```

#### **Test Cases:**
| Name    | Age | City       | Expected Output                                         |
|---------|-----|------------|---------------------------------------------------------|
| Ravi    | 23  | Vizag      | Hello, my name is Ravi, I am 23 years old, and I live in Vizag. |
| Sita    | 30  | Hyderabad  | Hello, my name is Sita, I am 30 years old, and I live in Hyderabad. |

---

### **2. Swapping Variables**
#### **Inputs:**
- `a = 5`
- `b = 10`

#### **Expected Output:**
```
Before swapping: a = 5, b = 10
After swapping: a = 10, b = 5
```

#### **Solution Code:**
```python
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")
```

#### **Test Cases:**
| `a` | `b`  | Expected Output                                    |
|-----|-------|---------------------------------------------------|
| 5   | 10    | Before swapping: a = 5, b = 10; After swapping: a = 10, b = 5 |
| 20  | 35    | Before swapping: a = 20, b = 35; After swapping: a = 35, b = 20 |

---

### **3. Variable Types**
#### **Inputs:**
- `integer_num = 42`
- `float_num = 3.14`
- `string_text = "Python"`
- `boolean_val = True`

#### **Expected Output:**
```
42 is of type <class 'int'>
3.14 is of type <class 'float'>
Python is of type <class 'str'>
True is of type <class 'bool'>
```

#### **Solution Code:**
```python
integer_num = 42
float_num = 3.14
string_text = "Python"
boolean_val = True

variables = [integer_num, float_num, string_text, boolean_val]
for var in variables:
    print(f"{var} is of type {type(var)}")
```

#### **Test Cases:**
| Variable         | Value        | Expected Type        |
|-------------------|--------------|----------------------|
| `integer_num`    | 42           | `<class 'int'>`      |
| `float_num`      | 3.14         | `<class 'float'>`    |
| `string_text`    | "Python"     | `<class 'str'>`      |
| `boolean_val`    | True         | `<class 'bool'>`     |

---

### **4. Arithmetic with Variables**
#### **Inputs:**
- `x = 15`
- `y = 4`

#### **Expected Output:**
```
Addition: 19
Subtraction: 11
Multiplication: 60
Division: 3.75
Modulus: 3
```

#### **Solution Code:**
```python
x = 15
y = 4

print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print(f"Modulus: {x % y}")
```

#### **Test Cases:**
| `x`  | `y` | Addition | Subtraction | Multiplication | Division | Modulus |
|------|-----|----------|-------------|----------------|----------|---------|
| 15   | 4   | 19       | 11          | 60             | 3.75     | 3       |
| 20   | 7   | 27       | 13          | 140            | 2.857    | 6       |

---

### **5. Updating Variables**
#### **Inputs:**
- `count = 0`

#### **Expected Output:**
```
Final count: 7
```

#### **Solution Code:**
```python
count = 0
count += 5
count *= 2
count -= 3
print(f"Final count: {count}")
```

#### **Test Cases:**
| Initial Count | Increment | Multiply | Subtract | Final Count |
|---------------|-----------|----------|----------|-------------|
| 0             | +5        | ×2       | -3       | 7           |
| 10            | +5        | ×2       | -3       | 27          |

---

### **6. User Input and Variables**
#### **Inputs:**
- Name: `Ravi`
- Favorite Number: `42`

#### **Expected Output:**
```
Hi Ravi! Your favorite number is 42.
```

#### **Solution Code:**
```python
name = input("Enter your name: ")
fav_number = input("Enter your favorite number: ")
print(f"Hi {name}! Your favorite number is {fav_number}.")
```

#### **Test Cases:**
| Name     | Favorite Number | Expected Output                    |
|----------|------------------|------------------------------------|
| Ravi     | 42              | Hi Ravi! Your favorite number is 42. |
| Sita     | 99              | Hi Sita! Your favorite number is 99. |

---

### **7. String Concatenation**
#### **Problem Statement:**
Combine a first name and last name into a full name.

#### **Inputs:**
- `first_name = "Ravi"`
- `last_name = "Pilaka"`

#### **Expected Output:**
```
Full name: Ravi Pilaka
```

#### **Solution Code:**
```python
first_name = "Ravi"
last_name = "Pilaka"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
```

#### **Test Cases:**
| First Name | Last Name  | Expected Output       |
|------------|------------|-----------------------|
| Ravi       | Pilaka     | Full name: Ravi Pilaka |
| John       | Doe        | Full name: John Doe   |

---

### **8. Reassigning Variables**
#### **Problem Statement:**
Update a variable’s value by adding 5 to its current value.

#### **Inputs:**
- `number = 10`

#### **Expected Output:**
```
Updated number: 15
```

#### **Solution Code:**
```python
number = 10
number = number + 5
print(f"Updated number: {number}")
```

#### **Test Cases:**
| Initial Value | Updated Value |
|---------------|---------------|
| 10            | 15            |
| 25            | 30            |

---

### **9. Calculating the Area of a Circle**
#### **Problem Statement:**
Calculate the area of a circle given its radius.

#### **Inputs:**
- `radius = 7`

#### **Expected Output:**
```
Area of the circle: 153.86
```

#### **Solution Code:**
```python
radius = 7
pi = 3.14
area = pi * (radius ** 2)
print(f"Area of the circle: {area}")
```

#### **Test Cases:**
| Radius | Expected Area |
|--------|---------------|
| 7      | 153.86        |
| 10     | 314.0         |

---

### **10. Temperature Conversion**
#### **Problem Statement:**
Convert a given temperature in Celsius to Fahrenheit.

#### **Inputs:**
- `celsius = 25`

#### **Expected Output:**
```
Temperature in Fahrenheit: 77.0
```

#### **Solution Code:**
```python
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")
```

#### **Test Cases:**
| Celsius | Fahrenheit |
|---------|------------|
| 25      | 77.0       |
| 0       | 32.0       |

---

### **11. Multiple Assignments**
#### **Problem Statement:**
Assign multiple values to multiple variables in one line.

#### **Inputs:**
- `a, b, c = 10, 20, 30`

#### **Expected Output:**
```
a = 10, b = 20, c = 30
```

#### **Solution Code:**
```python
a, b, c = 10, 20, 30
print(f"a = {a}, b = {b}, c = {c}")
```

#### **Test Cases:**
| Values Assigned | Expected Output           |
|-----------------|---------------------------|
| 10, 20, 30      | a = 10, b = 20, c = 30    |
| 5, 15, 25       | a = 5, b = 15, c = 25     |

---

### **12. Using Variables in Conditions**
#### **Problem Statement:**
Check if a number is greater than 10 and print a corresponding message.

#### **Inputs:**
- `num = 15`

#### **Expected Output:**
```
Number is greater than 10
```

#### **Solution Code:**
```python
num = 15
if num > 10:
    print("Number is greater than 10")
else:
    print("Number is 10 or less")
```

#### **Test Cases:**
| Number | Expected Output            |
|--------|-----------------------------|
| 15     | Number is greater than 10   |
| 8      | Number is 10 or less        |

---

### **Summary of All Problems**
This set of problems introduces beginners to:
1. Variable assignment.
2. Data types and basic operations.
3. String manipulation.
4. Input/output handling.
5. Arithmetic, conditionals, and updating values.
