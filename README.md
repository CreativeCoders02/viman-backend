

# Viman Backend API 📂

This repository contains the **Django backend API** for the **Viman** project. It handles the backend functionalities of the Viman cloakroom management platform, including user authentication, file (proof image) handling, and data management.

## Features

- **User Management**: Handles user registration, login, and authentication for secure access.
- **File Handling**: Manages proof images for item verification within the cloakroom system.
- **Authentication**: Ensures secure interactions and restricted access through token-based authentication.
- **API Endpoints**: Provides structured and RESTful API endpoints to support the frontend app.

## Installation

### Prerequisites

- **Python 3.x**
- **Django** and **Django Rest Framework (DRF)**
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Setting Up

1. Clone the repository:
   ```bash
   git clone https://github.com/sarfarajansari/viman-backend.git
   cd viman-backend
   ```

2. Configure the environment variables and database settings as needed.

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the Django server:
   ```bash
   python manage.py runserver
   ```
   The API server will run at `http://localhost:8000`.

## Endpoints Overview

- **Authentication**: `/api/auth/`
- **User Management**: `/api/users/`
- **Proof Image Upload**: `/api/upload-proof/`
- **Request Management**: `/api/requests/`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
