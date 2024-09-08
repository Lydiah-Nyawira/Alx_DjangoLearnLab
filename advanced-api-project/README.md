# Advanced API Project

This project demonstrates advanced API development using Django and Django REST Framework (DRF). It includes setting up a Django project, creating custom serializers, building custom and generic views, implementing advanced query capabilities, and writing comprehensive unit tests.

## Learning Objectives

1. **Set Up a New Django Project**: Initiate a Django project and configure it for advanced API development using custom serializers to handle complex data structures.
2. **Build Custom and Generic Views**: Develop custom views and utilize DRF’s generic views to manage CRUD operations and streamline API functionality.
3. **Implement Filtering, Searching, and Ordering**: Enhance API usability with filtering, searching, and ordering capabilities.
4. **Write Unit Tests**: Create unit tests to ensure the reliability and correctness of your API endpoints.

## Project Structure

- **Project Setup**: 
  - Install Django and DRF.
  - Create a directory ('advanced-api-project')
  - In the directory create a Django project (`advanced_api_project`) and app (`api`).
  - Configure models and serializers.
  
- **Models**:
  - **Author**: `name` (string)
  - **Book**: `title` (string), `publication_year` (integer), `author` (ForeignKey to Author)
  
- **Serializers**:
  - `BookSerializer`: Serializes `Book` model fields.
  - `AuthorSerializer`: Serializes `Author` model fields and includes nested `BookSerializer`.

- **Views**:
  - **Custom Views**: Implement generic views for CRUD operations on the `Book` model.
  - **Permissions**: Apply DRF’s permission classes to secure endpoints.

- **Filtering, Searching, Ordering**:
  - Use DRF’s `DjangoFilterBackend`, `SearchFilter`, and `OrderingFilter` to enhance query capabilities.

- **Unit Testing**:
  - Write tests for CRUD operations, filtering, searching, ordering, and permissions.

## Installation and Setup

1. **Install Dependencies**:
   ```bash
   pip install django djangorestframework

## API Endpoints

### Books

- `GET /books/`: Retrieve a list of all books.
- `POST /books/create/`: Create a new book (authentication required).
- `GET /books/<id>/`: Retrieve a specific book by ID.
- `PUT /books/<id>/update/`: Update a specific book by ID (authentication required).
- `DELETE /books/<id>/delete/`: Delete a specific book by ID (authentication required).

- **List Books**
  - **URL**: `/books/`
  - **Method**: `GET`
  - **Query Parameters**:
    - `title` (string): Filter books by title (case-insensitive).
    - `author` (string): Filter books by author (case-insensitive).
    - `publication_year` (integer): Filter books by publication year.
    - `search` (string): Search books by title or author.
    - `ordering` (string): Order results by field (e.g., `title`, `publication_year`).

**Examples**:

- **Filter by Title**: `/books/?title=SomeTitle`
- **Search by Author**: `/books/?search=SomeAuthor`
- **Order by Publication Year**: `/books/?ordering=publication_year`

**Permissions:**
- `GET /books/` and `GET /books/<id>/` are publicly accessible.
- `POST /books/create/`, `PUT /books/<id>/update/`, and `DELETE /books/<id>/delete/` require authentication.