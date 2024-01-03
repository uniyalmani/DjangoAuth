# Django Authentication Project

This project provides a Django-based authentication system with user signup, login, logout, and profile functionality.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Routes](#routes)


## Features

- User signup
- User login
- User logout
- User profile
- JWT-based authentication

## Tech Stack

- **Backend:**
  - [Django](https://www.djangoproject.com/): A high-level Python web framework that encourages rapid development and clean, pragmatic design.
  - [Django REST framework](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs in Django.

- **Frontend:**
  - HTML, CSS, JavaScript: Basic web technologies for the frontend.
  - [Django Templates](https://docs.djangoproject.com/en/3.2/topics/templates/): Django's templating engine for rendering dynamic content on the server-side.

- **Authentication:**
  - [JWT (JSON Web Tokens)](https://jwt.io/): A standard method for representing claims securely between two parties.

- **Database:**
  - SQLite (default database in Django, suitable for development).

- **Containerization:**
  - [Docker](https://www.docker.com/): A platform for developing, shipping, and running applications in containers.

- **Dependency Management:**
  - [pip](https://pip.pypa.io/en/stable/): The package installer for Python.


## Requirements

- Python 3.x
- Django
- Django REST framework
- djangorestframework-simplejwt
- Other dependencies (specified in requirements.txt)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Build and run the Docker containers: :

   ```bash
   docker-compose up

   ```

## Routes

  - Signup: `/auth/signup/`
  - Login: `/auth/login/`
  - Logout: `/auth/logout/`
  - Home: `/auth/home/`
  - Profile: `/auth/profile/`



