import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self, pr_list):
        self.pr_list = pr_list
        self.total_price = 0
        self.discount1 = [1, 5, 7, 10, 20]
        self.discount2 = [0, 0.05, 0.1, 0.2]

    def get_total_price(self):
        st = 0
        for pr in self.pr_list:
            st = 0.3 if pr.count == 20 else None

            for i in range(len(self.discount1)-1):
                if pr.count in range(self.discount1[i], self.discount1[i+1]):
                    st = self.discount2[i]
            self.total_price += pr.price * pr.count * (1-st)
        return self.total_price


class CartTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Cart(products1).get_total_price(), 24785.0)


products1 = (Product('p1', 10, 4),
            Product('p2', 100, 5),
            Product('p3', 200, 6),
            Product('p4', 300, 7),
            Product('p5', 400, 9),
            Product('p6', 500, 10),
            Product('p7', 1000, 20))
cart = Cart(products)
print(cart.get_total_price())

