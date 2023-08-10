# Fallaba en un test:
# https://platzi.com/clases/7967-python-21-dias/63519-maneja-las-excepciones/

def calculate_discounted_price(price, discount):
  """Function calculate discount price"""
  try:
    if price < 0 or discount < 0:
      raise ValueError("El precio y el descuento deben ser valores positivos")
    discounted_price = price - (price * discount)
  except ValueError as e:
    raise e
  except TypeError:
    raise TypeError("El precio y el descuento deben ser números")
  except Exception as e:
    raise Exception("Ha ocurrido un error inesperado: " + str(e))
  return discounted_price


response = calculate_discounted_price(100, 0.2)
print(response)