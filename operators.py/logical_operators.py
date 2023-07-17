"""
(AND)
Evalua si ambas condiciones son verdaderas.
"""
edad = 25
mayor_de_edad = edad >= 18

if edad >= 18 and mayor_de_edad:
  print("Eres mayor de edad")
else:
  print("Aún eres menor de edad")


"""
OR (or):
Evalúa si al menos una de las expresiones es verdadera.
"""
edad = 25
tiene_identificacion = False

if edad >= 18 or tiene_identificacion:
  print("Puedes trabajar legalemente")
else:
  print("No tienes la edad o la identificación suficiente para trabajar legalmente")


"""
NOT (not)**:
Este operador lógico invierte el valor de la expresión.
"""
es_fin_de_semana = True

if not es_fin_de_semana:
  print("A trabajar")
else:
  print("A disfrutar del fin de semana")
