Here are beginner-level **Python string concept problems** including **multi-line strings, slicing, modifying strings, concatenation, and format strings**. Each problem includes a **problem statement, inputs, expected outputs, solution code, and test cases**.

---

### **1. Multi-Line String**
#### **Problem Statement:**
Write a program to define and print a multi-line string.

#### **Inputs:**
```python
text = """Python is fun!
You can learn it easily.
It is versatile."""
```

#### **Expected Output:**
```
Python is fun!
You can learn it easily.
It is versatile.
```

#### **Solution Code:**
```python
text = """Python is fun!
You can learn it easily.
It is versatile."""
print(text)
```

#### **Test Cases:**
| Input String                          | Expected Output                       |
|---------------------------------------|---------------------------------------|
| `"""Line 1\nLine 2"""`                | Line 1<br>Line 2                      |
| `"""Hello\nWorld\n!"""`               | Hello<br>World<br>!                   |

---

### **2. String Slicing**
#### **Problem Statement:**
Write a program to extract a substring from a given string using slicing.

#### **Inputs:**
```python
text = "Learning Python"
start = 0
end = 8
```

#### **Expected Output:**
```
Learning
```

#### **Solution Code:**
```python
text = "Learning Python"
start = 0
end = 8
substring = text[start:end]
print(substring)
```

#### **Test Cases:**
| Input String      | Start | End  | Expected Output |
|--------------------|-------|------|-----------------|
| "Learning Python"  | 0     | 8    | Learning        |
| "Python Rocks"     | 7     | 12   | Rocks           |

---

### **3. Modify String**
#### **Problem Statement:**
Write a program to perform the following operations on a string:
1. Convert the string to uppercase.
2. Convert the string to lowercase.
3. Replace a word in the string.

#### **Inputs:**
```python
text = "Python is fun!"
to_replace = "fun"
replacement = "amazing"
```

#### **Expected Output:**
```
Uppercase: PYTHON IS FUN!
Lowercase: python is fun!
Modified String: Python is amazing!
```

#### **Solution Code:**
```python
text = "Python is fun!"
to_replace = "fun"
replacement = "amazing"

print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Modified String: {text.replace(to_replace, replacement)}")
```

#### **Test Cases:**
| Input String       | To Replace | Replacement | Expected Output                |
|--------------------|------------|-------------|--------------------------------|
| "Hello World!"     | "World"    | "Python"    | "Hello Python!"               |
| "Coding is cool!"  | "cool"     | "awesome"   | "Coding is awesome!"          |

---

### **4. String Concatenation**
#### **Problem Statement:**
Write a program to concatenate two strings.

#### **Inputs:**
```python
str1 = "Python"
str2 = "Programming"
```

#### **Expected Output:**
```
Concatenated String: PythonProgramming
```

#### **Solution Code:**
```python
str1 = "Python"
str2 = "Programming"
result = str1 + str2
print(f"Concatenated String: {result}")
```

#### **Test Cases:**
| String 1         | String 2         | Expected Output       |
|-------------------|------------------|-----------------------|
| "Hello"          | "World"          | "HelloWorld"          |
| "Data"           | "Science"        | "DataScience"         |

---

### **5. Format Strings**
#### **Problem Statement:**
Write a program to format a string using the `format()` method. Display a person's name, age, and profession.

#### **Inputs:**
```python
name = "Alice"
age = 30
profession = "Engineer"
```

#### **Expected Output:**
```
Name: Alice, Age: 30, Profession: Engineer
```

#### **Solution Code:**
```python
name = "Alice"
age = 30
profession = "Engineer"

formatted_string = "Name: {}, Age: {}, Profession: {}".format(name, age, profession)
print(formatted_string)
```

#### **Test Cases:**
| Name   | Age | Profession  | Expected Output                        |
|--------|-----|-------------|----------------------------------------|
| Alice  | 30  | Engineer    | "Name: Alice, Age: 30, Profession: Engineer" |
| Bob    | 25  | Developer   | "Name: Bob, Age: 25, Profession: Developer"  |

