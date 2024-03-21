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

## Development and DDD Implementation
This project was developed using Python 3.11 and adheres to Domain-Driven Design (DDD) principles, which is a strategy for focusing on the core domain logic of the application. DDD allows for the complex functionalities of high-traffic, intricate systems to be managed through the segregation of domain logic from UI, application logic, and database logic. The codebase is organized into distinct layers that separate concerns and promote a rich domain model.

### DDD Components
#### Entities
Entities are objects defined primarily by their identity, rather than their attributes. In our project, the entities are:

- **Libro (`libro.py`):** Represents a book with a unique identifier (ISBN). This is the key entity in our domain, encapsulating the essence of what a book is in the context of a library.
- **Usuario (`usuario.py`):** Represents a library user, identified uniquely by a user ID. Users are essential for tracking who has borrowed which books.
- **Prestamo (`prestamo.py`):** Represents a loan of a book to a user, uniquely identified by a loan ID. This entity tracks the relationship between a book and a user, including the loan period.

#### Value Objects
Value objects are objects that do not have a conceptual identity. They are defined only by their attributes and are immutable. In this project, we treat data like book titles, user names, or loan dates as value objects. They are critical for defining operations and ensuring integrity in the domain model but are not entities on their own.

#### Aggregates
An aggregate is a cluster of domain objects that can be treated as a single unit. Examples include:

- **Book and Loans Aggregate:** While `Libro` is an entity, it can form an aggregate with `Prestamo` entities, where the `Libro` serves as the aggregate root. This aggregate ensures that all loan operations are consistent with the state of the book (e.g., a book can't be loaned out if it's already on loan).

### Identifying DDD Elements in the Project
- **Entities:** `Libro` (ISBN), `Usuario` (User ID), `Prestamo` (Loan ID).
- **Value Objects:** Attributes like book titles, user names, and dates.
- **Aggregates:** The `Libro` and its `Prestamo`s, where `Libro` acts as the aggregate root.

The use of DDD principles guides the project's structure, ensuring that the system's complexity is well-managed and the domain logic remains the focal point of development.

## Layered Architecture

### Domain Layer
Contains the entities (`Libro`, `Usuario`, `Prestamo`), value objects, and domain services that encapsulate business logic and rules.

- **Libro (libro.py):** Represents a book entity with attributes such as ISBN, title, author, and year.
- **Prestamo (prestamo.py):** Represents a loan entity, tracking the relationship between a book and a user, including loan and return dates.
- **Usuario (usuario.py):** Represents a user entity, including user identification and other relevant attributes.

### Application Layer
Contains services (`BibliotecaService`) that orchestrate the flow between the presentation and domain layers, handling use cases and directing domain objects.

- **BibliotecaService (biblioteca_service.py):** Acts as the application service layer, orchestrating the flow between the domain and infrastructure layers. It contains business logic for adding books, lending books, returning books, and listing both books and loans.

### Infrastructure Layer
Implements persistence for domain objects (`RepositorioLibros`, `RepositorioPrestamos`), abstracting the details of data storage and retrieval.

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

## Development
This project was developed using Python 3.11. It adheres to Domain-Driven Design principles, organizing the codebase into distinct layers that separate concerns and promote a rich domain model.

## Contributors
    Grupo#2:		    ID:		Usuario de GitHub:
    Heydi Garcia Sánchez    1107303		CourantLuna
    Fernando A. Rodriguez   1096552		Farcuto
    Alex Valenzuela         1093917		Alex-GCS
    Diego Rodriguez         1105880		D1egoSebastian
    Axel Baez               1100321		Axell03
    Lisandro jesus          1103763		Lisandro1103763
    Gabriel De La Rosa      1108920     Gabriel7729

