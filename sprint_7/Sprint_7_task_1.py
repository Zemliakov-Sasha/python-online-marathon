from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product, ABC):
    def __init__(self):
        self.name_of_the_dish = "Fettuccine Alfredo"

    def cook(self):
        print(f"Italian main course prepared: {self.name_of_the_dish}")


class Tiramisu(Product, ABC):
    def __init__(self):
        self.name_of_the_dish = "Tiramisu"

    def cook(self):
        print(f"Italian dessert prepared: {self.name_of_the_dish}")


class DuckALOrange(Product, ABC):
    def __init__(self):
        self.name_of_the_dish = "Duck À L'Orange"

    def cook(self):
        print(f"French main course prepared: {self.name_of_the_dish}")


class CremeBrulee(Product, ABC):
    def __init__(self):
        self.name_of_the_dish = "Crème brûlée"

    def cook(self):
        print(f"French dessert prepared: {self.name_of_the_dish}")


class Factory(ABC):
    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory, ABC):
    def get_dish(self, type_of_meal):
        return FettuccineAlfredo() if type_of_meal == "main" else Tiramisu()


class FrenchDishesFactory(Factory, ABC):
    def get_dish(self, type_of_meal):
        return DuckALOrange() if type_of_meal == "main" else CremeBrulee()


class FactoryProducer:
    def get_factory(self, type_of_factory):
        return ItalianDishesFactory() if type_of_factory == "italian" else FrenchDishesFactory()


fp = FactoryProducer()
fac = fp.get_factory("italian")
main_dish = fac.get_dish("main")
main_dish.cook()

