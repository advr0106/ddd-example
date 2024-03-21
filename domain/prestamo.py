from domain.entidad_base import EntidadBase

class Prestamo(EntidadBase):
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        super().__init__()
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion