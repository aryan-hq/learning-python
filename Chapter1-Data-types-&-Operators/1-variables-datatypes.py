# In Python, we don't need to declare the data type of a variable before assigning it (unlike C).
# Python is dynamically typed, meaning the type is determined at runtime.
# Variable names cannot start with a number and cannot contain spaces or special characters (except _).

# Primitive Data Types
age = 20                # Integer (int)
price = 99.99           # Floating point number (float)
is_enrolled = True      # Boolean (bool) - must start with capital T or F
name = "aryan"          # String (str) - can use single or double quotes
empty_value = None      # NoneType - used to define a null variable, similar to NULL in C

# type() function returns the data type of the variable
print(type(age))
print(type(price))
print(type(is_enrolled))
print(type(empty_value))

# Type Casting (Converting one data type to another)
a = "50"
b = 10
# print(a + b) # This will give an error because you can't add string and integer directly

a = int(a) # Explicitly type casting string to integer
print(a + b) # Now this works and outputs 60

float_val = float(b) # Converting int to float
print(float_val) # Outputs 10.0

# Input and Output (I/O)
# input() function always takes input as a string by default
user_age = input("Enter your age: ") 
user_age = int(user_age) # Must cast to int if we want to do math with it

# f-strings (Formatted string literals) - the most modern way to print variables inside strings
course = "BCA"
print(f"My name is {name}, I am {user_age} years old, and I study {course}.")