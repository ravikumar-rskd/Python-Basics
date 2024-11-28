# Typecasting in Python

# String to Integer
str_number = "123"
int_number = int(str_number)  # Converts string to integer
print("String to Integer:")
print("Original:", str_number, "| Type:", type(str_number))
print("Converted:", int_number, "| Type:", type(int_number))

# String to Float
str_float = "45.67"
float_number = float(str_float)  # Converts string to float
print("\nString to Float:")
print("Original:", str_float, "| Type:", type(str_float))
print("Converted:", float_number, "| Type:", type(float_number))

# Integer to String
num = 456
str_num = str(num)  # Converts integer to string
print("\nInteger to String:")
print("Original:", num, "| Type:", type(num))
print("Converted:", str_num, "| Type:", type(str_num))

# Float to Integer
flt = 98.76
int_flt = int(flt)  # Converts float to integer (truncates decimal part)
print("\nFloat to Integer:")
print("Original:", flt, "| Type:", type(flt))
print("Converted:", int_flt, "| Type:", type(int_flt))

# Integer to Float
int_num = 42
float_num = float(int_num)  # Converts integer to float
print("\nInteger to Float:")
print("Original:", int_num, "| Type:", type(int_num))
print("Converted:", float_num, "| Type:", type(float_num))

# Boolean to String
bool_value = True
str_bool = str(bool_value)  # Converts boolean to string
print("\nBoolean to String:")
print("Original:", bool_value, "| Type:", type(bool_value))
print("Converted:", str_bool, "| Type:", type(str_bool))

# String to Boolean
str_bool_value = "True"
bool_from_str = bool(str_bool_value)  # Converts string to boolean (non-empty strings are True)
print("\nString to Boolean:")
print("Original:", str_bool_value, "| Type:", type(str_bool_value))
print("Converted:", bool_from_str, "| Type:", type(bool_from_str))
