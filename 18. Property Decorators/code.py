#       18. Property Decorators: @property, @setter, and @deleter

# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Invalid price! Must be non-negative.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

p1 = Product(100)

print(p1.price)     # Output: 100

p1.price = 150
print(p1.price)     # Output: 150

p1.price = -50      # Output: Invalid price!

del p1.price        # Output: Deleting price...