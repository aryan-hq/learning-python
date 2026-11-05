# Python set methods allow us to perform modifications and mathematical set operations 
# (like union, intersection, and difference).

group_A = {"apple", "banana", "cherry"}
group_B = {"google", "microsoft", "apple"}

# Adding and Removing Elements

# set_name.add(item) : Adds a single element
group_A.add("orange")
print(group_A)

# set_name.update(iterable) : Adds multiple items (from a list, tuple, or another set)
group_A.update(["mango", "grapes"])
print(group_A)

# Removing items: remove() vs discard()
# set_name.remove(item) : Removes the item, but throws an ERROR if the item doesn't exist.
group_A.remove("banana")

# set_name.discard(item) : Removes the item, but does NOT throw an error if it doesn't exist.
group_A.discard("banana") # No error even though banana is already gone
print(group_A)

# set_name.pop() : Removes and returns a random item 
# (because sets are unordered, you don't know which gets removed).
popped_item = group_A.pop()
print("Popped:", popped_item)

# set_name.clear() : Empties the set, leaving set()
# group_A.clear()

# Frozenset is an immutable version of a set. 
# Its elements cannot be changed after creation, but you can perform operations like union, 
# intersection and difference. Use frozenset() to create one.
s = set(["a", "b", "c"])
print("Normal Set:", s)

fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)

# Mathematical Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: Returns a new set with all items from both sets (duplicates are ignored)
# Syntax: A.union(B)  |  Shortcut operator: A | B
print("Union:", A.union(B))

# Intersection: Returns a new set with only the items that are present in BOTH sets
# Syntax: A.intersection(B)  |  Shortcut operator: A & B
print("Intersection:", A.intersection(B))

# Difference: Returns a new set with items in set A but NOT in set B
# Syntax: A.difference(B)  |  Shortcut operator: A - B
print("Difference (A - B):", A.difference(B))

# Symmetric Difference: Returns a new set with items that are NOT shared between the sets
# (Basically Union minus Intersection)
# Syntax: A.symmetric_difference(B)  |  Shortcut operator: A ^ B
print("Symmetric Difference:", A.symmetric_difference(B))

# issubset() and issuperset() return True/False based on whether one set contains another
C = {1, 2}
print("Is C a subset of A?", C.issubset(A)) # True, because 1 and 2 are in A