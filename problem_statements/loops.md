Here are **beginner-level problems** for **loops** in Python. Each section contains **3 problems** with their **problem statements, inputs, expected outputs, solutions as code, and test cases**.

---

## **1. Loops in Python**

### **Problem 1: Print Numbers from 1 to N (Using `for` loop)**
#### **Problem Statement:**
Write a program to print all numbers from 1 to a given number `N`.

#### **Inputs:**
```python
N = 5
```

#### **Expected Output:**
```
1
2
3
4
5
```

#### **Solution Code:**
```python
N = 5
for i in range(1, N + 1):
    print(i)
```

#### **Test Cases:**

| Input | Expected Output  |
|-------|------------------|
| 3     | 1, 2, 3          |
| 7     | 1, 2, 3, 4, 5, 6, 7 |
| 10    | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |

---

### **Problem 2: Sum of Numbers (Using `for` loop)**
#### **Problem Statement:**
Write a program to calculate the sum of all numbers from 1 to `N`.

#### **Inputs:**
```python
N = 4
```

#### **Expected Output:**
```
Sum: 10
```

#### **Solution Code:**
```python
N = 4
total = 0
for i in range(1, N + 1):
    total += i
print(f"Sum: {total}")
```

#### **Test Cases:**

| Input | Expected Output  |
|-------|------------------|
| 3     | Sum: 6           |
| 5     | Sum: 15          |
| 6     | Sum: 21          |

---

### **Problem 3: Multiplication Table (Using `for` loop)**
#### **Problem Statement:**
Write a program that prints the multiplication table for a given number `N` from 1 to 10.

#### **Inputs:**
```python
N = 3
```

#### **Expected Output:**
```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

#### **Solution Code:**
```python
N = 3
for i in range(1, 11):
    print(f"{N} x {i} = {N * i}")
```

#### **Test Cases:**

| Input | Expected Output  |
|-------|------------------|
| 2     | 2 x 1 = 2, 2 x 2 = 4, ..., 2 x 10 = 20 |
| 5     | 5 x 1 = 5, 5 x 2 = 10, ..., 5 x 10 = 50 |
| 8     | 8 x 1 = 8, 8 x 2 = 16, ..., 8 x 10 = 80 |

---

## **2. While Loop in Python**

### **Problem 4: Print Numbers from 1 to N (Using `while` loop)**
#### **Problem Statement:**
Write a program that prints numbers from 1 to a given number `N` using a `while` loop.

#### **Inputs:**
```python
N = 5
```

#### **Expected Output:**
```
1
2
3
4
5
```

#### **Solution Code:**
```python
N = 5
i = 1
while i <= N:
    print(i)
    i += 1
```

#### **Test Cases:**

| Input | Expected Output  |
|-------|------------------|
| 3     | 1, 2, 3          |
| 6     | 1, 2, 3, 4, 5, 6 |
| 8     | 1, 2, 3, 4, 5, 6, 7, 8 |

---

### **Problem 5: Factorial Calculation (Using `while` loop)**
#### **Problem Statement:**
Write a program that calculates the factorial of a given number `N` using a `while` loop.

#### **Inputs:**
```python
N = 4
```

#### **Expected Output:**
```
Factorial: 24
```

#### **Solution Code:**
```python
N = 4
factorial = 1
i = 1
while i <= N:
    factorial *= i
    i += 1
print(f"Factorial: {factorial}")
```

#### **Test Cases:**

| Input | Expected Output  |
|-------|------------------|
| 3     | Factorial: 6     |
| 5     | Factorial: 120   |
| 6     | Factorial: 720   |

---

### **Problem 6: Sum of Even Numbers (Using `while` loop)**
#### **Problem Statement:**
Write a program that calculates the sum of all even numbers from 1 to `N` using a `while` loop.

#### **Inputs:**
```python
N = 6
```

#### **Expected Output:**
```
Sum of even numbers: 12
```

#### **Solution Code:**
```python
N = 6
sum_even = 0
i = 2
while i <= N:
    sum_even += i
    i += 2
