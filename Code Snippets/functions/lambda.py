# Basic Lambda Function
#Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

#Lambda functions can take any number of arguments:
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8


# Lambda Function with Conditional Expression
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(4))  # Output: Even
print(check_even(5))  # Output: Odd
