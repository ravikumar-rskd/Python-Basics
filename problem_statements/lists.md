Here are **beginner-level problems** for **lists, tuples, sets, and dictionaries** in Python. Each section contains **3 problems** with their **problem statements, inputs, expected outputs, solutions as code, and test cases**.

---

## **1. Lists**
### **Problem 1: List Traversal and Summing Elements**
#### **Problem Statement:**
Write a program to calculate the sum of all elements in a given list of integers.

#### **Inputs:**
```python
numbers = [1, 2, 3, 4, 5]
```

#### **Expected Output:**
```
Sum of all elements: 15
```

#### **Solution Code:**
```python
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
print(f"Sum of all elements: {total_sum}")
```

#### **Test Cases:**
| List               | Expected Output |
|--------------------|-----------------|
| [1, 2, 3, 4, 5]    | 15              |
| [10, 20, 30]       | 60              |
| [5, 5, 5, 5, 5]    | 25              |

---

### **Problem 2: Adding and Removing Elements from List**
#### **Problem Statement:**
Write a program to add an element to the end of a list and remove an element from the list.

#### **Inputs:**
```python
numbers = [10, 20, 30]
new_number = 40
remove_number = 20
```

#### **Expected Output:**
```
Updated List: [10, 20, 30, 40]
After removal: [10, 30, 40]
```

#### **Solution Code:**
```python
numbers = [10, 20, 30]
new_number = 40
remove_number = 20

numbers.append(new_number)
print(f"Updated List: {numbers}")

numbers.remove(remove_number)
print(f"After removal: {numbers}")
```

#### **Test Cases:**
| List               | New Element | Remove Element | Updated List | After Removal |
|--------------------|-------------|----------------|--------------|---------------|
| [10, 20, 30]       | 40          | 20             | [10, 20, 30, 40] | [10, 30, 40]  |
| [5, 10, 15]        | 20          | 10             | [5, 10, 15, 20]  | [5, 15, 20]   |

---

### **Problem 3: List Slicing**
#### **Problem Statement:**
Write a program that slices a list and returns the first three elements.

#### **Inputs:**
```python
numbers = [1, 2, 3, 4, 5]
```

#### **Expected Output:**
```
First three elements: [1, 2, 3]
```

#### **Solution Code:**
```python
numbers = [1, 2, 3, 4, 5]
first_three = numbers[:3]
print(f"First three elements: {first_three}")
```

#### **Test Cases:**
| List               | Expected Output |
|--------------------|-----------------|
| [1, 2, 3, 4, 5]    | [1, 2, 3]       |
| [10, 20, 30, 40]   | [10, 20, 30]     |
| [5, 10, 15, 20]    | [5, 10, 15]      |

---
These problems cover the basics and can help beginners practice.