# Problem Statement:
# Write a program that assigns multiple values to multiple variables. Use tuple unpacking 
# to assign the values to the variables. Then, print the values of the variables.
# Input:
# Three integers (a, b, c).
# Output:
# The values of the variables after assigning multiple values.
# Example Input:
# 1 2 3
# Example Output:
# a: 1
# b: 2
# c: 3

a, b, c = map(int, input().split())

# Assigning multiple values to variables
x, y, z = a, b, c

# Printing the values of the variables
print(f"a: {x}")
print(f"b: {y}")
print(f"c: {z}")
