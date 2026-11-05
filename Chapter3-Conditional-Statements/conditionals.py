# Conditional statements decide the flow of execution based on True/False conditions.
# Python uses indentation (spaces) to define blocks of code, instead of curly braces {} like in C.

marks = 85

# if, elif, else statements
if marks >= 90:
    print("Grade: A")
elif marks >= 80: # elif is short for "else if"
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")
    print("Work harder!") # This is part of the else block because of indentation

# Nested if statements (if inside an if)
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Negative or Zero")

# Ternary Operator (Single line if-else)
# Syntax: [on_true] if [condition] else [on_false]
status = "Pass" if marks >= 40 else "Fail"
print(f"Result: {status}")