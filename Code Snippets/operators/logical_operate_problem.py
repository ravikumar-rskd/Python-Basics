"""
Problem Statement: 
Write a program to demonstrate the use of logical operators (and, or, not).
Input:
Two boolean values (x, y).
Output:
The results of logical operations on x and y.
Example Input:
True False
Example Output:
x and y -> False
x or y -> True
not x -> False

"""

x, y = map(lambda v: v == "True", input().split())

# Using logical operators
print(f"x and y -> {x and y}")
print(f"x or y -> {x or y}")
print(f"not x -> {not x}")
