def find_set_intersection(sets):
  """Function find set intersection"""
  if len(sets) == 0:
    return set()

  intersections = sets[0]
  for conjunto in sets[1:]:
      intersections = intersections.intersection(conjunto)
      # intersections &= conjunto
      # intersections = intersections & conjunto
  return intersections
  
sets = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]

sets2 = []

response = find_set_intersection(sets)
print(response)
