from entidad_base import EntidadBase

class Libro(EntidadBase):
    def __init__(self, isbn, titulo, autor, año):
        super().__init__()  # Llama al inicializador de la clase base para establecer ID y fechas
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año = año