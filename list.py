# List is a built in data structure used to store an ordered collection of items. 
# They are dynamic, resizable and can store multiple data types.

# List elements can be changed, updated, added, or removed after the list is created.
# Elements maintain the order in which they are inserted.
# Elements are accessed using their position, starting from index 0.

# Lists can be created in multiple ways, such as using square brackets [], the list() constructor or by repeating elements.
# (i) Using square brackets []
a = [1, 2, "mango", True]
print(a)

# (ii) Using list() constructor
# A list can also be created by passing an iterable 
# (such as tuple, string or another list) to the list() constructor.
list1 = list((1, 2, 3, 'apple', 4.5)) # basically we type casted a tuple into list
print(list1)

list2 = list("APPLE") #basically we type casted a string into list
print(list2)

# Creating List with Repeated Elements: 
# A list with repeated elements can be created using the multiplication (*) operator.
list3 = [6] * 5
print(list3)

# Accessing Elements in a List :
# Elements in a list are accessed using indexing. 
# Python uses zero-based indexing, meaning a[0] represents the first element. 
# Negative indexing is also supported, where -1 accesses the last element.
nums = [1, 2, 3, 4, 5]
print(nums[0])
print(nums[-1])

# To update / change the element :
# Since lists are mutable, elements can be updated by assigning new values using their index.
nums[2] = 9
print(nums)

# Nested List : 
# A nested list is a list that contains another list as its element. 
# It is commonly used to represent matrices or tabular data. 
# Nested elements can be accessed by chaining multiple indexes.
nest = [[1, 2], [3, 4]]
print(nest[0]) # will print the element at index 0 in the list "nest", which is another list : [1,2]
print(nest[1][0]) # will print the element at index 0 of the element at index 1 in the list "nest"

# We can use loop to Iterate Over a list, allowing operations to be performed on each element.
people = ['sam', 'musk', 'ben']
for i in people:
    print(i)