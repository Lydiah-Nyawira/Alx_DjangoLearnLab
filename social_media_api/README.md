# Social Media API

## Setup

1. Install dependencies:
   ```bash
   pip install django djangorestframework

Run migrations:
bash
python manage.py migrate

Start the server:
bash
python manage.py runserver

2. User Registration and Authentication
Register
Endpoint: /api/accounts/register/
Method: POST
Body:
json
{
    "username": "your_username",
    "password": "your_password",
    "email": "your_email@example.com"
}

Login
Endpoint: /api/accounts/login/
Method: POST
Body:
json
{
    "username": "your_username",
    "password": "your_password"
}
Response:
json
{
    "token": "your_auth_token"
}

## Posts app API
This is a Django-based RESTful API for managing posts and comments in a social media application. Users can create, view, update, and delete posts and comments.

## Base URL
http://127.0.0.1:8000/api/

php

## Authentication
All endpoints require authentication. Use a token-based authentication method (e.g., JWT or session authentication) to access the API.

## Endpoints

### 1. Posts

#### 1.1 List Posts
- **Method**: `GET`
- **Endpoint**: `/posts/`
- **Description**: Retrieve a list of all posts.

**Response**:
```json
{
    "count": 100,
    "next": "http://127.0.0.1:8000/api/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "First Post",
            "content": "This is the content of the first post.",
            "author": 1,
            "created_at": "2023-09-19T12:00:00Z",
            "updated_at": "2023-09-19T12:00:00Z"
        },
        ...
    ]
}
1.2 Create Post
Method: POST
Endpoint: /posts/
Description: Create a new post.
Request Body:

json
{
    "title": "New Post Title",
    "content": "This is the content of the new post."
}
Response:

json
{
    "id": 101,
    "title": "New Post Title",
    "content": "This is the content of the new post.",
    "author": 1,
    "created_at": "2023-09-19T12:00:00Z",
    "updated_at": "2023-09-19T12:00:00Z"
}
1.3 Retrieve a Post
Method: GET
Endpoint: /posts/{id}/
Description: Retrieve a specific post by ID.
Response:

json
{
    "id": 1,
    "title": "First Post",
    "content": "This is the content of the first post.",
    "author": 1,
    "created_at": "2023-09-19T12:00:00Z",
    "updated_at": "2023-09-19T12:00:00Z"
}
1.4 Update a Post
Method: PUT
Endpoint: /posts/{id}/
Description: Update a specific post by ID.
Request Body:

json
{
    "title": "Updated Post Title",
    "content": "This is the updated content."
}
Response:

json
Copy code
{
    "id": 1,
    "title": "Updated Post Title",
    "content": "This is the updated content.",
    "author": 1,
    "created_at": "2023-09-19T12:00:00Z",
    "updated_at": "2023-09-19T12:05:00Z"
}
1.5 Delete a Post
Method: DELETE
Endpoint: /posts/{id}/
Description: Delete a specific post by ID.
Response:

json
{
    "detail": "Post deleted successfully."
}
2. Comments
2.1 List Comments
Method: GET
Endpoint: /comments/
Description: Retrieve a list of all comments.
Response:

json
{
    "count": 50,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "post": 1,
            "author": 1,
            "content": "This is a comment.",
            "created_at": "2023-09-19T12:00:00Z",
            "updated_at": "2023-09-19T12:00:00Z"
        },
        ...
    ]
}
2.2 Create Comment
Method: POST
Endpoint: /comments/
Description: Create a new comment.
Request Body:

json
{
    "post": 1,
    "content": "This is a new comment."
}
Response:

json
{
    "id": 101,
    "post": 1,
    "author": 1,
    "content": "This is a new comment.",
    "created_at": "2023-09-19T12:00:00Z",
    "updated_at": "2023-09-19T12:00:00Z"
}
2.3 Retrieve a Comment
Method: GET
Endpoint: /comments/{id}/
Description: Retrieve a specific comment by ID.
Response:

json
{
    "id": 1,
    "post": 1,
    "author": 1,
    "content": "This is a comment.",
    "created_at": "2023-09-19T12:00:00Z",
    "updated_at": "2023-09-19T12:00:00Z"
}
2.4 Update a Comment
Method: PUT
Endpoint: /comments/{id}/
Description: Update a specific comment by ID.
Request Body:

json
{
    "content": "This is the updated comment."
}
Response:

json
{
    "id": 1,
    "post": 1,
    "author": 1,
    "content": "This is the updated comment.",
    "created_at": "2023-09-19T12:00:00Z",
    "updated_at": "2023-09-19T12:05:00Z"
}
2.5 Delete a Comment
Method: DELETE
Endpoint: /comments/{id}/
Description: Delete a specific comment by ID.
Response:

json
Copy code
{
    "detail": "Comment deleted successfully."
}