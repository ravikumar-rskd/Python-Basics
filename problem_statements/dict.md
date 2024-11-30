
## **4. Dictionaries**
### **Problem 1: Accessing and Modifying Dictionary Values**
#### **Problem Statement:**
Write a program to access and modify a value in a dictionary.

#### **Inputs:**
```python
person = {"name": "Alice", "age": 25}
```

#### **Expected Output:**
```
Name: Alice
Updated Age: 26
```

#### **Solution Code:**
```python
person = {"name": "Alice", "age": 25}

print(f"Name: {person['name']}")
person['age'] = 26
print(f"Updated Age: {person['age']}")
```

#### **Test Cases:**
| Dictionary             | Expected Output        |
|------------------------|------------------------|
| {"name": "Alice", "age": 25} | Name: Alice, Updated Age: 26 |
| {"name": "Bob", "age": 30}   | Name: Bob, Updated Age: 31 |

---

### **Problem 2: Iterating Over a Dictionary**
#### **Problem Statement:**
Write a program to iterate over a dictionary and print each key-value pair.

#### **Inputs:**
```python
student = {"name": "John", "grade": "A", "age": 21}
```

#### **Expected Output:**
```
name: John
grade: A
age: 21
```

#### **Solution Code:**
```python
student = {"name": "John", "grade": "A", "age": 21}

for key, value in student.items():
    print(f"{key}: {value}")
```

#### **Test Cases:**
| Dictionary              | Expected Output             |
|-------------------------|-----------------------------|
| {"name": "John", "age": 21} | name: John, age: 21      |
| {"city": "New York", "population": 8000000} | city: New York, population: 8000000 |

---

### **Problem 3: Checking if Key Exists**
#### **Problem Statement:**
Write a program to check if a given key exists in a dictionary.

#### **Inputs:**
```python
person = {"name": "Alice", "age": 25}
key_to_check = "age"
```

#### **Expected Output:**
```
Key exists: True
```

#### **Solution Code:**
```python
person = {"name": "Alice", "age": 25}
key_to_check = "age"

if key_to_check in person:
    print(f"Key exists: True")
else:
    print(f"Key exists: False")
```

#### **Test Cases:**
| Dictionary                | Key to Check | Expected Output |
|---------------------------|--------------|-----------------|
| {"name": "Alice", "age": 25} | "age"        | Key exists: True |
| {"name": "John", "city": "NY"} | "address"    | Key exists: False |

---
