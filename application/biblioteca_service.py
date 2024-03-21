from domain.libro import Libro
from domain.prestamo import Prestamo

class BibliotecaService:
    
    def __init__(self, repo_libros, repo_prestamos):
        
        self.repo_libros = repo_libros
        self.repo_prestamos = repo_prestamos
    
    def agregar_libro(self, isbn, titulo, autor, año):
        
        libro = Libro(isbn,titulo,autor,año)
        self.repo_libros.agregar_libro(libro)
        
        return libro
    
    def prestar_libro(self,isbn, usuario,fecha_prestamo,fecha_devolucion):
        
        libro = self.repo_libros.obtener_libro_por_isbn(isbn)
        
        if libro:
            prestamo = Prestamo(libro,usuario,fecha_prestamo,fecha_devolucion)
            self.repo_prestamos.agregar_prestamo(prestamo)
            
            return prestamo
        
        else:
        
            return None
    def decolver_libro(self, isdn, usuario):
        prestamo_usuario = self.repo_prestamos.obtener_prestamos_por_usuario(usuario)
        prestamo = next((prestamo for prestamo in prestamo_usuario if prestamo.libro.isbn == isbn), None)
        if prestamo:
            self.repo_prestamo.prestamo.remove(prestamo)
            return prestamo
        else:
            return None
    def lista_libros(self):
        return self.repo_libros.listar_libros()
    def listar_prestamo(self):
        return self.repo_prestamos.listar_prestamos()
