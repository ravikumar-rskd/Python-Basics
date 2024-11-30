## **2. Tuples**
### **Problem 1: Tuple Traversal**
#### **Problem Statement:**
Write a program to access the second element of a tuple.

#### **Inputs:**
```python
data = (5, 10, 15, 20)
```

#### **Expected Output:**
```
Second element: 10
```

#### **Solution Code:**
```python
data = (5, 10, 15, 20)
second_element = data[1]
print(f"Second element: {second_element}")
```

#### **Test Cases:**
| Tuple               | Expected Output |
|---------------------|-----------------|
| (5, 10, 15, 20)     | 10              |
| ('a', 'b', 'c')     | b               |
| (1, 2, 3, 4, 5)     | 2               |

---

### **Problem 2: Concatenating Tuples**
#### **Problem Statement:**
Write a program that concatenates two tuples and prints the resulting tuple.

#### **Inputs:**
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
```

#### **Expected Output:**
```
Concatenated Tuple: (1, 2, 3, 4, 5, 6)
```

#### **Solution Code:**
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
print(f"Concatenated Tuple: {concatenated}")
```

#### **Test Cases:**
| Tuple1      | Tuple2      | Expected Output   |
|-------------|-------------|-------------------|
| (1, 2, 3)   | (4, 5, 6)   | (1, 2, 3, 4, 5, 6)|
| ('a', 'b')  | ('c', 'd')  | ('a', 'b', 'c', 'd')|
| (10, 20)    | (30, 40)    | (10, 20, 30, 40)   |

---

### **Problem 3: Tuple Unpacking**
#### **Problem Statement:**
Write a program to unpack a tuple into separate variables.

#### **Inputs:**
```python
person = ("John", 25, "Engineer")
```

#### **Expected Output:**
```
Name: John
Age: 25
Profession: Engineer
```

#### **Solution Code:**
```python
person = ("John", 25, "Engineer")
name, age, profession = person

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
```

#### **Test Cases:**
| Tuple                  | Expected Output            |
|------------------------|----------------------------|
| ("John", 25, "Engineer")| Name: John, Age: 25, Profession: Engineer |
| ("Alice", 30, "Doctor")| Name: Alice, Age: 30, Profession: Doctor |
| ("Bob", 40, "Teacher") | Name: Bob, Age: 40, Profession: Teacher |

---