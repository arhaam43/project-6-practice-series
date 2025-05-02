#               7. Access Modifiers: Public, Private, and Protected

# Assignment:

# Create a class Employee with:
#    a public variable name,
#    a protected variable _salary, and
#    a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public
        self._salary = salary   # Protected (by convention)
        self.__ssn = ssn        # Private

# Create an object
emp = Employee("Ali", 50000, "321-54-9876")

# Accessing public variable
print("Name:", emp.name)  # ✅ Works fine

# Accessing protected variable
print("Salary:", emp._salary)  # ⚠️ Works, but not recommended (intended for internal use)

# Accessing private variable
print("SSN:", emp.__ssn)  # ❌ Error: AttributeError