class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.library = []
    def get_books(self):
        return self.library
    def add_book(self, book):
        self.library.append(book)
    def search_books(self, title = None, author = None):
        matches = []
        for book in self.library:
            if title:
                if title in book.title.lower():
                    matches.append(book)
                if title in book.title:
                    matches.append(book)
            if author:
                if author.name in book.author.name.lower():
                    matches.append(book)
                if author.name in book.author.name:
                    matches.append(book)
        return matches
            

class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.library = []
    def get_books(self):
        return self.library

class Book(object):
    def __init__(self, title, author = None):
        self.title = title
        if author:
            self.author = author
            author.library.append(self)
        