# Using *args (Variable Number of Arguments)
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3)  # Output: 1 2 3
print_numbers(10, 20, 30, 40)  # Output: 10 20 30 40

# Using **kwargs (Keyword Arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)  
# Output:
# name: Alice
# age: 25

# Using *args and **kwargs Together
def greet_info(*args, **kwargs):
    for arg in args:
        print(f"Hello, {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet_info("Alice", "Bob", age=25, city="New York")  
# Output:
# Hello, Alice
# Hello, Bob
# age: 25
# city: New York
