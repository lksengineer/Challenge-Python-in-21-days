"""Abrir un archivo: Para leer un archivo de texto, primero debemos abrirlo en modo lectura utilizando la función open(). El modo de apertura debe establecerse como “r” o “rt” para archivos de texto."""

file = open("archivo.txt", "r")

"""Leer todo el contenido: Una vez que hemos abierto el archivo, podemos leer todo su contenido utilizando el método read(). Este método devuelve una cadena que contiene todo el contenido del archivo."""

content = file.read()
print(content)

"""Leer línea por línea: Si deseamos leer el contenido del archivo línea por línea, podemos utilizar el método readline(). Este método lee una línea a la vez y mueve el indicador de posición del archivo a la siguiente línea."""

line = file.readline()
while line:
    print(line)
    line = file.readline()

"""Leer todas las líneas: Si queremos leer todas las líneas del archivo y almacenarlas en una lista, podemos utilizar el método readlines(). Este método devuelve una lista donde cada elemento es una línea del archivo."""

lines = file.readlines()
for line in lines:
    print(line)

"""Cerrar el archivo: Después de leer el archivo, es importante cerrarlo utilizando el método close(). Esto libera los recursos asociados al archivo y garantiza que no se produzcan conflictos de acceso en futuras operaciones."""

file.close()

"""Es importante tener en cuenta que la apertura y el cierre del archivo son operaciones necesarias para asegurar una manipulación adecuada de los archivos y evitar problemas de acceso o pérdida de datos.

Además, es una buena práctica utilizar bloques try-finally o with al leer archivos de texto. Estos bloques garantizan que el archivo se cierre correctamente, incluso si se produce una excepción durante el proceso de lectura."""

try:
    file = open("archivo.txt", "r")
    # Realizar operaciones de lectura
finally:
    file.close()

"""O utilizando el bloque with:"""

with open("archivo.txt", "r") as file:
    # Realizar operaciones de lectura.
