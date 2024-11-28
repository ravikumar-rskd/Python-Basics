# Using *args
def print_elements(*args):
    for element in ____:
        print(element)

print_elements(1, 2, 3, 4)  # Should print: 1 2 3 4

# Using **kwargs
def print_data(**kwargs):
    for key, value in kwargs.____():
        print(f"{key}: {value}")

print_data(name="David", age=28)  # Should print:
# name: David
# age: 28

# Using *args and **kwargs Together
def show_details(*args, **kwargs):
    for arg in args:
        print(f"Argument: {arg}")
    for key, value in kwargs.____():
        print(f"{key}: {value}")

show_details("Alice", "Bob", city="New York", age=35)
# Should print:
# Argument: Alice
# Argument: Bob
# city: New York
# age: 35
