# Dominio (Domain)
class Libro:
    def __init__(self, isbn, titulo, autor, año):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año = año

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

# Capa de Infraestructura de Persistencia
class RepositorioLibros:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def obtener_libro_por_isbn(self, isbn):
        return next((libro for libro in self.libros if libro.isbn == isbn), None)

class RepositorioPrestamos:
    def __init__(self):
        self.prestamos = []

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def obtener_prestamos_por_usuario(self, usuario):
        return [prestamo for prestamo in self.prestamos if prestamo.usuario == usuario]

# Aplicación (Application)
class BibliotecaService:
    def __init__(self, repo_libros, repo_prestamos):
        self.repo_libros = repo_libros
        self.repo_prestamos = repo_prestamos

    def agregar_libro(self, isbn, titulo, autor, año):
        libro = Libro(isbn, titulo, autor, año)
        self.repo_libros.agregar_libro(libro)

    def prestar_libro(self, isbn, usuario, fecha_prestamo, fecha_devolucion):
        libro = self.repo_libros.obtener_libro_por_isbn(isbn)
        if libro:
            prestamo = Prestamo(libro, usuario, fecha_prestamo, fecha_devolucion)
            self.repo_prestamos.agregar_prestamo(prestamo)
        else:
            raise Exception("El libro no está disponible para préstamo.")

    def devolver_libro(self, isbn, usuario):
        prestamos_usuario = self.repo_prestamos.obtener_prestamos_por_usuario(usuario)
        prestamo = next((prestamo for prestamo in prestamos_usuario if prestamo.libro.isbn == isbn), None)
        if prestamo:
            self.repo_prestamos.prestamos.remove(prestamo)
        else:
            raise Exception("No se encontró ningún préstamo para el usuario y libro especificados.")

# Capa de Presentación
class Consola:
    def __init__(self, biblioteca_service):
        self.biblioteca_service = biblioteca_service

    def ejecutar(self):
        self.biblioteca_service.agregar_libro("978-0544003415", "El Hobbit", "J.R.R. Tolkien", 1937)
        self.biblioteca_service.agregar_libro("978-8497597445", "Cien años de soledad", "Gabriel García Márquez", 1967)

        usuario1 = Usuario("Juan Pérez", "juan@example.com")
        usuario2 = Usuario("María Gómez", "maria@example.com")

        self.biblioteca_service.prestar_libro("978-0544003415", usuario1, "2024-03-20", "2024-04-10")
        self.biblioteca_service.prestar_libro("978-8497597445", usuario2, "2024-03-20", "2024-04-10")

        print("Libros disponibles:", [libro.titulo for libro in self.biblioteca_service.repo_libros.libros])
        print("Préstamos:", [(prestamo.libro.titulo, prestamo.usuario.nombre) for prestamo in self.biblioteca_service.repo_prestamos.prestamos])

        self.biblioteca_service.devolver_libro("978-0544003415", usuario1)

        print("Libros disponibles después de la devolución:", [libro.titulo for libro in self.biblioteca_service.repo_libros.libros])
        print("Préstamos después de la devolución:", [(prestamo.libro.titulo, prestamo.usuario.nombre) for prestamo in self.biblioteca_service.repo_prestamos.prestamos])

# Configuración e Inicio
if __name__ == "__main__":
    repo_libros = RepositorioLibros()
    repo_prestamos = RepositorioPrestamos()
    biblioteca_service = BibliotecaService(repo_libros, repo_prestamos)
    consola = Consola(biblioteca_service)
    consola.ejecutar()