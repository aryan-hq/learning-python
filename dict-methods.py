# Python dictionary methods are built-in functions that allow us to perform various operations 
# on dictionaries, such as adding, updating, accessing and removing key-value pairs.

raw = {
    "name" : "jeff",
    "course" : "B.Tech",
    "subjects" : ("PIC", "IT", "EVS", "DTP"),
    "percentage" : 89.4,
    "verified" : True
}

print(raw.keys()) # dict_name.keys() returns all the keys in the dictionary, 
# but doesn't return keys of nested dictionaries.
print(list(raw.keys())) # we can also type cast to get list or tuple etc. of keys

print(raw.values())  # dict_name.values() returns all the values in the dictionary
print(list(raw.values())) # we can also type cast to get list or tuple etc. of values

print(raw.items()) # returns all (key, value) pairs as tuples
# we can also access this dict_name.items tuple like :
items = list(raw.items()) 
print("Accessing dict_name.items tuple : ", items[0])

print(len(raw)) #to get the length (no. of key value pairs) in the dictionary
print(len(raw.keys())) # will give the same output as len(dict_name) but we can also use function inside function. :)


# To get values according to the keys there are 2 ways :
# 1> dict_name("key") but by this method if the key doesn't exist in the dictionary it will give error.
# 2> dict_name.get("key") by this method if the key doesn't exist in the dictionary it will give "None". (no error)

print(raw.get("name")) #it will give the value of key "name"

# To add new key value pair using function
raw.update({"city" : "Delhi", "age" : 67})
print(raw)

#To create a copy of a dictionary :
new_dict = raw.copy() # dict_name.copy() returns a shallow copy of the dictionary.

#To clear the dictionary (removes all key value pairs) :
raw.clear()
print(raw)

# To remove the specified key and return its value : dict_name.pop("key")
print(new_dict.pop("age"))
print(new_dict)

#To remove and return the last inserted key-value pair : dict_name.popitem()
print(new_dict.popitem())
print(new_dict)

# dict_name.setdefault(key, default_value) 
# Returns the value of a key if it exists. Otherwise, inserts the key with the specified default value.
new_dict.setdefault("age", 25)
print(new_dict)

# dict.fromkeys(iterable, value)
# Creates a new dictionary using the given iterable as keys and assigns the same default value to all keys.
d = dict.fromkeys(new_dict, "NA")
print(d)