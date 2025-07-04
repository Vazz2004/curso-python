import limpiar_consola


limpiar_consola.limpiarConsola

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True 

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro '{self.title}' ha sido prestado")
        else:
            print("El libro no está disponible para préstamo")

    def return_book(self):  # nombre corregido
        self.available = True
        print(f"El libro '{self.title}' ha sido devuelto")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_books(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro '{book.title}' no está disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)  # nombre corregido
        else:
            print("Este libro no está en la lista de préstamos")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro '{book.title}' ha sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario '{user.name}' ha sido registrado")

    def show_available_books(self):
        print("Los libros disponibles son:")
        for book in self.books:
            if book.available:
                print(f"{book.title}, {book.author}")


# Crear libros
book1 = Book("El Principito", "Antoine de Saint-Exupéry")
book2 = Book("1984", "George Orwell")

# Crear usuario
user1 = User('Samuel', '001')

# Crear biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

# Prueba de préstamo y devolución
user1.borrow_books(book1)
user1.return_book(book1)
library.show_available_books()


#mostar libros 
library.show_available_books()


#realizar un prestamo

user1.borrow_books(book1)


#mostar libros 
library.show_available_books()

#delvolver los libros 
user1.return_book(book1)


#mostar libros 
library.show_available_books()
