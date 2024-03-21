from domain.libro import Libro
from domain.usuario import Usuario
from domain.prestamo import Prestamo
class RepositorioPrestamos:
    def __init__(self):
        libro1 = Libro("978-0544003415", "El Hobbit", "J.R.R. Tolkien", 1937)
        libro2 = Libro("978-8497597445", "Cien años de soledad", "Gabriel García Márquez", 1967)
        usuario1 = Usuario("Juan Pérez", "juan@example.com")
        usuario2 = Usuario("María Gómez", "maria@example.com")
        self.prestamos = [
            Prestamo(libro1, usuario1, "2024-03-20", "2024-04-10"),
            Prestamo(libro2, usuario2, "2024-03-20", "2024-04-10")
        ]

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def obtener_prestamos_por_usuario(self, usuario_email):
        return [prestamo for prestamo in self.prestamos if prestamo.usuario.email == usuario_email]

    def listar_prestamos(self):
        return self.prestamos