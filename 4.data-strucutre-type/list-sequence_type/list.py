# Go to the first item of the list
print("List of colores")
colors = ["red", "blue", "green"]
print(colors[0]) # red


# Update a specific value in the list.
print("\nUpdate list")
numbers = [1, 4, 5, 6, 2, 8]
print(numbers[0]) # 1
numbers[0] = 8
print(numbers) # [8, 4, 5, 6, 2, 8]


"""
Most used methods in lists
append(): Adds a new item to the end of the list

pop(): Allows you remove the last item in the list
or a specific index of the list: pop(0)
"""
print("\nAPPEND() Add new item")
colors = ["brown", "white", "newwine"]
colors.append("yellow")
print(colors) # ["brown", "white", "newwine", "yellow"]
print("\nPOP() Remove a item in specific index")
colors.pop(0)
print(colors) # ["brown", "white", "newwine"]

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

# reverse(): Reverses the order of the list items
print("\nREVERSE() Reverses the order of the list items")
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros) # [5, 4, 3, 2, 1]

# sort(): Sorts the list in ascending or descending order
print("\nSORT(): Sorts the list in ascending or descending order")
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numeros.sort()
print(numeros) # [1, 1, 2, 3, 4, 5, 5, 6, 9]

numeros.sort(reverse=True)
print(numeros) # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# IN: Check if "apple" is present in the list:
print("IN: Check if 'apple' is present in the list:")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")