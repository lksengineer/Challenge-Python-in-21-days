"""Herencia: La herencia es un concepto clave en la POO que permite crear nuevas clases basadas en clases existentes. La clase original se conoce como clase base o superclase, y la nueva clase se llama clase derivada o subclase. La subclase hereda los atributos y métodos de la superclase y puede agregar nuevos atributos o métodos, o modificar los existentes. En Python, se utiliza la palabra clave class seguida del nombre de la subclase y entre paréntesis el nombre de la superclase:"""

class ClaseBase:
    # Definición de la clase base

class SubClase(ClaseBase):
    # Definición de la subclase

"""Polimorfismo: El polimorfismo es la capacidad de objetos de diferentes clases de responder a un mismo mensaje de diferentes formas. En Python, el polimorfismo se logra a través de la implementación de métodos con el mismo nombre en diferentes clases. Cada clase puede tener su propia implementación del método, pero se llama al método adecuado según el tipo de objeto con el que se esté trabajando."""

class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("Guau!")

class Gato(Animal):
    def sonido(self):
        print("Miau!")

def hacer_sonar(animal):
    animal.sonido()

perro = Perro()
gato = Gato()

hacer_sonar(perro) # Output: "Guau!"
hacer_sonar(gato) # Output: "Miau!"