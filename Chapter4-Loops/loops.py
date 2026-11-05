# Loops are used to iterate over a sequence or execute a block of code multiple times.

# 1. While Loop
# Executes a set of statements as long as a condition is true.
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1 # Important: loop control variable must be updated to avoid infinite loop

# 2. For Loop (Using range function)
# range(stop) -> generates numbers from 0 to stop-1
# range(start, stop) -> generates numbers from start to stop-1
# range(start, stop, step) -> increments by step

print("Printing 1 to 5:")
for i in range(1, 6): 
    print(i)

print("Printing even numbers up to 10:")
for i in range(2, 11, 2): # starts at 2, ends at 10, jumps by 2
    print(i)

# 3. Loop Control Statements (break, continue, pass)

# break: stops the loop completely
print("Break example:")
for i in range(1, 10):
    if i == 5:
        break # Exits the loop when i becomes 5
    print(i)

# continue: skips the current iteration and moves to the next one
print("Continue example:")
for i in range(1, 6):
    if i == 3:
        continue # Skips printing 3
    print(i)

# pass: does nothing. Used as a placeholder for future code to avoid syntax errors
for i in range(5):
    pass # I will write code here later