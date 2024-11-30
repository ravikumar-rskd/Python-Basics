Here’s a collection of **beginner-level problems** for the **operators concept** in Python, covering **arithmetic, assignment, comparison, and logical operators**. Each problem includes a **problem statement, inputs, expected output, solution code, and test cases**.

---

### **1. Arithmetic Operators**
#### **Problem Statement:**
Write a program to perform basic arithmetic operations: addition, subtraction, multiplication, division, modulus, exponentiation, and floor division on two numbers.

#### **Inputs:**
```python
num1 = 12
num2 = 5
```

#### **Expected Output:**
```
Addition: 17
Subtraction: 7
Multiplication: 60
Division: 2.4
Modulus: 2
Exponentiation: 248832
Floor Division: 2
```

#### **Solution Code:**
```python
num1 = 12
num2 = 5

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")
print(f"Exponentiation: {num1 ** num2}")
print(f"Floor Division: {num1 // num2}")
```

#### **Test Cases:**
| Num1 | Num2 | Addition | Subtraction | Multiplication | Division | Modulus | Exponentiation | Floor Division |
|------|------|----------|-------------|----------------|----------|---------|----------------|----------------|
| 12   | 5    | 17       | 7           | 60             | 2.4      | 2       | 248832         | 2              |
| 15   | 3    | 18       | 12          | 45             | 5.0      | 0       | 3375           | 5              |

---

### **2. Assignment Operators**
#### **Problem Statement:**
Write a program to demonstrate assignment operators by incrementing, decrementing, and multiplying a number.

#### **Inputs:**
```python
num = 10
```

#### **Expected Output:**
```
Initial value: 10
After increment: 15
After decrement: 10
After multiplication: 30
```

#### **Solution Code:**
```python
num = 10
print(f"Initial value: {num}")

num += 5
print(f"After increment: {num}")

num -= 5
print(f"After decrement: {num}")

num *= 3
print(f"After multiplication: {num}")
```

#### **Test Cases:**
| Initial Num | Increment By | Decrement By | Multiply By | Expected Output |
|-------------|--------------|--------------|-------------|-----------------|
| 10          | 5            | 5            | 3           | 10 → 15 → 10 → 30 |
| 20          | 10           | 5            | 2           | 20 → 30 → 25 → 50 |

---

### **3. Comparison Operators**
#### **Problem Statement:**
Write a program to compare two numbers using comparison operators (`>`, `<`, `==`, `!=`, `>=`, `<=`).

#### **Inputs:**
```python
num1 = 15
num2 = 20
```

#### **Expected Output:**
```
Is 15 > 20? False
Is 15 < 20? True
Is 15 == 20? False
Is 15 != 20? True
Is 15 >= 20? False
Is 15 <= 20? True
```

#### **Solution Code:**
```python
num1 = 15
num2 = 20

print(f"Is {num1} > {num2}? {num1 > num2}")
print(f"Is {num1} < {num2}? {num1 < num2}")
print(f"Is {num1} == {num2}? {num1 == num2}")
print(f"Is {num1} != {num2}? {num1 != num2}")
print(f"Is {num1} >= {num2}? {num1 >= num2}")
print(f"Is {num1} <= {num2}? {num1 <= num2}")
```

#### **Test Cases:**
| Num1 | Num2 | >       | <       | ==      | !=      | >=      | <=      |
|------|------|---------|---------|---------|---------|---------|---------|
| 15   | 20   | False   | True    | False   | True    | False   | True    |
| 25   | 10   | True    | False   | False   | True    | True    | False   |

---

### **4. Logical Operators**
#### **Problem Statement:**
Write a program to demonstrate the use of logical operators (`and`, `or`, `not`) with two conditions.

#### **Inputs:**
```python
a = True
b = False
```

#### **Expected Output:**
```
a and b: False
a or b: True
not a: False
```

#### **Solution Code:**
```python
a = True
b = False

print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")
```

#### **Test Cases:**
| A       | B       | A AND B | A OR B | NOT A |
|---------|---------|---------|--------|-------|
| True    | False   | False   | True   | False |
| False   | True    | False   | True   | True  |
| True    | True    | True    | True   | False |

---

