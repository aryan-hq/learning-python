# Strings are sequence of characters written inside quotes. 
# It can include letters, numbers, symbols and spaces. 
# Python does not have a separate character data type.
# A single character is treated as a string of length one.
# Strings are commonly used for text handling and manipulation.


# Strings can be created using either single ('abc') or double ("abc") quotes. Both behave the same.
str = "aryan-hq"  
print(str)

# Use triple quotes ('''text''' ) or ( """text""") for strings that span multiple lines. 
# Newlines are preserved.
s = """Hi.
I am Aryan.
How are you?"""
print(s)

# Strings are indexed sequences. 
# Positive indices start at 0 from the left, negative indices start at -1
print(s[1], s[-2])

# Strings can be combined by using + operator.
a = "Hello"
b = "World"
print(a + " " + b)

# A string can be repeated multiple times using * operator.
print(a * 5)

#String Slicing :
# Slicing is a way to extract a portion of a string by specifying the start and end indexes. 
# Syntax for slicing : string_name[start:end]
# where start is starting index and end is stopping index (excluded).
s2 = "ARYANHQ"
print(s2[1:5]) 
print(s2[:4]) # will start from begining as no value is given for start and will go to index 4 excluded  
print(s2[5:]) # will start from index 5 and goes to the end as no value is given for end
print(s2[::-1]) # will print whole string in reverse

#Looping through string
print("Printing each character in s2 using loop : ")
for char in s2:
    print(char)


# To directly insert variables and expressions inside a string using {} brackets. :
name = "Aryan"
age = 101
print(f"Name: {name}, Age: {age}")

# .format() method allows inserting values into placeholders {} inside a string.
intro = "My name is {} and I am {} years old.".format("Aryan", 101)
print(intro)

# 'in' keyword is used to check whether a substring exists inside a string. 
# It returns True if the substring is found, otherwise it returns False.
print("ya" in name)
print("na" in name)