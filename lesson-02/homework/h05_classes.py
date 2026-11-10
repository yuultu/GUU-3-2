def hw_15():
    class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def peek(self):
            return self.items[-1]

        def is_empty(self):
            return len(self.items) == 0

    return Stack


Stack = hw_15()


def hw_16():
    class Queue:
        def __init__(self):
            self.items = []

        def enqueue(self, item):
            self.items.append(item)

        def dequeue(self):
            return self.items.pop(0)

        def size(self):
            return len(self.items)

    return Queue


Queue = hw_16()


def hw_17():
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

    class Library:
        def __init__(self):
            self.books = []

        def add(self, book):
            self.books.append(book)

        def titles(self):
            return [book.title for book in self.books]

        def by_author(self, author):
            return [
                book.title
                for book in self.books
                if book.author == author
            ]

    return Book, Library


Book, Library = hw_17()
