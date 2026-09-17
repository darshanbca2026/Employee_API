# Employee Management API

![Python](https://img.shields.io/badge/Python-3.11-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/b-darshan-a628192ba)

A secure and scalable RESTful API for Employee Management with JWT authentication, built using FastAPI and PostgreSQL.

**Live API:** https://employee-api-93no.onrender.com 
**Swagger Docs:** https://employee-api-93no.onrender.com/docs

### Features
- JWT based Authentication and Authorization
- User Registration and Login
- Complete Employee CRUD Operations
- PostgreSQL with SQLAlchemy ORM
- Password Hashing with Bcrypt

### API Endpoints
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | /register | Register a new user | No |
| POST | /login | Login and get access token | No |
| GET | /employees | Get all employees | Yes |
| POST | /employees | Create a new employee | Yes |
| GET | /employees/{id} | Get employee by ID | Yes |
| PUT | /employees/{id} | Update employee details | Yes |
| DELETE | /employees/{id} | Delete employee | Yes |

### Getting Started
1. Clone the repository
```bash
git clone https://github.com/darshanbca2026/Employee_-API.git
cd Employee_-API
Author
Darshan B - BCA 2026 | GitHub: @darshanbca2026 | LinkedIn: https://www.linkedin.com/in/b-darshan-a628192ba
