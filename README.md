# Library Management System With DDD (Domain-Driven Design)

This project is a Library Management System developed using Python and following Domain-Driven Design (DDD) principles. It is designed to manage book lending and returns, keeping track of books and users in a library setting. 

## Project Structure
Below is the project's directory structure:

    │ main.py
    │ README.md
    │
    ├───application
    │ │ biblioteca_service.py
    │
    ├───domain
    │ │ libro.py
    │ │ prestamo.py
    │ │ usuario.py
    │
    ├───infrastructure
    │ │ repositorio_libros.py
    │ │ repositorio_prestamos.py
    │
    ├───presentation
    │ │consola.py

## Components

### Domain Layer
- **Libro (libro.py):** Represents a book entity with attributes such as ISBN, title, author, and year.
- **Prestamo (prestamo.py):** Represents a loan entity, tracking the relationship between a book and a user, including loan and return dates.
- **Usuario (usuario.py):** Represents a user entity, including user identification and other relevant attributes.

### Application Layer
- **BibliotecaService (biblioteca_service.py):** Acts as the application service layer, orchestrating the flow between the domain and infrastructure layers. It contains business logic for adding books, lending books, returning books, and listing both books and loans.

### Infrastructure Layer
- **RepositorioLibros (repositorio_libros.py):** Implements the repository pattern for books, providing CRUD operations for book entities.
- **RepositorioPrestamos (repositorio_prestamos.py):** Implements the repository pattern for loans, providing CRUD operations for loan entities.


### Presentation Layer
- **Consola (consola.py):** Provides a console-based user interface for interacting with the library system, including actions like searching for books, checking out books, and returning books.

## Getting Started
To run this project, ensure you have Python installed on your system. Clone the repository, navigate to the project directory, and run:

```bash
python main.py
```

This will start the console-based application, where you can interact with the library management system.

