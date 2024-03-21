# suponiendo que el archivo se llama repositorio_usuarios.py

from domain.usuario import Usuario

class RepositorioUsuarios:
    def __init__(self):
        self.usuarios = [
            Usuario("Juan Pérez", "juan@example.com"),
            Usuario("María Gómez", "maria@example.com")
        ]

    def agregar_usuario(self, usuario):
        """Agrega un nuevo usuario a la lista de usuarios."""
        self.usuarios.append(usuario)

    def obtener_usuario_por_email(self, email):
        """Busca y devuelve un usuario por su email, si no lo encuentra devuelve None."""
        return next((usuario for usuario in self.usuarios if usuario.email == email), None)

    def obtener_usuarios_por_nombre(self, nombre):
        """Devuelve una lista de usuarios que coinciden con el nombre dado."""
        return [usuario for usuario in self.usuarios if usuario.nombre == nombre]

    def listar_usuarios(self):
        """Devuelve la lista de todos los usuarios."""
        return self.usuarios
