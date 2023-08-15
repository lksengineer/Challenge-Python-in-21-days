"""El polimorfismo es un concepto fundamental en la programación orientada a objetos, y Python es un lenguaje que soporta este concepto de manera nativa. En términos simples, el polimorfismo permite que una sola interfaz pueda ser implementada por múltiples clases, permitiendo que diferentes objetos respondan de diferentes maneras a la misma llamada."""

"""En Python, el polimorfismo se logra a través de la herencia de clases y la sobrescritura de métodos. Por ejemplo, si tenemos una clase Animal con un método hablar(), podemos crear subclases como Perro y Gato, y sobrescribir el método hablar() para que cada subclase tenga su propia implementación. De esta manera, podemos llamar al método hablar() en un objeto de tipo Animal y obtener diferentes resultados dependiendo de la subclase."""

# La clase Animal que define un método hablar()
class Animal:
    def hablar(self):
        print('Sonidos de animal')

# Perro que hereda de la clase Animal y sobrescribe el método hablar()
# con una implementación específica
class Perro(Animal):
    def hablar(self):
        print('Guau guau!')

# Gato que hereda de la clase Animal y sobrescribe el método hablar()
# con otra implementación
class Gato(Animal):
    def hablar(self):
        print('Miau miau!')

# Ahora podemos crear objetos de las tres clases
# y llamar al método hablar(), que proporcionará
# una salida diferente para cada uno de ellos

animal = Animal()
perro = Perro()
gato = Gato()

animal.hablar()  # Sonidos de animal
perro.hablar()  # Guau guau!
gato.hablar()   # Miau miau!

"""El polimorfismo en Python es útil porque nos permite escribir código más modular y genérico, ya que podemos diseñar nuestras clases para que implementen una interfaz común, pero con comportamientos diferentes. Esto nos permite reutilizar código y aumentar la flexibilidad de nuestro programa."""

"""Además, el polimorfismo también es una técnica importante para la abstracción de datos, ya que nos permite ocultar detalles de implementación detrás de una interfaz común. Por ejemplo, si tenemos una clase Figura que tiene un método calcular_area(), podemos crear subclases como Rectángulo y Círculo que implementen el método de manera diferente, pero que todavía se comporten como una Figura. Esto nos permite abstraer la complejidad de la implementación y trabajar con objetos de manera más abstracta y genérica."""