### **5. Combine All Operators**
#### **Problem Statement:**
Write a program that uses all operators to calculate and evaluate conditions on two numbers.

#### **Inputs:**
```python
num1 = 8
num2 = 4
```

#### **Expected Output:**
```
Arithmetic Operations:
Addition: 12
Subtraction: 4
Multiplication: 32
Division: 2.0

Assignment Operations:
Initial num1: 8
After adding 4: 12
After subtracting 4: 8

Comparison:
Is num1 > num2? True

Logical Operations:
Is num1 > 5 and num2 < 5? True
Is num1 < 5 or num2 > 5? False
```

#### **Solution Code:**
```python
# Arithmetic Operators
num1 = 8
num2 = 4
print("Arithmetic Operations:")
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")

# Assignment Operators
print("\nAssignment Operations:")
num1 += 4
print(f"After adding 4: {num1}")
num1 -= 4
print(f"After subtracting 4: {num1}")

# Comparison Operators
print("\nComparison:")
print(f"Is num1 > num2? {num1 > num2}")

# Logical Operators
print("\nLogical Operations:")
print(f"Is num1 > 5 and num2 < 5? {num1 > 5 and num2 < 5}")
print(f"Is num1 < 5 or num2 > 5? {num1 < 5 or num2 > 5}")
```

#### **Test Cases:**
| Num1 | Num2 | Add | Sub | Mult | Div  | Assign (`+=4`) | Assign (`-=4`) | >    | AND          | OR          |
|------|------|-----|-----|------|------|----------------|----------------|------|--------------|-------------|
| 8    | 4    | 12  | 4   | 32   | 2.0  | 12             | 8              | True | True (8 > 5) | False       |
| 10   | 2    | 12  | 8   | 20   | 5.0  | 14             | 10             | True | True (10 > 5)| False       |

---

These problems demonstrate each operator's functionality, combining conceptual clarity with practical usage. Let me know if you'd like to explore advanced operator problems! 😊


ADVANCE

Here are **advanced-level problems** for Python **operators**:

---

### **1. Arithmetic and Logical Combination**
#### **Problem Statement:**
Write a program that checks if the sum of two numbers is even and greater than a third number. If true, multiply the result by 10; otherwise, divide it by 2.

#### **Inputs:**
```python
num1 = 8
num2 = 6
num3 = 12
```

#### **Expected Output:**
```
Sum of 8 and 6: 14
Sum is even and greater than 12: True
Result after multiplication: 140
```

#### **Solution Code:**
```python
num1 = 8
num2 = 6
num3 = 12

sum_result = num1 + num2
print(f"Sum of {num1} and {num2}: {sum_result}")

condition = sum_result % 2 == 0 and sum_result > num3
print(f"Sum is even and greater than {num3}: {condition}")

if condition:
    result = sum_result * 10
else:
    result = sum_result / 2

print(f"Final result: {result}")
```

#### **Test Cases:**
| Num1 | Num2 | Num3 | Condition (Even & > Num3) | Final Result |
|------|------|------|--------------------------|--------------|
| 8    | 6    | 12   | True                     | 140          |
| 5    | 4    | 10   | False                    | 4.5          |

---

### **2. Comparison of Numbers Using Logical Operators**
#### **Problem Statement:**
Write a program to check if all numbers in a list are greater than a threshold and at least one number is even.

#### **Inputs:**
```python
numbers = [15, 22, 31, 18]
threshold = 10
```

#### **Expected Output:**
```
All numbers > 10: True
At least one number is even: True
```

#### **Solution Code:**
```python
numbers = [15, 22, 31, 18]
threshold = 10

all_above_threshold = all(num > threshold for num in numbers)
at_least_one_even = any(num % 2 == 0 for num in numbers)

print(f"All numbers > {threshold}: {all_above_threshold}")
print(f"At least one number is even: {at_least_one_even}")
```

#### **Test Cases:**
| Numbers         | Threshold | All > Threshold | At Least One Even |
|------------------|-----------|-----------------|-------------------|
| [15, 22, 31, 18] | 10        | True            | True              |
| [5, 11, 9]       | 10        | False           | False             |

---

### **3. Reverse Engineer a Target Number**
#### **Problem Statement:**
Using arithmetic and assignment operators, find two numbers from a list that, when added and multiplied, equal a target number. Return the pair of numbers or state that no such pair exists.

