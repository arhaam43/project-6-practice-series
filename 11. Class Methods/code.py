# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count() 

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

b1 = Book("Python Basics by Ameen Alam")
b2 = Book("Data Science AI-102")
b3 = Book("Giaic, Book of Codes")

print("Total books added:", Book.total_books)
# Output: Total books added: 3