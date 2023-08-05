def my_map(list, func):
  """Function emular map funciton"""
  # Aplicando map
  # list(map(lambda element: func(element), list))

  # Emulador map con functions
  # x = []
  # for element in list:
  #   x.append(func(element))
  # return x

  # Emulador map with list comprehension
  return [func(element) for element in list]
  

if __name__ == '__main__':
  """Start function"""
  # response = my_map([1, 2, 3, 4], lambda num: num * 2)
  
  response = my_map([
    {"name": "michi", "age": 2},
    {"name": "firulais", "age": 6}], lambda pet: pet["name"])
  
  print(response)