# Sets

#  Creating a Set
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)  # Output: {'apple', 'banana', 'cherry'}

# Adding to a Set
fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}

#  Set Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}

#  Set Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.intersection(set2)
print(result)  # Output: {3}

#  Set Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2)
print(result)  # Output: {1, 2}
