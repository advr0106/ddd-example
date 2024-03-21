from domain.usuario import Usuario
from application.biblioteca_service import BibliotecaService

class Consola:
    def __init__(self, biblioteca_service):
        self.biblioteca_service = biblioteca_service

    def mostrar_menu(self):
        print("---- Menú ----")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Listar libros existentes")
        print("5. Listar libros prestados")
        print("6. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese el número de la opción que desea realizar: ")

            if opcion == "1":
                isbn = input("Ingrese el ISBN del libro: ")
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                año = input("Ingrese el año de publicación del libro: ")
                libro = self.biblioteca_service.agregar_libro(isbn, titulo, autor, año)
                if libro:
                    print(f"Libro '{libro.titulo}' agregado correctamente.")
                else:
                    print("Error: No se pudo agregar el libro.")

            elif opcion == "2":
                isbn = input("Ingrese el ISBN del libro que desea prestar: ")
                usuario_nombre = input("Ingrese su nombre: ")
                usuario_email = input("Ingrese su correo electrónico: ")
                usuario = Usuario(usuario_nombre, usuario_email)
                fecha_prestamo = input("Ingrese la fecha de préstamo (YYYY-MM-DD): ")
                fecha_devolucion = input("Ingrese la fecha de devolución (YYYY-MM-DD): ")
                prestamo = self.biblioteca_service.prestar_libro(isbn, usuario, fecha_prestamo, fecha_devolucion)
                if prestamo:
                    print(f"Libro '{prestamo.libro.titulo}' prestado correctamente a '{prestamo.usuario.nombre}'.")
                else:
                    print("Error: No se pudo realizar el préstamo.")

            elif opcion == "3":
                isbn = input("Ingrese el ISBN del libro que desea devolver: ")
                usuario_nombre = input("Ingrese su nombre: ")
                usuario_email = input("Ingrese su correo electrónico: ")
                usuario = Usuario(usuario_nombre, usuario_email)
                prestamo = self.biblioteca_service.devolver_libro(isbn, usuario)
                if prestamo:
                    print(f"Libro '{prestamo.libro.titulo}' devuelto correctamente por '{prestamo.usuario.nombre}'.")
                else:
                    print("Error: No se pudo realizar la devolución.")

            elif opcion == "4":
                libros = self.biblioteca_service.listar_libros()
                print("Libros existentes:")
                for libro in libros:
                    print(f"ISBN: {libro.isbn}, Título: {libro.titulo}, Autor: {libro.autor}, Año: {libro.año}")

            elif opcion == "5":
                prestamos = self.biblioteca_service.listar_prestamos()
                print("Libros prestados:")
                for  prestamo in prestamos:
                    print(f"Libro: {prestamo.libro.titulo}, Usuario: {prestamo.usuario.nombre}, Fecha de préstamo: {prestamo.fecha_prestamo}, Fecha de devolución: {prestamo.fecha_devolucion}")

            elif opcion == "6":
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")