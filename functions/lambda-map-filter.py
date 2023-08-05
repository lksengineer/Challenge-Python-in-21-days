"""
Son funciones anónimas que se pueden definir de manera concisa en una sola línea. A diferencia de las funciones regulares, las funciones lambda no requieren un nombre y se utilizan principalmente para realizar operaciones simples y rápidas.
"""

"""
La sintaxis básica de una lambda es la siguiente:
   lambda argumentos: expresion

argumentos: son los parámetros de la función.
expresion: es la operación que se realizará y se devolverá como resultado.

Las lambdas se utilizan comúnmente en combinación con otras funciones, como map(), filter() y reduce(), para realizar operaciones sobre secuencias de manera más concisa.
"""

# Ejemplos para ilustrar el uso de las lambdas:

# Ejemplo 1: Función lambda simple
suma = lambda a, b: a + b
resultado = suma(2, 3)
print(resultado)  # Output: 5

# Ejemplo 2: Uso de lambda con map()
# La función retornará un objeto map que posteriormente podemos convertir a una lista o tupla.
numeros = [1, 2, 3, 4, 5]
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)  # Output: [2, 4, 6, 8, 10]



# Ejemplo 3: Uso de lambda con filter()
#  devuelve un objeto iterable con todos aquellos valores de una colección de datos que cumplen una determinada condición.
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Output: [2, 4]
