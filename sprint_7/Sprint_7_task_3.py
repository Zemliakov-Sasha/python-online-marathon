class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    """Class for Truck"""

    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    """Class for Car"""

    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"


class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.adapted_methods = adapted_methods["wheels"]
        self.name = self.obj.name

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""

    def wheels(self):
        return self.adapted_methods()

    def original_dict(self):
        """Print original object dict"""
        pass


objects = []
motorCycle = MotorCycle()
objects.append(Adapter(motorCycle, wheels=motorCycle.TwoWheeler))
truck = Truck()
objects.append(Adapter(truck, wheels=truck.EightWheeler))
car = Car()
objects.append(Adapter(car, wheels=car.FourWheeler))
for obj in objects:
    print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))





