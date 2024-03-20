from domain.libro import Libro
class RepositorioLibros:
    def __init__(self):
        self.libros = [
            Libro("978-0544003415", "El Hobbit", "J.R.R. Tolkien", 1937),
            Libro("978-8497597445", "Cien años de soledad", "Gabriel García Márquez", 1967),
            Libro("978-0307392817", "1984", "George Orwell", 1949)
        ]

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def obtener_libro_por_isbn(self, isbn):
        return next((libro for libro in self.libros if libro.isbn == isbn), None)

    def listar_libros(self):
        return self.libros