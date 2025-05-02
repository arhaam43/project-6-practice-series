#       9. callable() and __call__()

# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Factor set ho raha hai constructor mein

    def __call__(self, value):
        return self.factor * value  # Jab object call hoga, multiply karega

# Step 1: Object banao
times3 = Multiplier(3)

# Step 2: Check if object is callable
print(callable(times3))  # Output: True

# Step 3: Object ko function ki tarah call karo
result = times3(5)
print(result)  # Output: 15 (3 * 5)
