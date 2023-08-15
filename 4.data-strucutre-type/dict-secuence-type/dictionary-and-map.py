"""En Python, los diccionarios y los mapas son esencialmente lo mismo. Un diccionario es una colección desordenada de elementos. Cada elemento de un diccionario tiene una clave/valor. Los diccionarios son optimizados para recuperar valores cuando se conoce la clave."""

# Aquí hay un ejemplo de cómo se utiliza un diccionario en Python:

# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a un valor por su clave
print(mi_diccionario["nombre"])  # Salida: Juan

# Cambiar el valor de una clave
mi_diccionario["edad"] = 31

# Añadir una nueva clave/valor
mi_diccionario["profesion"] = "Ingeniero"

# Eliminar una clave/valor
del mi_diccionario["ciudad"]

# Comprobar si una clave existe
if "nombre" in mi_diccionario:
    print("La clave 'nombre' existe en el diccionario")

# Iterar sobre las claves
for clave in mi_diccionario:
    print(clave)

# Iterar sobre los valores
for valor in mi_diccionario.values():
    print(valor)

# Iterar sobre las claves y los valores
for clave, valor in mi_diccionario.items():
    print("La clave es " + clave + " y el valor es " + str(valor))

"""La función 
map()
 es una función incorporada en Python que toma en dos argumentos: una función y un iterable. 
map()
 aplica la función a todos los elementos del iterable y devuelve un objeto map.

Aquí hay un ejemplo de cómo se utiliza 
map()
 en Python:"""

# Crear una función que calcula el cuadrado de un número
def cuadrado(n):
    return n * n

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Usar map para aplicar la función cuadrado a todos los números de la lista
cuadrados = map(cuadrado, numeros)

# Convertir el objeto map a una lista y imprimirlo
print(list(cuadrados))  # Salida: [1, 4, 9, 16, 25]

"""En este ejemplo, 
map()

aplica la función 
cuadrado()
 a cada elemento de la lista 
numeros
. El resultado es un nuevo objeto map que contiene los cuadrados de todos los números en la lista original."""