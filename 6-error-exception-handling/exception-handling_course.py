"""El manejo de errores en Python es una parte fundamental de la programación para garantizar que nuestros programas sean robustos y puedan manejar situaciones inesperadas. Python proporciona diversas herramientas y técnicas para manejar y controlar errores."""

"""En Python, los errores se conocen como excepciones y se producen cuando ocurre una situación inesperada durante la ejecución de un programa. Algunos ejemplos comunes de excepciones son:
TypeError, NameError, ValueError, entre otros."""

"""A continuación, se presenta una descripción detallada sobre el manejo de errores en Python:"""

"""Bloques try-except: El bloque try-except se utiliza para capturar y manejar excepciones. El código sospechoso de causar una excepción se coloca dentro del bloque try, y si se produce alguna excepción, se ejecuta el bloque except correspondiente."""

try:
    # Código sospechoso
  pass
except ExceptionType:
    # Manejar la excepción
  pass


# El bloque except puede manejar excepciones específicas o genéricas. Por ejemplo:
try:
    # Código sospechoso
  pass
except ValueError:
    # Manejar la excepción ValueError
  pass
except:
    # Manejar cualquier otra excepción
  pass


# Bloque finally: El bloque finally se utiliza para ejecutar código que debe ejecutarse sin importar si se produjo una excepción o no. Este bloque se coloca después del bloque try-except.
try:
    # Código sospechoso
  pass
except ExceptionType:
    # Manejar la excepción
  pass
finally:
    # Código que se ejecuta siempre
  pass


# Cláusula raise: La cláusula raise se utiliza para generar manualmente una excepción en Python. Esto nos permite lanzar una excepción específica cuando ocurre una condición no deseada.
 if condition:
    raise ExceptionType("Mensaje de error")
  

# Por ejemplo, para generar una excepción TypeError, se puede utilizar la siguiente línea de código:
raise TypeError("Se esperaba un tipo de dato diferente")


# Bloques try-except-else: También se puede utilizar un bloque else junto con try-except para especificar un código que se ejecutará si no se produce ninguna excepción.
try:
    # Código sospechoso
  pass
except ExceptionType:
    # Manejar la excepción
  pass
else:
    # Código que se ejecuta si no hay excepciones
  pass

# Manejo de excepciones específicas: Además de capturar excepciones genéricas, también es posible manejar excepciones específicas y personalizadas. Esto permite un manejo más granular y adaptado a situaciones particulares.
try:
    # Código sospechoso
  pass
except ValueError as ve:
    # Manejar excepción ValueError
  pass
except TypeError as te:
    # Manejar excepción TypeError
  pass