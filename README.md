# Task Manager API

A RESTful Task Manager backend built with **Python, FastAPI, and PostgreSQL**.
The project implements CRUD operations for tasks, user registration and login, password hashing, JWT-based authentication, user-specific task authorization, PostgreSQL connection pooling, layered architecture, and API error handling.

## Features

- User registration
- Secure password hashing with `pwdlib`
- User login
- JWT authentication
- Bearer token authentication with FastAPI OAuth2 utilities
- JWT expiration
- Protected task endpoints
- User-specific task ownership
- Create, read, update, and delete tasks
- PostgreSQL database
- PostgreSQL connection pooling with `psycopg_pool`
- Service and data/repository layers
- HTTP error handling
- Environment variables for secrets
- Interactive API documentation with Swagger UI

## Tech Stack

- **Python**
- **FastAPI**
- **PostgreSQL**
- **psycopg**
- **psycopg\_pool**
- **PyJWT**
- **pwdlib**
- **python-dotenv**
- **Uvicorn**

## Project Structure

```
TaskManager/
├── main.py
├── models/
│   ├── task.py
│   └── users.py
├── routers/
│   ├── tasks.py
│   ├── users.py
│   └── auth.py
├── services/
│   ├── taskService.py
│   └── userService.py
└── data/
    ├── task.py
    ├── user.py
    └── connection_pool.py
```

## Architecture

The application follows a layered structure:

```
Client
  ↓
Router
  ↓
Service
  ↓
Data / Repository
  ↓
PostgreSQL
```

Authentication is handled through a JWT dependency:

```
Login
  ↓
Verify credentials
  ↓
Create JWT
  ↓
Client sends Bearer token
  ↓
OAuth2PasswordBearer extracts token
  ↓
JWT is decoded and validated
  ↓
User is retrieved from database
  ↓
Protected endpoint
```

## Database

The project uses PostgreSQL with two main tables:

### Users

```
id
username
hashed_password
```

### Tasks

```
id
title
completed
user_id
```

`user_id` associates each task with its owner.
Task queries use the authenticated user's ID, preventing one user from accessing or modifying another user's tasks.

## Authentication

After a successful login, the API returns:

```
{
  "access_token": "<JWT>",
  "token_type": "bearer"
}
```

The token is sent with protected requests using:

```
Authorization: Bearer <JWT>
```

The JWT contains the user's ID in the `sub` claim and an expiration time.

## Environment Variables

Sensitive configuration is stored outside the source code.
Example `.env`:

```
SECRET_KEY=your-secret-key
```

The `.env` file should **not** be committed to Git.
Example `.gitignore`:

```
.env
.venv/
venv/
__pycache__/
```

## Running the Project

### 1. Create and activate a virtual environment

Windows PowerShell:

```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```
pip install fastapi uvicorn psycopg[binary] psycopg[pool] PyJWT pwdlib python-dotenv
```

### 3. Configure PostgreSQL

Create a PostgreSQL database named:

```
task_manager
```

Create the required `users` and `tasks` tables, including the foreign-key relationship between `tasks.user_id` and `users.id`.

### 4. Configure environment variables

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key
```

Configure the PostgreSQL connection details in the application's connection-pool configuration.

### 5. Start the server

```
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive documentation.
Swagger UI:

```
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation:

```
http://127.0.0.1:8000/redoc
```

## Main Endpoints

### Authentication

| MethodEndpointDescription |             |                                |
| ------------------------- | ----------- | ------------------------------ |
| POST                      | `/register` | Register a new user            |
| POST                      | `/login`    | Authenticate and receive a JWT |

### Tasks

| MethodEndpointDescription |               |                                    |
| ------------------------- | ------------- | ---------------------------------- |
| POST                      | `/tasks`      | Create a task                      |
| GET                       | `/tasks`      | Get the authenticated user's tasks |
| GET                       | `/tasks/{id}` | Get one of the user's tasks        |
| PUT                       | `/tasks/{id}` | Update one of the user's tasks     |
| DELETE                    | `/tasks/{id}` | Delete one of the user's tasks     |

Task endpoints require a valid Bearer token.

## Authorization

Authentication answers:

> Who is the user?

Authorization answers:

> Is this user allowed to access this task?

For example, task queries include the authenticated user's ID:

```
WHERE id = %s AND user_id = %s
```

This ensures that knowing another task's ID is not enough to access it.

## Connection Pooling

The application creates a shared PostgreSQL connection pool and obtains connections from it when database operations are performed.

```
Request
  ↓
Get connection from pool
  ↓
Execute query
  ↓
Return connection to pool
```

This avoids creating a new database connection for every request and allows connections to be reused.

## Error Handling

The API handles common failures such as:

- Invalid credentials
- Invalid JWTs
- Missing JWT claims
- Nonexistent users
- Invalid or inaccessible task IDs
- Unauthorized access to another user's tasks

Authentication failures return `401 Unauthorized`, while inaccessible/nonexistent tasks are handled by the task endpoints.

## Learning Goals

This project was built to practice backend development concepts including:

- REST API design
- FastAPI
- PostgreSQL
- SQL queries
- Connection pooling
- Authentication
- Authorization
- JWT
- Password hashing
- Dependency injection
- Layered architecture
- Error handling
- Environment-based configuration

## Future Improvements

Possible future improvements include:

- Automated tests with `pytest`
- Database migrations
- More extensive request validation
- Refresh tokens
- Rate limiting
- Dockerization
- CI/CD
- Production deployment
- Improved logging and monitoring

## License

This project is for learning and educational purposes.
