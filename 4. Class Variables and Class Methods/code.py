# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    # Class variable
    bank_name = "Old Bank"

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    # Method to show current bank name (optional, for clarity)
    def show_bank_name(self):
        print(f"Bank Name: {self.bank_name}")

# Create two objects
acc1 = Bank()
acc2 = Bank()

# Show bank name before changing
acc1.show_bank_name()  # Output: Old Bank
acc2.show_bank_name()  # Output: Old Bank

# Change bank name using class method
Bank.change_bank_name("New Era Bank")

# Show bank name after changing
acc1.show_bank_name()  # Output: New Era Bank
acc2.show_bank_name()  # Output: New Era Bank