print(f"Sum of even numbers: {sum_even}")
```

#### **Test Cases:**

| Input | Expected Output  |
|-------|------------------|
| 4     | Sum of even numbers: 6 |
| 8     | Sum of even numbers: 20 |
| 10    | Sum of even numbers: 30 |

---

### **Problem 7: Infinite Loop with Break Condition (Using `while` loop)**
#### **Problem Statement:**
Write a program that continuously asks the user to input a number. If the user inputs `0`, break the loop and print "Exited".

#### **Inputs:**
```python
# User input loop until 0 is entered
# Sample inputs: 5, 3, 0
```

#### **Expected Output:**
```
Exited
```

#### **Solution Code:**
```python
while True:
    num = int(input("Enter a number (0 to exit): "))
    if num == 0:
        print("Exited")
        break
```

#### **Test Cases:**

| Input Sequence     | Expected Output  |
|--------------------|------------------|
| 5, 3, 0            | Exited           |
| 10, 15, 0          | Exited           |
| 8, 6, 3, 0         | Exited           |

---

These problems cover basic loop concepts using both the `for` and `while` loops in Python. They allow beginners to practice iteration, accumulation, and breaking out of loops.

Here are **additional problems** involving the use of `break` and `continue` statements in loops for **beginners**.

---

### **Problem 8: Finding Prime Numbers (Using `break` and `continue`)**
#### **Problem Statement:**
Write a program to find and print the first `N` prime numbers. If a number is divisible by any number other than 1 and itself, skip it using the `continue` statement. If a number is found to be prime, print it. Use `break` to stop after printing `N` prime numbers.

#### **Inputs:**
```python
N = 5
```

#### **Expected Output:**
```
2
3
5
7
11
```

#### **Solution Code:**
```python
N = 5
count = 0
num = 2
while count < N:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
    num += 1
```

#### **Test Cases:**

| Input | Expected Output  |
|-------|------------------|
| 3     | 2, 3, 5          |
| 4     | 2, 3, 5, 7       |
| 6     | 2, 3, 5, 7, 11, 13 |

---

### **Problem 9: Skipping Even Numbers (Using `continue`)**
#### **Problem Statement:**
Write a program that prints all odd numbers from 1 to `N`. Use the `continue` statement to skip even numbers.

#### **Inputs:**
```python
N = 10
```

#### **Expected Output:**
```
1
3
5
7
9
```

#### **Solution Code:**
```python
N = 10
for i in range(1, N + 1):
    if i % 2 == 0:
        continue
    print(i)
```

#### **Test Cases:**

| Input | Expected Output  |
|-------|------------------|
| 7     | 1, 3, 5, 7       |
| 12    | 1, 3, 5, 7, 9, 11 |
| 15    | 1, 3, 5, 7, 9, 11, 13, 15 |

---

### **Problem 10: Stopping After Specific Number (Using `break`)**
#### **Problem Statement:**
Write a program that prints numbers from 1 to `N`, but stops the loop if the number is equal to `X`. Use the `break` statement to stop the loop.

#### **Inputs:**
```python
N = 10
X = 6
```

#### **Expected Output:**
```
1
2
3
4
5
```

#### **Solution Code:**
```python
N = 10
X = 6
for i in range(1, N + 1):
    if i == X:
        break
    print(i)
```

#### **Test Cases:**

| Input (N, X) | Expected Output  |
|--------------|------------------|
| (10, 6)      | 1, 2, 3, 4, 5    |
| (8, 4)       | 1, 2, 3          |
| (15, 10)     | 1, 2, 3, 4, 5, 6, 7, 8, 9 |

---

These problems introduce how `break` and `continue` can be used in loops to control flow—`break` for terminating a loop early and `continue` for skipping specific iterations of the loop.