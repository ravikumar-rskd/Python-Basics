"""
Problem Statement: 
Write a program to demonstrate the use of assignment operators (=, +=, -=, *=, /=).
Input:
Two integers (a, b).
Output:
The results of using assignment operators on the variables.
Example Input:
5 3
Example Output:
a = 5
a += b -> 8
a -= b -> 5
a *= b -> 15
a /= b -> 5.0


"""
a, b = map(int, input().split())

# Using assignment operators
a = 5
print(f"a = {a}")
a += b
print(f"a += b -> {a}")
a -= b
print(f"a -= b -> {a}")
a *= b
print(f"a *= b -> {a}")
a /= b
print(f"a /= b -> {a}")
