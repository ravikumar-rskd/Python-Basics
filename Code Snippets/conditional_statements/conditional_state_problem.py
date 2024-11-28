# Problem Statement: 
# Write a program that checks if a number is positive, negative, or zero.
# Input:
# An integer (n).
# Output:
# A message indicating whether the number is positive, negative, or zero.
# Example Input:
# -5
# Example Output:
# Negative number

n = int(input())

if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")
