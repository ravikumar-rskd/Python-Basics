# Dictionaries

# 22. Creating a Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 23. Accessing Dictionary Values
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["age"])  # Output: 25

# 24. Adding Key-Value Pairs to a Dictionary
person = {"name": "Alice", "age": 25}
person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 25. Dictionary Method - get()
person = {"name": "Alice", "age": 25}
print(person.get("name"))  # Output: Alice

# 26. Dictionary Method - keys()
person = {"name": "Alice", "age": 25}
print(person.keys())  # Output: dict_keys(['name', 'age'])

# 27. Dictionary Method - values()
person = {"name": "Alice", "age": 25}
print(person.values())  # Output: dict_values(['Alice', 25])
