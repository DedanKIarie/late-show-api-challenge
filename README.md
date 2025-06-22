# Late Show API Challenge

This is a Flask REST API for a Late Night TV show system.

## Setup Instructions

### Clone the repository:
```bash
git clone https://github.com/DedanKIarie/late-show-api-challenge.git
cd late-show-api-challenge
```

### Install dependencies:
It is recommended to use a virtual environment.

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### PostgreSQL Setup:
Log in to your PostgreSQL server and create the database.

```sql
CREATE DATABASE late_show_db;
```

### Environment Variables:
In `server/config.py`, set your database connection string.

```python
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
```

## How to Run

### Database Migrations:
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### Seed the database:
```bash
python server/seed.py
```

### Run the application:
```bash
python server/app.py
```

The application will be running on http://127.0.0.1:5555.

## Authentication Flow

1. **Register a new user:**
   Send a POST request to `/register` with a username and password.

2. **Login:**
   Send a POST request to `/login` with the registered username and password to receive a JWT access token.

3. **Using the token:**
   To access protected routes, include the token in the Authorization header.
   ```
   Authorization: Bearer <your_jwt_token>
   ```

## API Routes

| Method | Route | Auth Required | Description |
|--------|-------|---------------|-------------|
| POST | `/register` | No | Register a new user. |
| POST | `/login` | No | Log in and receive a JWT token. |
| GET | `/episodes` | No | Get a list of all episodes. |
| GET | `/episodes/<int:id>` | No | Get a specific episode and its appearances. |
| DELETE | `/episodes/<int:id>` | Yes | Delete an episode and its related appearances. |
| GET | `/guests` | No | Get a list of all guests. |
| POST | `/appearances` | Yes | Create a new appearance. |

## Sample Request/Response

### POST /register
**Request:**
```json
{
    "username": "testuser",
    "password": "password123"
}
```

**Response:**
```json
{
    "message": "User created successfully"
}
```

### GET /episodes/1
**Response:**
```json
{
    "id": 1,
    "date": "2024-06-20",
    "number": 101,
    "appearances": [
        {
            "id": 1,
            "rating": 5,
            "guest": {
                "id": 1,
                "name": "John Mulaney",
                "occupation": "Comedian"
            }
        }
    ]
}
```

## Postman Usage

1. Import the `challenge-4-lateshow.postman_collection.json` file into Postman.

2. Use the "Register" request to create a user.

3. Use the "Login" request to get an access token.

4. For protected routes like POST `/appearances`, go to the "Authorization" tab, select "Bearer Token" as the type, and paste the access token into the token field.

