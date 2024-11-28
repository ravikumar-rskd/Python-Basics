Here are **basic Python codes** to help understand the **Data Structures** topic, including strings, lists, tuples, sets, and dictionaries, along with **fill-in-the-blank exercises** for each concept.

---

### **Strings**

**1. String Concatenation**
```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World
```

**2. String Slicing**
```python
text = "Python"
print(text[0:3])  # Output: Pyt
print(text[3:])   # Output: hon
print(text[:4])   # Output: Pyth
```

**3. String Indexing**
```python
word = "Programming"
print(word[0])   # Output: P
print(word[-1])  # Output: g
```

**4. String Method - upper()**
```python
sentence = "hello python"
print(sentence.upper())  # Output: HELLO PYTHON
```

**5. String Method - lower()**
```python
sentence = "HELLO PYTHON"
print(sentence.lower())  # Output: hello python
```

**6. String Method - strip()**
```python
text = "   Python   "
print(text.strip())  # Output: Python
```

**7. String Method - split()**
```python
sentence = "apple,banana,grape"
fruits = sentence.split(",")
print(fruits)  # Output: ['apple', 'banana', 'grape']
```

---

### **Lists**

**8. Creating a List**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

**9. Appending to a List**
```python
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

**10. Removing from a List**
```python
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']
```

**11. Sorting a List**
```python
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]
```

**12. Accessing List Elements by Index**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana
```

---

### **Tuples**

**13. Creating a Tuple**
```python
fruit_tuple = ("apple", "banana", "cherry")
print(fruit_tuple)  # Output: ('apple', 'banana', 'cherry')
```

**14. Accessing Tuple Elements by Index**
```python
fruit_tuple = ("apple", "banana", "cherry")
print(fruit_tuple[1])  # Output: banana
```

**15. Tuple with Multiple Data Types**
```python
info = ("John", 25, "Engineer")
print(info)  # Output: ('John', 25, 'Engineer')
```

**16. Tuple Length**
```python
fruit_tuple = ("apple", "banana", "cherry")
print(len(fruit_tuple))  # Output: 3
```

---

### **Sets**

**17. Creating a Set**
```python
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)  # Output: {'apple', 'banana', 'cherry'}
```

**18. Adding to a Set**
```python
fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}
```

**19. Set Union**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}
```

**20. Set Intersection**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.intersection(set2)
print(result)  # Output: {3}
```

**21. Set Difference**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2)
print(result)  # Output: {1, 2}
```

---

### **Dictionaries**

**22. Creating a Dictionary**
```python
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

**23. Accessing Dictionary Values**
```python
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["age"])  # Output: 25
```

**24. Adding Key-Value Pairs to a Dictionary**
```python
person = {"name": "Alice", "age": 25}
person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

**25. Dictionary Method - get()**
```python
person = {"name": "Alice", "age": 25}
print(person.get("name"))  # Output: Alice
```

**26. Dictionary Method - keys()**
```python
person = {"name": "Alice", "age": 25}
print(person.keys())  # Output: dict_keys(['name', 'age'])
```

**27. Dictionary Method - values()**
```python
person = {"name": "Alice", "age": 25}
print(person.values())  # Output: dict_values(['Alice', 25])
```

---

### **Fill in the blanks to practice**

---

### **Strings**

**1. String Concatenation**
```python
str1 = "Good"
str2 = "Morning"
result = str1 ____ str2
print(result)  # Should print: Good Morning
```

**2. String Indexing**
```python
word = "Programming"
print(word[____])  # Should print: P
```

**3. String Method - lower()**
```python
sentence = "HELLO WORLD"
print(sentence.____())  # Should print: hello world
```

---

### **Lists**

**4. Adding to a List**
```python
fruits = ["apple", "banana"]
fruits.____("orange")
print(fruits)  # Should print: ['apple', 'banana', 'orange']
```

**5. Removing from a List**
```python
fruits = ["apple", "banana", "cherry"]
fruits.____("banana")
print(fruits)  # Should print: ['apple', 'cherry']
```

**6. Sorting a List**
```python
numbers = [9, 3, 5, 2]
numbers.____()
print(numbers)  # Should print: [2, 3, 5, 9]
```

---

### **Tuples**

**7. Tuple Access**
```python
fruit_tuple = ("apple", "banana", "cherry")
print(fruit_tuple[____])  # Should print: banana
```

**8. Length of a Tuple**
```python
fruit_tuple = ("apple", "banana", "cherry")
print(____(fruit_tuple))  # Should print: 3
```

---

### **Sets**

**9. Adding to a Set**
```python
fruits_set = {"apple", "banana"}
fruits_set.____("orange")
print(fruits_set)  # Should print: {'apple', 'banana', 'orange'}
```

**10. Set Difference**
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.____(set2)
print(result)  # Should print: {1}
```

---

### **Dictionaries**

**11. Accessing Dictionary Values**
```python
person = {"name": "Bob", "age": 30}
print(person["____"])  # Should print: Bob
```

**12. Adding to a Dictionary**
```python
person = {"name": "Alice"}
person["age"] = 25
print(person)  # Should print: {'name': 'Alice', 'age': 25}
```

**13. Dictionary Method - get()**
```python
person = {"name": "Alice", "age": 25}
print(person.____("age"))  # Should print: 25
```

---

These examples cover the key concepts of **strings**, **lists**, **tuples**, **sets**, and **dictionaries** in Python. The **fill-in-the-blank** exercises are designed to test your understanding of basic operations and methods. Let me know if you'd like solutions or further clarifications!
