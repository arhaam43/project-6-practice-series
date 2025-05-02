# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name      # 'self' stores the name in the object
        self.marks = marks    # 'self' stores the marks in the object

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example: Create a student and display details
student1 = Student("Ali", 90)
student1.display()