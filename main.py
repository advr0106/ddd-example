from domain.usuario import Usuario
from infrastructure.repositorio_libros import RepositorioLibros
from infrastructure.repositorio_prestamos import RepositorioPrestamos
from application.biblioteca_service import BibliotecaService
from presentation.consola import Consola

if __name__ == "__main__":
    repo_libros = RepositorioLibros()
    repo_prestamos = RepositorioPrestamos()
    biblioteca_service = BibliotecaService(repo_libros, repo_prestamos)
    consola = Consola(biblioteca_service)
    consola.ejecutar()