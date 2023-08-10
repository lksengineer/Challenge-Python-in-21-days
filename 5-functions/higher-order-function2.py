# High Order Functions: funciones que cumplen al menos uno de los siguientes criterios:
# - Toman una o más funciones como argumentos.
#- Devuelven una función como resultado.

"""
Estas funciones son fundamentales para la programación funcional y nos permiten trabajar con funciones de manera modular y flexible.

En Python, algunas de las High Order Functions incorporadas más comunes son:

- map(función, secuencia): Aplica la función a cada elemento de la secuencia y devuelve un iterador con los resultados.

- filter(función, secuencia): Filtra los elementos de la secuencia según la función dada y devuelve un iterador con los elementos que cumplan la condición.

- reduce(función, secuencia): Aplica la función a los elementos de la secuencia de manera acumulativa, reduciéndolos a un solo valor.

- sorted(secuencia, key=función): Ordena la secuencia según la función de clave dada y devuelve una nueva lista con los elementos ordenados.
Estas funciones de orden superior nos permiten escribir código más limpio y expresivo al evitar la necesidad de bucles explícitos y operaciones repetitivas.

Además, podemos crear nuestras propias High Order Functions en Python. Esto se logra utilizando la capacidad de Python para tratar las funciones como objetos de primera clase. Podemos pasar funciones como argumentos a otras funciones, devolver funciones desde funciones y almacenar funciones en variables.
"""

# Aquí hay un ejemplo acerca del uso de las High Order Functions en Python:

def aplicar_operacion(func, a, b):
  return func(a, b)

def suma(a, b):
  return a + b

def resta(a, b):
  return a - b

resultado = aplicar_operacion(suma, 5, 3)
print(resultado)  # Output: 8

resultado = aplicar_operacion(resta, 10, 7)
print(resultado)  # Output: 3