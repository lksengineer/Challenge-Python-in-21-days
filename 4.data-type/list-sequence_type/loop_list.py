"""
Loop Through a List
You can loop through the list items by using a for loop:
"""
# Print all items in the list, one by one:
thislist = ["banana", "apple", "cherry"]
id = 0
for x in thislist:
  id += 1
  print(f"Fruit{id}: {x}")


"""
Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.
"""
# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(f"Fruit{i + 1}: {thislist[i]}")


# Using a While Loop
# Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# Looping Using List Comprehension
# A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]