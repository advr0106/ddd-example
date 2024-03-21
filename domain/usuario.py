from entidad_base import EntidadBase

class Usuario(EntidadBase):
    def __init__(self, nombre, email):
        super().__init__()
        self.nombre = nombre
        self.email = email