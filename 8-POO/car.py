class Car:
    """Class Car"""
    def __init__(self, brand, model, year, mileage):
         """Car Class Constructor and its attributes"""
         self.brand = brand
         self.model = model
         self.year = year
         self.mileage = mileage
         self.state = False

    def turnOn(self):
        """TurnOn Method"""
        self.state = True

    def turnOff(self):
        """TurnOn Method"""
        self.state = False

    def drive(self, kilometers):
        """drive Method"""
        if not self.state:
            raise Exception("El auto está apagado")
        self.mileage += kilometers


if __name__ == '__main__':
    """Start function"""
    toyota = Car("Toyota", "Corolla", 2020, 0)
    toyota.turnOn()
    toyota.drive(100)
    # print(toyota.brand)
    # print(toyota.model)
    # print(toyota.year)
    print(toyota.mileage)
    # print(toyota.state)
