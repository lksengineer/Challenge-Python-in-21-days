"""Polymorphism = Muchas formas"""


class Animal:
  """Class Animal"""

  def __init__(self, name):
    self.name = name

  def sound(self):
    """Sound method"""
    print(f"{self.name}: Guau Guau")


class Dog(Animal):
  """Class Dog"""
  pass


class Cat(Animal):
  """Class Cat"""

  def sound(self):
    """Sound method inherited"""
    print("Miau Miau")


class Vaca(Animal):
  """Class Vaca"""

  def sound(self):
    """Sound method inherited"""
    print("Muuuu")


class Oveja(Animal):
  """Class Obeja"""

  def sound(self):
    """Sound method inherited"""
    print("Meeeeeeee")


dog = Dog("Firulai")
dog.sound()

cat = Cat("Garffie")
cat.sound()

vaca = Vaca("Lola")
vaca.sound()

oveja = Oveja("Dumbo")
oveja.sound()
