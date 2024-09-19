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

User Registration and Authentication
1. Register
Endpoint: /api/accounts/register/
Method: POST
Body:
json
{
    "username": "your_username",
    "password": "your_password",
    "email": "your_email@example.com"
}

2. Login
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