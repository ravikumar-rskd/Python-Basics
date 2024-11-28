# Dictionaries

# Creating a Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing Dictionary Values
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["age"])  # Output: 25

#  Adding Key-Value Pairs to a Dictionary
person = {"name": "Alice", "age": 25}
person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Dictionary Method - get()
person = {"name": "Alice", "age": 25}
print(person.get("name"))  # Output: Alice

# Dictionary Method - keys()
person = {"name": "Alice", "age": 25}
print(person.keys())  # Output: dict_keys(['name', 'age'])

#  Dictionary Method - values()
person = {"name": "Alice", "age": 25}
print(person.values())  # Output: dict_values(['Alice', 25])
