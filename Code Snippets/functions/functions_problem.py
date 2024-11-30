"""
Problem Statement: 
Write a function that takes two numbers as input and returns their sum.
Input:
Two integers (a, b).
Output:
The sum of a and b.
Example Input:
3 5
Example Output:
8

"""

def add_numbers(a, b):
    return a + b

a, b = map(int, input().split())
print(add_numbers(a, b))
