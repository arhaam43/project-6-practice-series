#       14. Aggregation

# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# Employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def show_employee(self):
        print(f"Employee: {self.name}")

# Department class (aggregation)
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # aggregation: employee object passed in

    def show_department(self):
        print(f"Department: {self.dept_name}")
        self.employee.show_employee()  # using employee object inside department

# Independent employee object
emp1 = Employee("Ahmed")

# Department object — employee's reference pass
dept1 = Department("IT", emp1)

# Show department info
dept1.show_department()
