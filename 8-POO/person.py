class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

    def cumplir_anios(self):
        self.edad += 1

# Creamos objetos de la clase Persona
persona1 = Persona("Juan", 30, "Masculino")
persona2 = Persona("María", 25, "Femenino")

# Llamamos a los métodos de los objetos
persona1.saludar()  # Salida: Hola, mi nombre es Juan.
persona2.saludar()  # Salida: Hola, mi nombre es María.

print(persona1.edad)  # Salida: 30
persona1.cumplir_anios()
print(persona1.edad)  # Salida: 31