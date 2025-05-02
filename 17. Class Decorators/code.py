#       17. Class Decorators

# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# Step 1: Create class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Method add kar diya class ke andar
    return cls

# Step 2: Apply decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Ali")
print(p1.greet())  # Output: Hello from Decorator!