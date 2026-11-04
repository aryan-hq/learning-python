# Python string methods are built-in functions that allow us to perform different operations on strings.
# Since strings are immutable in Python, 
# these methods return a new string instead of modifying the original one.

text = "   C and C++ both are programming languages.  "

# string_name.upper() converts all characters to uppercase 
print("Upper : ", text.upper())

# string_name.lower() converts all characters to lowercase.
print("Lower : ", text.lower())

# Capitalizes the first character of the string and makes other characters small. 
# It gives a copy, no change in original string.
print("Capitalised : ", text.capitalize())

# To replace a substring from another in a string.
text = text.replace("C++", "Python")
print("new text : ", text)

# To find a substring in a string and return the 1st index of first occurrence and -1 if not present.
print("Found Python : ", text.find("Python"))

# To check if a string starts with a substring. returns true/false 
print("Starts with 'the' : ", text.endswith("the"))

# To check if a string ends with a substring. returns true/false
print("Ends with 'es' : ", text.endswith("es.  "))

# string_name.strip() removes leading and trailing whitespace from the string.
print("After Strip : ", text.strip())

# To count the occurrence of substring.
print("'a' is present ", text.count("a"), " times.")

# To find length of the string.
print("length of text : ", len(text))

# To join elements of an iterable into a single string.
words = ["Python", "is", "easy"]
print("-".join(words))

# To delete the string : del string_name
del text

# There are many more string methods... 