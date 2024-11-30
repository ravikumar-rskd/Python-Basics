## **3. Sets**
### **Problem 1: Set Operations**
#### **Problem Statement:**
Write a program to perform union, intersection, and difference between two sets.

#### **Inputs:**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
```

#### **Expected Output:**
```
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}
```

#### **Solution Code:**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2

print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")
```

#### **Test Cases:**
| Set1         | Set2         | Union           | Intersection    | Difference       |
|--------------|--------------|-----------------|-----------------|------------------|
| {1, 2, 3, 4} | {3, 4, 5, 6} | {1, 2, 3, 4, 5, 6} | {3, 4}         | {1, 2}           |
| {10, 20}     | {20, 30}     | {10, 20, 30}    | {20}            | {10}             |

---

### **Problem 2: Adding and Removing Elements from Set**
#### **Problem Statement:**
Write a program to add an element to a set and remove an element from the set.

#### **Inputs:**
```python
fruits = {"apple", "banana", "cherry"}
add_fruit = "orange"
remove_fruit = "banana"
```

#### **Expected Output:**
```
Updated Set: {'apple', 'banana', 'cherry', 'orange'}
After Removal: {'apple', 'cherry', 'orange'}
```

#### **Solution Code:**
```python
fruits = {"apple", "banana", "cherry"}
add_fruit = "orange"
remove_fruit = "banana"

fruits.add(add_fruit)
print(f"Updated Set: {fruits}")

fruits.remove(remove_fruit)
print(f"After Removal: {fruits}")
```

#### **Test Cases:**
| Set                   | Add Element | Remove Element | Updated Set      | After Removal    |


|-----------------------|-------------|----------------|------------------|------------------|
| {"apple", "banana"}    | "orange"    | "banana"       | {"apple", "banana", "orange"} | {"apple", "orange"} |

---

### **Problem 3: Set Length**
#### **Problem Statement:**
Write a program to count the number of elements in a set.

#### **Inputs:**
```python
colors = {"red", "green", "blue", "yellow"}
```

#### **Expected Output:**
```
Number of elements: 4
```

#### **Solution Code:**
```python
colors = {"red", "green", "blue", "yellow"}
print(f"Number of elements: {len(colors)}")
```

#### **Test Cases:**
| Set                 | Expected Output |
|---------------------|-----------------|
| {"red", "green"}     | 2               |
| {"apple", "banana", "cherry"} | 3       |

---