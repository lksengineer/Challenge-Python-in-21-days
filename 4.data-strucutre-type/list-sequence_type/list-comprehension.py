"""list comprehensions son una forma elegante de transformar o filtrar elementos de una lista existente para crear una nueva lista."""

# La sintaxis básica de una list comprehension es la siguiente:

# nueva_lista = [expresion for elemento in lista_original if # condicion]

"""expresion es una expresión que define cómo se transformarán los elementos de la lista original para obtener los elementos de la nueva lista.
elemento es una variable que representa cada elemento de la lista original mientras se recorre.
lista_original es la lista de origen de la cual se obtendrán los elementos.
condicion es una condición opcional que filtra los elementos de la lista original.
Aquí hay un ejemplo acerca del uso de las list comprehensions:"""

numeros = [1, 2, 3, 4, 5]

# Crear una nueva lista con el cuadrado de los números pares de la lista original
cuadrados_pares = [num ** 2 for num in numeros if num % 2 == 0]
print(cuadrados_pares)  # Output: [4, 16]

# Crear una nueva lista con los números impares multiplicados por 2 de la lista original
impares_multiplicados = [num * 2 for num in numeros if num % 2 != 0]
print(impares_multiplicados)  # Output: [2, 6, 10]


# Las list comprehensions también pueden incluir cláusulas else
# para manejar casos en los que la condición no se cumple.

numeros = [1, 2, 3, 4, 5]

# Crear una nueva lista con los números pares de la lista original, y 'No par' para los impares
numeros_par_o_no_par = ['Par' if num % 2 == 0 else 'No par' for num in numeros]
print(numeros_par_o_no_par)  # Output: ['No par', 'Par', 'No par', 'Par', 'No par']
