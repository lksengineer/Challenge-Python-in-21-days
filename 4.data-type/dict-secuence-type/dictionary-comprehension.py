"""Dictionary comprehensions, son una característica poderosa de Python que nos permite crear diccionarios de forma concisa y eficiente utilizando una sintaxis compacta. Son una forma elegante de transformar o filtrar elementos de una secuencia para crear un nuevo diccionario"""

# La sintaxis básica de una dictionary comprehension es la siguiente:
#nuevo_diccionario = {clave_expresion: valor_expresion for elemento in secuencia if condicion}

"""clave_expresion es una expresión que define cómo se generarán las claves del nuevo diccionario.
valor_expresion es una expresión que define cómo se generarán los valores del nuevo diccionario.
elemento es una variable que representa cada elemento de la secuencia mientras se recorre.
secuencia es la secuencia de origen de la cual se obtendrán los elementos.
condicion es una condición opcional que filtra los elementos de la secuencia."""


#ejemplo para uso de las dictionary comprehensions:
personas = [("Juan", 25), ("María", 30), ("Pedro", 20)]

# Crear un nuevo diccionario con el nombre como clave y la edad como valor, solo para personas mayores de 25 años
personas_mayores = {nombre: edad for nombre, edad in personas if edad > 25}
print(personas_mayores)  # Output: {'María': 30}

# Crear un nuevo diccionario con el nombre como clave y la longitud del nombre como valor para todas las personas
diccionario_longitudes = {nombre: len(nombre) for nombre, _ in personas}
print(diccionario_longitudes)  # Output: {'Juan': 4, 'María': 5, 'Pedro': 5}