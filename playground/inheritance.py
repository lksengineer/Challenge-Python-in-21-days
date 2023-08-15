"""En este desafío, debes crear una jerarquía de
clases mediante el uso de la herencia.

 La clase base será Animal con las propiedades name,
age y specie y un método getInfo que devuelve
un objeto con la información del animal.

 Luego, debes crear una clase Mammal que herede de Animal y
tenga una propiedad adicional hasFur y un método
getInfo que sobreescriba al del padre y incluya la
información de hasFur.

Finalmente, debes crear una clase Dog que herede de Mammal y tenga
una propiedad adicional breed y un método getInfo que sobreescriba al
del padre y incluya la información de breed, al igual que el método
bark que devuelva el string "woof!". Las propiedades de specie y
hasFur deben estar incluídas como "dog" y True respectivamente
desde la implementación por lo que no
debe ser necesario pasar los valores a
la hora de crear la instancia.

Ejemplo 1
Input:
bird = Animal("pepe", 1, "bird")
bird.getInfo()

Output:
{
  "name": "pepe",
  "age": 1,
  "specie": "bird",
}

Ejemplo 2
Input:
hippo = Mammal("bartolo", 3, "hippo", false)
hippo.getInfo()

Output:
{
  "name": "bartolo",
  "age": 3,
  "specie": "hippo",
  "hasFur": false,
}

Ejemplo 3
Input:
dog = Dog("fido", 4, "pastor aleman");
dog.bark()

Output:
"woof!"
"""


class Animal:
    """Class Animal. Base class"""
    def __init__(self, name, age, specie):
        self.name = name
        self.age = age
        self.specie = specie

    def getInfo(self):
        """Get info method."""
        return {
            'name': self.name,
            'age': self.age,
            'specie': self.specie,
        }


class Mammal(Animal):
    """Class Mammal. SubClass of Class Animal"""
    def __init__(self, name, age, specie, hasFur):
        super().__init__(name, age, specie)
        self.hasFur = hasFur

    def getInfo(self):
        """Get info method"""
        return {
            'name': self.name,
            'age': self.age,
            'specie': self.specie,
            'hasFur': self.hasFur,
        }


class Dog(Mammal):
    """Class Dog. SubClass of Class Mammal"""
    def __init__(self, name, age, breed):
        # super().__init__(name, age, "dog", True)
        super().__init__(name, age, specie="dog", hasFur=True)
        self.breed = breed

    def getInfo(self):
        """Get info method to return without repeat the object """
        info = super().getInfo()
        info['breed'] = self.breed
        return info
        # return {
        #     'name': self.name,
        #     'age': self.age,
        #     'specie': self.specie,
        #     'hasFur':self.hasFur,
        #     'breed': self.breed,
        # }

    def bark(self):
        """Bark method"""
        return "woof!"

# Example 1
# bird = Animal("pepe", 1, "bird")
# r = bird.getInfo()
# print(r)

# Example 2
# hippo = Mammal("bartolo", 3, "hippo", False)
# r = hippo.getInfo()
# print(r)

# Example 3
dog = Dog("fido", 4, "pastor aleman")
r = dog.bark()
print(r)
r = dog.getInfo()
print(r)