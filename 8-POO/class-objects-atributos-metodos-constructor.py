"""La programación orientada a objetos (POO) en Python, se encuentra totalmente soportada y se utiliza ampliamente en el desarrollo de aplicaciones. Aquí te contamos a detalle más acerca de este paradigma:"""

"""
Clases y Objetos: En la POO, una clase es una plantilla o modelo que define las propiedades y comportamientos de un objeto. Un objeto es una instancia de una clase, lo que significa que se crea a partir de la clase y tiene sus propias características y comportamientos. Para definir una clase en Python, se utiliza la palabra clave class, seguida del nombre de la clase:"""

class MiClase:
    # Definición de propiedades y métodos de la clase

# Para crear un objeto a partir de una clase, se utiliza la siguiente sintaxis:
objeto = MiClase()

"""Atributos: Los atributos son variables que se asocian a los objetos y almacenan información específica de cada instancia de la clase. Pueden ser variables de instancia, que son propias de cada objeto, o variables de clase, que son compartidas por todas las instancias de la clase. Los atributos se definen dentro de la clase y se acceden utilizando la sintaxis objeto.atributo:"""

class MiClase:
    variable_de_clase = "Compartida por todos los objetos"

    def __init__(self):
        self.variable_de_instancia = "Propia de cada objeto"

objeto = MiClase()
print(objeto.variable_de_instancia) # Output: "Propia de cada objeto"
print(objeto.variable_de_clase) # Output: "Compartida por todos los objetos"

"""Métodos: Los métodos son funciones definidas dentro de una clase y se utilizan para realizar operaciones relacionadas con los objetos de la clase. Los métodos pueden acceder y modificar los atributos de un objeto. El primer parámetro de un método siempre es self, que hace referencia al objeto en sí mismo. A través de self, se puede acceder a los atributos y otros métodos de la clase:"""

class MiClase:
    def mi_metodo(self):
        print("Hola desde el método")

objeto = MiClase()
objeto.mi_metodo() # Output: "Hola desde el método"

"""Constructor: El constructor es un método especial que se ejecuta automáticamente al crear un objeto a partir de una clase. En Python, el constructor se define utilizando el método __init__() y se utiliza para inicializar los atributos de la clase. Los parámetros que recibe el constructor son aquellos que se deben pasar al crear un objeto:"""

class MiClase:
    def __init__(self, parametro):
        self.atributo = parametro

objeto = MiClase("Valor del atributo")
print(objeto.atributo) # Output: "Valor del atributo"
