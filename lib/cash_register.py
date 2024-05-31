class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.prices = []  # List to store prices of each item
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.prices.extend([price] * quantity)  # Store the price of each item

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.prices.pop()  # Get the price of the last item
            self.total -= last_item_price
            # Remove the last item from the items list for the corresponding price
            for _ in range(self.prices.count(last_item_price)): 
                self.items.pop()
        else:
            print("No items to void.")