---

### **6. Reverse a String**
#### **Problem Statement:**
Write a program to reverse a given string.

#### **Inputs:**
```python
text = "Python"
```

#### **Expected Output:**
```
Reversed String: nohtyP
```

#### **Solution Code:**
```python
text = "Python"
reversed_text = text[::-1]
print(f"Reversed String: {reversed_text}")
```

#### **Test Cases:**
| Input String    | Expected Output |
|------------------|-----------------|
| "Python"        | "nohtyP"        |
| "Hello"         | "olleH"         |

---

### **7. Check for Substring**
#### **Problem Statement:**
Write a program to check whether a given substring exists in a string.

#### **Inputs:**
```python
text = "Learning Python is fun!"
substring = "Python"
```

#### **Expected Output:**
```
Substring found: True
```

#### **Solution Code:**
```python
text = "Learning Python is fun!"
substring = "Python"
found = substring in text
print(f"Substring found: {found}")
```

#### **Test Cases:**
| String                      | Substring | Expected Output |
|------------------------------|-----------|-----------------|
| "Learning Python is fun!"    | "Python"  | True            |
| "I love programming"         | "Java"    | False           |

---

### **8. Count the Occurrences of a Character**
#### **Problem Statement:**
Write a program to count the occurrences of a specific character in a string.

#### **Inputs:**
```python
text = "banana"
character = "a"
```

#### **Expected Output:**
```
Occurrences of 'a': 3
```

#### **Solution Code:**
```python
text = "banana"
character = "a"
count = text.count(character)
print(f"Occurrences of '{character}': {count}")
```

#### **Test Cases:**
| Input String | Character | Expected Count |
|--------------|-----------|----------------|
| "banana"     | "a"       | 3              |
| "apple"      | "p"       | 2              |

---

These problems cover multi-line strings, slicing, modifying strings, concatenation, formatting, and more. Let me know if you’d like additional advanced problems for strings! 😊

Here are **advanced-level problems** for Python **string concepts**:

---

### **1. Extract and Count Words from a Multi-Line String**
#### **Problem Statement:**
Write a program to extract all unique words from a multi-line string and count their occurrences.

#### **Inputs:**
```python
text = """Python is versatile.
Python is easy to learn.
Python is fun."""
```

#### **Expected Output:**
```
{'Python': 3, 'is': 3, 'versatile.': 1, 'easy': 1, 'to': 1, 'learn.': 1, 'fun.': 1}
```

#### **Solution Code:**
```python
from collections import Counter

text = """Python is versatile.
Python is easy to learn.
Python is fun."""

# Split text into words
words = text.split()
word_count = Counter(words)
print(dict(word_count))
```

#### **Test Cases:**
| Input Text                                | Expected Output                                  |
|-------------------------------------------|-------------------------------------------------|
| "Hello world! Hello Python."              | {'Hello': 2, 'world!': 1, 'Python.': 1}         |
| "Data science is fun. Data is powerful."  | {'Data': 2, 'science': 1, 'is': 2, 'fun.': 1, 'powerful.': 1} |

---

### **2. String Slicing with Steps**
#### **Problem Statement:**
Write a program to extract every third character from a given string.

#### **Inputs:**
```python
text = "abcdefghijklmn"
```

#### **Expected Output:**
```
adgjm
```

#### **Solution Code:**
```python
text = "abcdefghijklmn"
result = text[::3]
print(result)
```

#### **Test Cases:**
| Input String        | Expected Output |
|----------------------|-----------------|
| "abcdefghijklmn"     | "adgjm"         |
| "PythonProgramming"  | "Phgai"         |

---

### **3. Check if Two Strings are Anagrams**
#### **Problem Statement:**
Write a program to check if two given strings are anagrams of each other.

#### **Inputs:**
```python
str1 = "listen"
str2 = "silent"
```

#### **Expected Output:**
```
True
```

