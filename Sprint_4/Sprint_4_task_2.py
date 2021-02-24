class Pizza:
    number = 0
    def __init__(self, ing):
        self.ingredients = ing
        Pizza.number += 1
        self.order_number = Pizza.number
        print(self.number)

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])

p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
p2 = Pizza.garden_feast()
p3 = Pizza.meat_festival()
p4 = Pizza.hawaiian()
p5 = Pizza(["bacon", "parmesan", "ham"])   # order 1
p6 = Pizza(["bacon", "parmesan", "ham"])   # order 1


print("====================")
print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
print(p5.order_number)
print(p6.order_number)
