class Goods:
    def __init__(self, price, discount_strategy = None):
        self.price = price
        self.discount_strategy = discount_strategy

    def __str__(self):
        return self.price_after_discount()

    def price_after_discount(self):

        nPrice = self.price if self.discount_strategy == None else self.discount_strategy(self.price)
        return f"Price: {self.price}, price after discount: {nPrice}"


def on_sale_discount(order):
    return order*0.5


def twenty_percent_discount(order):
    return order*0.8


print(Goods(20000))