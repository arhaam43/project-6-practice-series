#       20. Creating a Custom Exception

# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Custom exception class
class InvalidAgeError(Exception):
    pass

# Function that uses the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Access granted!")

# Try...except block
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Access denied:", e)