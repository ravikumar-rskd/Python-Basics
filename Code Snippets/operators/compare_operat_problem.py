# Problem Statement: 
# Write a program to compare two integers using comparison operators (==, !=, <, >, <=, >=).
# Input:
# Two integers (a, b).
# Output:
# The results of comparison operators on the two integers.
# Example Input:
# 5 3
# Example Output:
# a == b -> False
# a != b -> True
# a < b -> False
# a > b -> True
# a <= b -> False
# a >= b -> True

a, b = map(int, input().split())

# Using comparison operators
print(f"a == b -> {a == b}")
print(f"a != b -> {a != b}")
print(f"a < b -> {a < b}")
print(f"a > b -> {a > b}")
print(f"a <= b -> {a <= b}")
print(f"a >= b -> {a >= b}")
