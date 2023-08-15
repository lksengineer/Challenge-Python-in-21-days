# Clases, objectos y atributos
# class POO:
#   """Class POO"""
#   variable_class = "Variable de la clase"
#   def __init__(self):
#     """varible instace"""
#     self.variable_instance = "Variable instance"

# objeto = POO()
# print(objeto.variable_class)
# print(objeto.variable_instance)


# Herecnia
# class Motor(POO):
#   variable_class = "Variable de la clase Motor"
#   # def __init__(self):
#   #   """varible instace"""
#   #   self.variable_instances = "Variable instance POO"

# objeto2 = Motor()
# print(objeto2.variable_class)
# print(objeto2.variable_instance)
# # print(objeto2.variable_instances)

# Polimorfismo
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

# Forma 1 mia de sona el metodo
Perro().sonido()
Gato().sonido()

# Forma 2 mia de sona el metodo
gato.sonido()
perro.sonido()

# Forma 3 ensenada en clase de sonar el metodo
hacer_sonar(perro) # Output: "Guau!"
hacer_sonar(gato) # Output: "Miau!"
