"""Leer CSV
Además de leer archivos de texto en Python, también es común necesitar leer archivos CSV (Comma-Separated Values). Los archivos CSV contienen datos estructurados separados por comas, lo que los convierte en una forma popular de almacenar y compartir conjuntos de datos. Aquí te dejamos la forma de cómo leer archivos CSV en Python:"""

"""Importar el módulo csv: Antes de leer archivos CSV, debemos importar el módulo csv, que proporciona funciones y clases específicas para trabajar con este tipo de archivos."""

import csv

"""Abrir el archivo CSV: Al igual que con los archivos de texto, debemos abrir el archivo CSV en modo lectura utilizando la función open(). Es importante especificar el modo de apertura como “r” o “rt” para archivos de texto."""

with open('archivo.csv', 'r') as file:
    # Realizar operaciones de lectura del archivo CSV

"""Crear un objeto lector CSV: Para leer los datos del archivo CSV, necesitamos crear un objeto lector CSV utilizando la función reader() del módulo csv. Este objeto nos permitirá acceder a los datos fila por fila."""

with open('archivo.csv', 'r') as file:
  csv_reader = csv.reader(file)
  # Realizar operaciones de lectura del archivo CSV

"""Leer filas del archivo CSV: Utilizando el objeto lector CSV, podemos leer las filas del archivo CSV una a una utilizando un bucle for. Cada fila se representa como una lista de valores correspondientes a cada columna del archivo CSV."""

with open('archivo.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # Acceder a los valores de cada columna en la fila
        print(row)

"""Leer datos en diccionarios: Si el archivo CSV tiene una fila de encabezado que contiene los nombres de las columnas, podemos leer los datos en forma de diccionarios utilizando un objeto lector CSV con el método DictReader(). Esto nos permite acceder a los valores utilizando los nombres de las columnas como claves."""

with open('archivo.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Acceder a los valores utilizando los nombres de las columnas
        print(row['columna1'], row['columna2'])
      
"""Es importante tener en cuenta que los archivos CSV pueden tener diferentes delimitadores, como comas, punto y coma o tabulaciones. Si el archivo CSV utiliza un delimitador distinto de la coma, podemos especificarlo al crear el objeto lector CSV utilizando el parámetro delimiter."""