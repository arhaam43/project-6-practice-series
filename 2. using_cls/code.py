# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    # Class variable to keep track of the number of instances created
    count = 0

    def __init__(self):
        # Increment the counter every time a new object is created
        Counter.count += 1

    @classmethod
    def show_count(cls):
        # Display the current count of created objects
        print(f"Total objects created: {cls.count}")

# Example usage:
a = Counter()  # First object
b = Counter()  # Second object
c = Counter()  # Third object

# Call the class method to show the current count
Counter.show_count()  # Output: Total objects created: 3
