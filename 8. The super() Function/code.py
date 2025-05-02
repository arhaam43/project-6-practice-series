#       8. The super() Function

# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent constructor
        self.subject = subject

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

t1 = Teacher("Miss Rubi", "Geography")
t1.show_info()
# OUTPUTS: 
#    Name: Miss Rubi
#   Subject: Geography
