def calculate_average(numbers):
  """Function to calculate the average"""
  # average = map(lambda num: num, numbers)
  try:
    if len(numbers) == 0:
      raise ValueError("La lista está vacía")
   
    return sum(num for num in numbers) / len(numbers)

  except TypeError:
    raise TypeError("La lista contiene elementos no numéricos")


response = calculate_average([1, 2, 3, "4", 5])
print(response)