#   10. Instance Methods

# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance variable
        self.breed = breed    # instance variable

    def bark(self):
        print(f"{self.name} is barking! 🐶")

dog1 = Dog("Rocky", "Labrador")
dog1.bark()  # Output: Rocky is barking! 🐶

dog2 = Dog("Bella", "Poodle")
dog2.bark()  # Output: Bella is barking! 🐶