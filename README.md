# Backend Data Pipeline Assessment

## Overview
This project implements a containerized backend data pipeline using FastAPI, Flask, PostgreSQL, SQLAlchemy, and Docker. The system simulates a real-world workflow where customer data is fetched from a mock API, processed by a backend service, and stored in a PostgreSQL database.

## Architecture
Flask Mock Server → FastAPI Pipeline Service → PostgreSQL Database

## Tech Stack
- Python 3.10+
- FastAPI
- Flask
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose

## Project Structure
```
project-root
│
├── docker-compose.yml
├── mock-server
│   ├── app.py
│   └── requirements.txt
│
├── pipeline-service
│   ├── main.py
│   ├── database.py
│   ├── models/customer.py
│   ├── services/ingestion.py
│   └── requirements.txt
│
└── README.md
```

## Setup Instructions

### Clone the Repository
```
git clone https://github.com/yourusername/backend-data-pipeline.git
cd backend-data-pipeline
```

### Run the Project
```
docker compose up --build
```

## Services
- FastAPI Pipeline Service: http://localhost:8000  
- Flask Mock Server: http://localhost:5000  
- PostgreSQL Database: Port 5432  

## API Endpoints

### Ingest Data
POST /api/ingest

### Get Customers
GET /api/customers?page=1&limit=10

### Get Customer by ID
GET /api/customers/{customer_id}

## API Documentation
Swagger UI is available at:
http://localhost:8000/docs

## Author
Swalpita Ray Nayak
