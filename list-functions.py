list1 = [2, 3, 1, 2, 7, 7, 6]
print("List : ", list1)

list1.append(4) #adds one element at the end
print("List after appending 4 : ", list1)

list1.sort() #sorts in ascending order
print("List after sorting : ", list1)

list1.sort(reverse = True) #sorts in descending order
print("List after sorting in reverse : ", list1)

list1.reverse() #reverses list
print("List reversed : ", list1)

list1.insert(2, 9) #inserts element at the index
print("List after inserting 9 at index 2 : ", list1)

list1.remove(2) #removes the first occurrence of the element
print("List after removing element 2 first occurrence : ", list1)

list1.pop(3) #removes element at the index
print("List after pop at index 3 : ", list1)

print("No. of Occurrence of 7 in List : ", list1.count(7)) #counts occurrence of element

print("Index of first occurrence of 7 : ", list1.index(7)) #returns index of first occurrence of element

list2 = list1.copy() #creates copy of the list
print("Copy List : ", list2)

list1.clear() #list empty
print("List after clear : ", list1)