class WashingMachine:
    def __init__(self):
        self.w = Washing()
        self.r = Rinsing()
        self.s = Spinning()
        r = self.startWashing()

    def startWashing(self):
        res = [self.w.metod_processing(), self.r.metod_processing(), self.s.metod_processing()]
        print("\n".join(res))
        return "\n".join(res)


class Washing:
    def wash(self):
        return self.metod_processing()

    def metod_processing(self):
        return "Washing..."


class Rinsing:
    def rinse(self):
        return self.metod_processing()

    def metod_processing(self):
        return "Rinsing..."


class Spinning:
    def spin(self):
        return self.metod_processing()

    def metod_processing(self):
        return "Spinning..."


washingMachine = WashingMachine()
washingMachine.startWashing()
