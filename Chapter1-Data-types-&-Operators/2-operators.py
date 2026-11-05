# Operators are used to perform operations on variables and values.

a = 15
b = 4

# 1. Arithmetic Operators
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division (always returns a float in Python, output: 3.75)
print(a // b) # Floor Division (removes the decimal part, returns int, output: 3)
print(a % b)  # Modulo (returns the remainder, output: 3)
print(a ** b) # Exponentiation (a to the power of b)

# 2. Assignment Operators
c = 10
c += 5 # Same as c = c + 5 (outputs 15)
c -= 2 # Same as c = c - 2 (outputs 13)
# There is NO c++ or c-- in Python. You must use c += 1 or c -= 1

# 3. Comparison (Relational) Operators - always return True or False
print(a == b) # Equal to
print(a != b) # Not equal to
print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= 15) # Greater than or equal to

# 4. Logical Operators (used to combine conditional statements)
x = True
y = False

# 'and' returns True if both statements are true
print(a > 10 and b < 5) 

# 'or' returns True if one of the statements is true
print(a > 20 or b < 5) 

# 'not' reverses the result, returns False if the result is true
print(not(a > 10 and b < 5))