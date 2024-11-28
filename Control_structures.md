Here are **20 basic Python codes** to help understand "Control Structures," including conditional statements and loops. I'll also include **fill-in-the-blank exercises** for each concept.

---

### **Conditional Statements**

**1. If Statement**
```python
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5
```

**2. If-Else Statement**
```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")  # Output: x is less than or equal to 5
```

**3. If-Elif-Else Statement**
```python
x = 8
if x > 10:
    print("x is greater than 10")
elif x == 8:
    print("x is equal to 8")  # Output: x is equal to 8
else:
    print("x is less than 8")
```

---

### **Loops**

**4. For Loop - Iterate over a range**
```python
for i in range(5):
    print(i)  # Output: 0 1 2 3 4
```

**5. For Loop - Iterate over a list**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry
```

**6. While Loop**
```python
x = 0
while x < 5:
    print(x)  # Output: 0 1 2 3 4
    x += 1
```

**7. For Loop with break**
```python
for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0 1 2 3 4
```

**8. For Loop with continue**
```python
for i in range(6):
    if i == 3:
        continue
    print(i)  # Output: 0 1 2 4 5
```

**9. While Loop with break**
```python
x = 0
while x < 10:
    if x == 7:
        break
    print(x)  # Output: 0 1 2 3 4 5 6
    x += 1
```

**10. While Loop with continue**
```python
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)  # Output: 1 2 4 5
```

**11. Nested Loops**
```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")  # Output: i=0, j=0; i=0, j=1; i=1, j=0; i=1, j=1; i=2, j=0; i=2, j=1
```

**12. For Loop with else**
```python
for i in range(3):
    print(i)
else:
    print("Loop finished!")  # Output: 0 1 2 Loop finished!
```

---

### **Fill in the blanks for practice**

---

### **Conditional Statements**

**1. If Statement**
```python
x = 12
if x ____ 10:
    print("x is greater than 10")  # Should print: x is greater than 10
```

**2. If-Else Statement**
```python
x = 7
if x ____ 10:
    print("x is less than 10")
else:
    print("x is greater than or equal to 10")  # Should print: x is less than 10
```

**3. If-Elif-Else Statement**
```python
x = 4
if x ____ 5:
    print("x is greater than 5")
elif x ____ 4:
    print("x is equal to 4")  # Should print: x is equal to 4
else:
    print("x is less than 4")
```

---

### **Loops**

**4. For Loop**
```python
for i in ____:
    print(i)  # Should print: 0 1 2 3 4
```

**5. For Loop with a List**
```python
colors = ["red", "green", "blue"]
for color in ____:
    print(color)  # Should print: red, green, blue
```

**6. While Loop**
```python
x = 0
while x ____ 5:
    print(x)  # Should print: 0 1 2 3 4
    x += 1
```

**7. For Loop with break**
```python
for i in range(10):
    if i ____ 5:
        break
    print(i)  # Should print: 0 1 2 3 4
```

**8. For Loop with continue**
```python
for i in range(6):
    if i ____ 3:
        continue
    print(i)  # Should print: 0 1 2 4 5
```

**9. While Loop with break**
```python
x = 0
while x ____ 10:
    if x ____ 7:
        break
    print(x)  # Should print: 0 1 2 3 4 5 6
    x += 1
```

**10. While Loop with continue**
```python
x = 0
while x ____ 5:
    x += 1
    if x ____ 3:
        continue
    print(x)  # Should print: 1 2 4 5
```

**11. Nested Loops**
```python
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")  # Should print: i=0, j=0; i=0, j=1; i=0, j=2; i=1, j=0; i=1, j=1; i=1, j=2
```

**12. For Loop with else**
```python
for i in range(3):
    print(i)
else:
    print("Done!")  # Should print: 0 1 2 Done!
```

---

These exercises cover **conditional statements**, **loops**, and their control structures. They allow you to practice fundamental control flow concepts in Python. Let me know if you'd like solutions or further explanations!
