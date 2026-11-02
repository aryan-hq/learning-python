text = input("Enter Text : ")

print("Ends with 'er' : ", text.endswith("er")) #to check if a string ends with a substring. returns true/false

print("Capitalised : ", text.capitalize()) #capitalizes the first character of the string and makes other characters small. it gives a copy, no change in original string.

text = text.replace("c", "python") #replaces a substring from another in a string.
print("new text : ", text)

print("Found Python : ", text.find("python")) #finds a substring in a string and returns the 1st index of first occurrence and -1 if not present.

print("'an' is present ", text.count("an"), " times.") #counts the occurrence of substring.

print("length of text : ", len(text)) #prints length