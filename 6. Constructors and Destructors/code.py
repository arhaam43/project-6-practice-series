# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("📥 Logger object has been created.")

    def __del__(self):
        print("🗑️ Logger object has been destroyed.")

#To create object:
log1 = Logger()  # Output: 📥 Logger object has been created.

# To trigger the destructor:
del log1  # Output: 🗑️ Logger object has been destroyed.