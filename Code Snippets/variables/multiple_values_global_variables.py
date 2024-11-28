
# Assigning Multiple Values to Variables
a, b, c = 5, "Hello", 3.14  # Assign multiple values at once
print("Values assigned:")
print("a =", a)
print("b =", b)
print("c =", c)

# Assign the same value to multiple variables
x = y = z = 10
print("\nSame value assigned:")
print("x =", x)
print("y =", y)
print("z =", z)

# Output Variables using the print() Function
name = "Alice"
age = 25
print("\nUsing print() to output variables:")
print("Name:", name)
print("Age:", age)

# Concatenating text and variables in print()
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

# Global Variables
# A variable declared outside any function is global and can be accessed inside functions.

global_var = "awesome"

def myfunc():
  global_var = "fantastic"
  print("Python is " + global_var)

myfunc()

print("Python is " + global_var)

##If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global xy
  xy = "fantastic"

myfunc()

print("Python is " + xy)

##To change the value of a global variable inside a function, refer to the variable by using the global keyword:

glob_x = "awesome"

def myfunc():
  global glob_x
  glob_x = "fantastic"

myfunc()

print("Python is " + glob_x)
