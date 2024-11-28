# Problem Statement: 
# Write a program that demonstrates the use of basic arithmetic operators (+, -, *, /).
# Input:
# Two integers (a, b).
# Output:
# The result of a + b, a - b, a * b, and a / b.
# Example Input:
# 6 3
# Example Output:
# 9 3 18 2.0

a, b = map(int, input().split())
print(a + b, a - b, a * b, a / b)
