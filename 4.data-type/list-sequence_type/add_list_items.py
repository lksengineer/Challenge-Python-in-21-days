# append() method to append an item in the last position:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# insert() method to insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# Extend list with extend() method
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add elements of a tuple to a list.
# You can add any iterable object (tuples, sets, dictionaries etc):
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

