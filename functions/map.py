"""En Python, la función map nos permite aplicar una función sobre los items de un objeto iterable (lista, tupla, etc...)."""


# map() Sintaxis
# map(function, objeto iterable)
# La función retornará un objeto map que posteriormente podemos convertir a una lista o tupla.

# Function normal 
def cuadrado(numero):
 return numero * numero

print(cuadrado(2))


# Function map()
lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)

lista_resultado = list(resultado)
print(lista_resultado)

# Es posible utilizar map junto con una función lambda. En lo personal considero esta la mejor opción.
lista = [1,2,3,4,5]
resultado = map(lambda numero: numero * numero , lista)

lista_resultado = list(resultado)
print(lista_resultado)