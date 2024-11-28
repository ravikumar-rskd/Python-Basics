# Problem Statement:
# Write a program that demonstrates the use of a global variable. The program should 
# have a global variable that is modified inside a function. The program should 
# print the value of the global variable before and after modification.
# Input:
# A single integer value to modify the global variable.
# Output:
# The value of the global variable before and after modification.
# Example Input:
# 10
# Example Output:
# Global variable before modification: 5
# Global variable after modification: 15

global_var = 5  # Global variable

def modify_global_variable(value):
    global global_var  # Declare the variable as global
    print(f"Global variable before modification: {global_var}")
    global_var += value
    print(f"Global variable after modification: {global_var}")

# Input and function call
value = int(input())
modify_global_variable(value)