#### **Inputs:**
```python
numbers = [1, 3, 5, 7, 9]
target = 24
```

#### **Expected Output:**
```
Found numbers: 3 and 7
```

#### **Solution Code:**
```python
numbers = [1, 3, 5, 7, 9]
target = 24

found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] * 2 == target:
            print(f"Found numbers: {numbers[i]} and {numbers[j]}")
            found = True
            break
    if found:
        break

if not found:
    print("No such pair found.")
```

#### **Test Cases:**
| Numbers          | Target | Found Numbers |
|-------------------|--------|---------------|
| [1, 3, 5, 7, 9]   | 24     | 3 and 7       |
| [2, 4, 6, 8]      | 20     | None          |

---

### **4. Nested Logical Conditions**
#### **Problem Statement:**
Write a program to determine if a number is positive, a multiple of 5, and greater than 50.

#### **Inputs:**
```python
num = 75
```

#### **Expected Output:**
```
Number is positive, a multiple of 5, and greater than 50: True
```

#### **Solution Code:**
```python
num = 75

condition = num > 0 and num % 5 == 0 and num > 50
print(f"Number is positive, a multiple of 5, and greater than 50: {condition}")
```

#### **Test Cases:**
| Number | Is Positive | Multiple of 5 | Greater than 50 | Final Condition |
|--------|-------------|---------------|-----------------|-----------------|
| 75     | True        | True          | True            | True            |
| 45     | True        | True          | False           | False           |

---

### **5. Expression Evaluation with Logical Operators**
#### **Problem Statement:**
Evaluate a complex boolean expression combining arithmetic, comparison, and logical operators.

#### **Inputs:**
```python
a = 10
b = 20
c = 30
```

#### **Expected Output:**
```
Expression: (a + b > c) and (b < c) or (a % 2 == 0)
Result: True
```

#### **Solution Code:**
```python
a = 10
b = 20
c = 30

result = (a + b > c) and (b < c) or (a % 2 == 0)
print(f"Expression: (a + b > c) and (b < c) or (a % 2 == 0)")
print(f"Result: {result}")
```

#### **Test Cases:**
| A   | B   | C   | Result |
|-----|-----|-----|--------|
| 10  | 20  | 30  | True   |
| 15  | 25  | 50  | False  |

---

### **6. Logical Operation on Strings**
#### **Problem Statement:**
Check if a string starts with a vowel and ends with a consonant using logical operators.

#### **Inputs:**
```python
text = "Apple"
```

#### **Expected Output:**
```
Starts with a vowel: True
Ends with a consonant: False
```

#### **Solution Code:**
```python
text = "Apple"

vowels = "AEIOUaeiou"
starts_with_vowel = text[0] in vowels
ends_with_consonant = text[-1].lower() not in vowels and text[-1].isalpha()

print(f"Starts with a vowel: {starts_with_vowel}")
print(f"Ends with a consonant: {ends_with_consonant}")
```

#### **Test Cases:**
| Text   | Starts with Vowel | Ends with Consonant |
|--------|--------------------|---------------------|
| Apple  | True               | False              |
| Orange | True               | True               |

---

### **7. Arithmetic and Logical Challenge**
#### **Problem Statement:**
Calculate the product of all even numbers in a list greater than a given threshold using arithmetic and logical operators.

#### **Inputs:**
```python
numbers = [2, 4, 6, 8, 10]
threshold = 5
```

#### **Expected Output:**
```
Product of even numbers > 5: 48
```

#### **Solution Code:**
```python
numbers = [2, 4, 6, 8, 10]
threshold = 5

product = 1
for num in numbers:
    if num % 2 == 0 and num > threshold:
        product *= num

print(f"Product of even numbers > {threshold}: {product}")
```

#### **Test Cases:**
| Numbers          | Threshold | Result |
|-------------------|-----------|--------|
| [2, 4, 6, 8, 10] | 5         | 48     |
| [12, 14, 16]     | 10        | 2688   |

---

These problems integrate Python's operators into real-world scenarios, encouraging deep understanding and creative problem-solving. Let me know if you’d like additional variations or assistance! 😊