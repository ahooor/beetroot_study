# Library

# Write a class structure that implements a library. Classes:

# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class

# Methods:

# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year

# All 3 classes must have a readable __repr__ and __str__ methods.

# Also, the book class should have a class variable which holds the amount of all existing books


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __str__(self):
        return self.name
    

class Book:
    count = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.count += 1
        self.author.books.append(self)

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

    def __str__(self):
        return self.name


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def add_book(self, book):
        self.books.append(book)

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library({self.name})"

    def __str__(self):
        return self.name


author_rowling = Author("J. K. Rowling", "United Kingdom", "31.07.1965")
author_martin = Author("George R. R. Martin", "United States", "20.09.1948")
author_tolkien = Author("J. R. R. Tolkien", "United Kingdom", "03.01.1892")

print(author_rowling.__repr__())
print(author_rowling.__str__())
print("\n")

book_potter1 = Book("Harry Potter & the Philosopher's Stone", 1997, author_rowling)
book_potter2 = Book("Harry Potter & the Chamber of Secrets", 1998, author_rowling)
book_potter3 = Book("Harry Potter & the Prisoner of Azkaban", 1999, author_rowling)
book_asoiaf1 = Book("A Game of Thrones", 1996, author_martin)
book_asoiaf2 = Book("A Clash of Kings", 1999, author_martin)
book_lotr1 = Book("The Fellowship of the Ring", 1954, author_tolkien)
book_lotr2 = Book("The Two Towers", 1954, author_tolkien)

print(book_asoiaf1.__repr__())
print(book_asoiaf1.__str__())
print("\n")

my_library = Library("My library")
my_library.add_book(book_potter1)
my_library.add_book(book_potter2)
my_library.add_book(book_potter3)
my_library.add_book(book_asoiaf1)
my_library.add_book(book_asoiaf2)
my_library.add_book(book_lotr1)
my_library.add_book(book_lotr2)

print(my_library.group_by_author(author_rowling))
print("\n")
print(my_library.group_by_author(author_martin))
print("\n")
print(my_library.group_by_author(author_tolkien))
print("\n")
print(my_library.group_by_year(1997))
print("\n")
print(my_library.group_by_year(1999))
print("\n")

print(my_library.__repr__())
print(my_library.__str__())
print("\n")
