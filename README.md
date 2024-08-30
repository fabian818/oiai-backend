# oiai-backend

**oiai-backend** is a backend simple ping server service built with FastAPI, designed for performance, scalability, and maintainability. It uses containerization with Docker and deployment orchestration via Helm for Kubernetes environments.


Available on http://api.oiai.thisguydeploys.com/

## Features

- **FastAPI Framework**: Provides a high-performance, modern web framework for building APIs.
- **Asynchronous Design**: Handles a high volume of concurrent requests efficiently.
- **Containerization**: Docker support for consistent and portable development environments.
- **Database Migrations**: Managed using Alembic to handle schema changes effectively.
- **CI/CD Integration**: Automated workflows for continuous integration and deployment using GitHub Actions.
- **Kubernetes Deployment**: Helm charts provided for easy Kubernetes deployment.

## Project Structure

```plaintext
.
├── __init__.py
├── alembic                   # Alembic directory for database migrations
│   ├── README
│   ├── __init__.py
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── 99bde30f69cd_created_texts_table.py
├── alembic.ini               # Alembic configuration file
├── app                       # Core application directory
│   ├── __init__.py
│   ├── crud.py               # CRUD operations for the application
│   ├── database.py           # Database connection and setup
│   ├── main.py               # Entry point for FastAPI application
│   └── models.py             # Database models
├── charts                    # Helm charts for Kubernetes deployment
│   └── api
│       ├── Chart.yaml        # IMPORTANT I'm using a librarychart in the Chart dependencies, it provides me DRY code in the helm chart.
│       ├── templates
│       │   └── api.yaml
│       └── values.yaml
├── docker                    # Additional Docker configuration
│   └── app
│       └── Dockerfile
└── requirements.txt          # Python dependencies

```
# Getting Started
## Prerequisites
- Docker: Required for containerization.
- Python 3.9+: The backend service is built using Python 3.9 or later.
- Helm: Required for managing Kubernetes deployments.

# Running Locally
## Clone the repository:

``` bash
git clone https://github.com/fabian818/oiai-backend.git
cd oiai-backend
``` 
## Build and run the Docker container:


``` bash
docker build -t oiai-backend .
docker run -p 8000:8000 oiai-backend
``` 

# Database Migrations
Alembic is used for managing database migrations. Follow the steps below to handle database schema changes:

## Generate a new migration script:

``` bash
alembic revision --autogenerate -m "describe your changes here"
``` 

Apply migrations to the database:

``` bash
alembic upgrade head
``` 

## Rollback the last migration:

``` bash
alembic downgrade -1
``` 
- Make sure the correct database URL is set in alembic.ini or the environment variables.

## CI/CD Pipeline

The CI/CD pipeline uses GitHub Actions for automating the build and deployment processes:

- Docker Push Workflow: On each push to the main branch, the Docker image is built and pushed to the container registry.
- Helm Push Workflow: Helm charts are packaged and pushed to the Helm repository for Kubernetes deployments.
