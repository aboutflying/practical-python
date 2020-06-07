class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt
        # print(f'Sold {amt} of {self.name}. We now have {self.shares} shares of {self.name}.')

class MyStock(Stock):
    def cost(self):
        return 1.25 * super().cost()

    def panic(self):
        self.sell(self.shares)