# dictionary is in key : value pair, in values almost all data types are acceptable
# but in keys we can't use list and dictionary (basically datatypes which are mutable aren't allowed)
# Dictionaries are unordered, mutable & don't allow duplicate keys

raw = {
    "name" : "jeff",
    "course" : "B.Tech",
    "subjects" : ("PIC", "IT", "EVS", "DTP"),
    "percentage" : 89.4,
    "verified" : True
}

print(raw["subjects"]) #to access or print values of any key dict_name[key]
raw["name"] = "sam" #to change the value
raw["blood group"] = "B+" #to add new key value pair

null_dict = {} #to create dictionary with no data, we can add key value in future
print(raw)

#creating nested dictionary
student = {
    "name" : "musk",
    "subjects" : {
        "phy" : 92,
        "chem" : 89,
        "maths" : 96
    }
}
print(student["subjects"]["maths"])