#### **Solution Code:**
```python
str1 = "listen"
str2 = "silent"

# Check if sorted characters of both strings are equal
is_anagram = sorted(str1) == sorted(str2)
print(is_anagram)
```

#### **Test Cases:**
| String 1    | String 2    | Expected Output |
|-------------|-------------|-----------------|
| "listen"    | "silent"    | True            |
| "hello"     | "world"     | False           |

---

### **4. Format String with Dictionary**
#### **Problem Statement:**
Write a program to format a string using a dictionary of values.

#### **Inputs:**
```python
template = "My name is {name} and I am a {profession}."
data = {"name": "Alice", "profession": "developer"}
```

#### **Expected Output:**
```
My name is Alice and I am a developer.
```

#### **Solution Code:**
```python
template = "My name is {name} and I am a {profession}."
data = {"name": "Alice", "profession": "developer"}

formatted_string = template.format(**data)
print(formatted_string)
```

#### **Test Cases:**
| Template                           | Data                                  | Expected Output                          |
|------------------------------------|---------------------------------------|------------------------------------------|
| "Hello {name}!"                    | {"name": "Bob"}                       | "Hello Bob!"                             |
| "Age: {age}, Profession: {job}"    | {"age": 30, "job": "engineer"}        | "Age: 30, Profession: engineer"          |

---

### **5. Palindrome Check**
#### **Problem Statement:**
Write a program to check if a string is a palindrome (ignoring case and non-alphanumeric characters).

#### **Inputs:**
```python
text = "A man, a plan, a canal, Panama"
```

#### **Expected Output:**
```
True
```

#### **Solution Code:**
```python
import re

text = "A man, a plan, a canal, Panama"
cleaned_text = re.sub(r'[^A-Za-z0-9]', '', text).lower()
is_palindrome = cleaned_text == cleaned_text[::-1]
print(is_palindrome)
```

#### **Test Cases:**
| Input String                         | Expected Output |
|--------------------------------------|-----------------|
| "A man, a plan, a canal, Panama"     | True            |
| "Hello World"                        | False           |

---

### **6. Extract Numbers from a String**
#### **Problem Statement:**
Write a program to extract all numbers from a string and return them as a list.

#### **Inputs:**
```python
text = "My phone number is 123-456-7890 and my zip is 98765."
```

#### **Expected Output:**
```
[123, 456, 7890, 98765]
```

#### **Solution Code:**
```python
import re

text = "My phone number is 123-456-7890 and my zip is 98765."
numbers = list(map(int, re.findall(r'\d+', text)))
print(numbers)
```

#### **Test Cases:**
| Input String                                      | Expected Output      |
|--------------------------------------------------|----------------------|
| "Order 123 has been shipped on 04/10/2024."      | [123, 4, 10, 2024]   |
| "No numbers here!"                               | []                   |

---

### **7. Create an Acronym**
#### **Problem Statement:**
Write a program to generate an acronym from a given phrase. The acronym should consist of the first letter of each word in uppercase.

#### **Inputs:**
```python
phrase = "As soon as possible"
```

#### **Expected Output:**
```
ASAP
```

#### **Solution Code:**
```python
phrase = "As soon as possible"
acronym = "".join(word[0].upper() for word in phrase.split())
print(acronym)
```

#### **Test Cases:**
| Phrase                      | Expected Output |
|-----------------------------|-----------------|
| "As soon as possible"       | ASAP            |
| "National Aeronautics Space Administration" | NASA |

---

### **8. Remove Duplicates from a String**
#### **Problem Statement:**
Write a program to remove duplicate characters from a string while maintaining the order.

#### **Inputs:**
```python
text = "programming"
```

#### **Expected Output:**
```
progamin
```

#### **Solution Code:**
```python
text = "programming"
unique_chars = "".join(dict.fromkeys(text))
print(unique_chars)
```

#### **Test Cases:**
| Input String   | Expected Output |
|-----------------|-----------------|
| "programming"   | "progamin"      |
| "aabbccddeeff"  | "abcdef"        |

---
