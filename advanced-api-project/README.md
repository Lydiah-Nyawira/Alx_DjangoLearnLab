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

- **List Books**
  - **URL**: `/books/`
  - **Method**: `GET`
  - **Permissions**: Public
  - **Description**: Retrieves a list of all books in the system.


- **Create Book**
  - **URL**: `/books/`
  - **Method**: `POST`
  - **Permissions**: Public
  - **Description**: Creates a new book record. Requires title, publication_year, and author fields in the request body.


- **Retrieve Book**
  - **URL**: `/books/<int:pk>/`
  - **Method**: `GET`
  - **Permissions**: Authenticated
  - **Description**: Retrieves the details of a specific book identified by its primary key (pk).


- **Update Book**
  - **URL**: `/books/<int:pk>/`
  - **Method**: `PUT`
  - **Permissions**: Authenticated
  - **Description**: Updates the details of a specific book. Requires title, publication_year, and author fields in the request body.

- **Delete Book**
  - **URL**: `/books/<int:pk>/`
  - **Method**: `DELETE`
  - **Permissions**: Authenticated
  - **Description**: Deletes the specified book identified by its primary key (pk).
