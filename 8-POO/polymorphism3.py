class MiClase:
    """Class MiClase to practice Polymorphism"""
    def __init__(self):
        # Attribute private but I can get from the object 
        self._atributo_privado = 10
      
        # Attribute private but I not can get from the object 
        self.__atributo_privado = 100
        
      # Attribitu public
        self.atributo_privado = 20

    # Decorator to create a method and get the attribute private self.__atributo_privado
    @property
    def atributo_publico(self):
      return self.__atributo_privado

    #Decorator to modify the attribute self.__atributo_privado
    @atributo_publico.setter
    def atributo_publico(self, x):
      self.__atributo_privado = x


# Object of the instantiated class
object = MiClase()

# Print __atribute_privado 
# Python renanme with the _NameClase__atribut0_ptivado
print(f"Hello: {object._MiClase__atributo_privado}")

# Print "_atribute_privado"
print(object._atributo_privado)

# Print __atribute_privado by the method with @aproperty decorator
print(object.atributo_publico)

# Modify __atribute_privado by the method with @atributo_publico.setter decorator
object.atributo_publico = 1

# Print __atribute_privado by the method with @aproperty decorator
print(object.atributo_publico)

print(object.atributo_privado)