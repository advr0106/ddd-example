from datetime import datetime

class EntidadBase:
    def __init__(self):
        self.id = None  # Normalmente, este valor se asignaría automáticamente al guardar en una base de datos
        self.fecha_creacion = datetime.now()
        self.fecha_modificacion = datetime.now()

    # Método para actualizar la fecha de modificación
    def actualizar_fecha_modificacion(self):
        self.fecha_modificacion = datetime.now()