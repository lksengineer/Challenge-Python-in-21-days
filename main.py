mySet = {1, 3, 2, 4, 6, 3}
print(mySet)

mySet.add(7)
print(mySet)

mySet.add(";")
print(mySet)

mySet.pop()
print(mySet)

mySet.pop()
print(mySet)

mySet.add(";")
print(mySet)

mySet.remove(";")
print(mySet)

mySet.add(";")
print(mySet)

mySet.discard("'';")
print(mySet)

# count(): Counts how many times an element is in a list
print("\nCOUNT() How many times an element in the list")
numbers = [1, 4, 1, 3, 2, 1]
print(numbers.count(1)) # 3

# extend(lista): Permite extender una lista agregándole los elementos de otra lista.
print("\nEXTEND() Extiende una lista agregándole los elementos de otra lista")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
# list2.extend(list1)
print(list1 + list2)
print(list1) # [1, 2, 3, 4, 5, 6]
print(list2) # [4, 5, 6]