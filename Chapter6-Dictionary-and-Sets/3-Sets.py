# Set is a built-in Python data type used to store a collection of unique items.

# Stores only unique elements; duplicate values are automatically ignored.
# The set itself is mutable (you can add/remove items), but its elements must be immutable.
# Unordered, unindexed collection, so elements do not have a fixed position and cannot be accessed using indexes.
# Supports fast search, insertion and deletion operations using hashing internally.

# They are written with curly brackets {}, just like dictionaries, but without key-value pairs.

# Creating a set
subjects = {"PIC", "IT", "EVS", "DTP", "IT"} # See "IT" is repeated
print(subjects) # But output will not contain the duplicate "IT" and the order may change

# Creating an empty set
# null_set = {} # WRONG! This creates an empty dictionary, not a set.
null_set = set() # CORRECT way to create an empty set
print(type(null_set))

# Sets can contain different data types (strings, ints, booleans)
# Note: True and 1 are considered the same value in sets, and False and 0 are the same.
mixed_set = {"jeff", 89.4, True, 1, 0, False}
print(mixed_set) # 1 and False will be removed as duplicates of True and 0

# Since sets are unordered and unindexed, you CANNOT access items using an index like subjects[0].
# But you can loop through them or check if an item exists:
print("PIC" in subjects) # Returns True if "PIC" is in the set