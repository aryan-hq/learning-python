# A tuple is a built in data collection type used to store multiple items in a single variable.
# Tuples are immutable, we can't change, add or remove elements once it is created.
# Because tuples are immutable (cannot be changed after creation), 
# Python tuples have only two built in methods: count() and index().

tup = (5, 8, 7, 2, 7, 9, 2, 2)
print(tup[1:4])

print(tup.index(7)) #returns index of the first occurrence of element
print(tup.count(2)) #counts total occurrence of element