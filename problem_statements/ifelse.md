Here are **beginner-level problems** for **conditional statements** in Python. Each section contains **3 problems** with their **problem statements, inputs, expected outputs, solutions as code, and test cases**.

---

## **1. Conditional Statements in Python**

### **Problem 1: Checking Even or Odd**
#### **Problem Statement:**
Write a program that checks if a number is **even** or **odd**.

#### **Inputs:**
```python
num = 7
```

#### **Expected Output:**
```
7 is Odd
```

#### **Solution Code:**
```python
num = 7
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
```

#### **Test Cases:**

| Input | Expected Output  |
|-------|------------------|
| 4     | 4 is Even        |
| 7     | 7 is Odd         |
| 10    | 10 is Even       |
| 15    | 15 is Odd        |

---

### **Problem 2: Checking If a Number is Positive, Negative, or Zero**
#### **Problem Statement:**
Write a program to check if a given number is **positive**, **negative**, or **zero**.

#### **Inputs:**
```python
num = -5
```

#### **Expected Output:**
```
-5 is Negative
```

#### **Solution Code:**
```python
num = -5
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print(f"{num} is Zero")
```

#### **Test Cases:**

| Input  | Expected Output    |
|--------|--------------------|
| 5      | 5 is Positive      |
| -3     | -3 is Negative     |
| 0      | 0 is Zero          |
| 12     | 12 is Positive     |

---

### **Problem 3: Grade Evaluation**
#### **Problem Statement:**
Write a program that takes a score as input and prints the corresponding grade based on the following criteria:
- **A** for scores 90 and above
- **B** for scores between 80 and 89
- **C** for scores between 70 and 79
- **D** for scores between 60 and 69
- **F** for scores below 60

#### **Inputs:**
```python
score = 85
```

#### **Expected Output:**
```
Grade: B
```

#### **Solution Code:**
```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

#### **Test Cases:**

| Score | Expected Output |
|-------|-----------------|
| 92    | Grade: A        |
| 85    | Grade: B        |
| 75    | Grade: C        |
| 65    | Grade: D        |
| 50    | Grade: F        |

---

### **Problem 4: Checking Leap Year**
#### **Problem Statement:**
Write a program to check if a given year is a **leap year** or not. A leap year is:
- Divisible by 4, but not divisible by 100, or divisible by 400.

#### **Inputs:**
```python
year = 2020
```

#### **Expected Output:**
```
2020 is a Leap Year
```

#### **Solution Code:**
```python
year = 2020

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
```

#### **Test Cases:**

| Year  | Expected Output          |
|-------|--------------------------|
| 2020  | 2020 is a Leap Year      |
| 1900  | 1900 is not a Leap Year  |
| 2000  | 2000 is a Leap Year      |
| 2024  | 2024 is a Leap Year      |
| 2023  | 2023 is not a Leap Year  |

---

### **Problem 5: Nested If Statements (Age Classification)**
#### **Problem Statement:**
Write a program to classify a person's age into different groups:
- **Child**: Age less than 13
- **Teenager**: Age between 13 and 19
- **Adult**: Age between 20 and 64
- **Senior**: Age 65 and above

#### **Inputs:**
```python
age = 16
```

#### **Expected Output:**
```
Teenager
```

#### **Solution Code:**
```python
age = 16

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 64:
    print("Adult")
else:
    print("Senior")
```

#### **Test Cases:**

| Age  | Expected Output |
|------|-----------------|
| 10   | Child           |
| 15   | Teenager        |
| 30   | Adult           |
| 70   | Senior          |

---

These problems cover basic conditional concepts such as `if`, `elif`, and `else`, as well as using logical operators and nested `if` statements to solve real-world problems.