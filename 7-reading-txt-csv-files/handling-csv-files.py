# csv model
import csv


#creando manualmente un csv
archivo = open('archivo_csv.csv', 'w')
encabezado='"id", "nombre", "edad", "direccion"'
archivo.write(encabezado + '\n')
for i in range(100):
    archivo.write('{},"usuario{}",{},"calle {}, carrera {}"\n'.format(i, i, 30 + (i % 10), 100 + i, 200 - i))
archivo.close()


# Ahora lo leemos se importa el modulo csv
archivo = open('archivo_csv.csv', 'r')
csv_reader = csv.reader(archivo)
for fila in csv_reader:
    print(fila)
archivo.close()

# Ahora queremos obtener una lista de diccionarios. Aqui es clave la primera linea del archivo csv.
archivo = open('archivo_csv.csv', 'r')
csv_dict_reader = csv.DictReader(archivo)
lista_diccionarios = list(csv_dict_reader)
for i in range(10,20):
    print(lista_diccionarios[i])

archivo.close()