class Container:
 
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def displayContainers(self):
        print("Container:",self.name)
        print("Price:",self.price)

    def transaction(self, price, amount):
        if amount < self.price:
            print("Insufficient Payment!")

            self.displayContainers()
            change = amount - self.price
            print("Change: P" + str(change))
            self.displayChange(change)

    def displayChange(self, change):
        denominations = [20, 10, 5, 1]
        remaining = change
        for denom in denominations:
            count = remaining // denom
            remaining -= count * denom
            print(f"P{denom}: {count}")