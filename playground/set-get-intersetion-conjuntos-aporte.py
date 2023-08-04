def find_set_intersection(sets):
  """Function find set intersection"""
  if not sets:
    return set()

  # Calculate the intersection of the sets in the list
  set_intersection = sets[0].intersection(*sets[1:])
  return set_intersection


sets = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]

sets2 = []

response = find_set_intersection(sets)
print(response)
