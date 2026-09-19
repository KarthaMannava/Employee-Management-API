<<<<<<< HEAD
# 📘 Employee Management System (CRUD)
## Streamlit • FastAPI • PostgreSQL • Docker

<img width="1536" height="1024" alt="crud diagram" src="https://github.com/user-attachments/assets/a7d9c23b-88f5-49a1-86f2-b6d1b140e468" />

---

## 📌 Overview
This project is a full-stack CRUD (Create, Read, Update, Delete) employee management system built with Python, Streamlit, FastAPI, and PostgreSQL.
It demonstrates real-world backend API design, database integration, and containerized infrastructure using Docker.

---

## 🧱 Architecture & Flow
```
User
 └── Streamlit (Frontend UI)
        └── FastAPI (REST Backend)
               └── PostgreSQL (Dockerized Database)
```

<img width="1536" height="1024" alt="crud flow pic" src="https://github.com/user-attachments/assets/3748a60b-9c01-4279-ad55-b4d329484ae4" />

---

## 🚀 Features
Add, view, update, and delete employee records
RESTful API built with FastAPI
Interactive frontend built with Streamlit
PostgreSQL database running in Docker
SQLAlchemy ORM for database modeling
Environment-based configuration
Swagger UI for API testing

---

## 🛠️ Tech Stack
Layer	            Technology
Frontend	        Streamlit
Backend	            FastAPI
ORM	                SQLAlchemy
Database	        PostgreSQL
Containerization	Docker
API Docs	        Swagger UI
Language	        Python

---

## 📂 Project Structure
```
streamlit_postgres_crud/
├── app.py                 # Streamlit frontend
├── db.py                  # Streamlit DB connector
├── fastapi_crud/          # FastAPI backend
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── docker-compose.yml     # PostgreSQL Docker setup
├── requirements.txt
├── .env                   # Environment variables (not committed)
└── README.md
```

---

## 🗄️ Database Schema
```sql
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(50),
    salary NUMERIC(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

<img width="1742" height="656" alt="image" src="https://github.com/user-attachments/assets/b0c8d609-6705-466a-99cd-e1c96cfc4b4d" />

---

## ⚙️ Setup Instructions
#### 1️⃣ Clone Repository
`git clone https://github.com/abrahamj101/employee-crud-streamlit-postgres`
`cd streamlit_postgres_crud`

#### 2️⃣ Create Virtual Environment
`python -m venv venv`
`venv\Scripts\activate`

#### 3️⃣ Install Dependencies
`pip install -r requirements.txt`

#### 4️⃣ Start PostgreSQL (Docker)
`docker compose up -d`

#### 5️⃣ Run FastAPI Backend
`uvicorn fastapi_crud.main:app --reload`

#### Access API docs:
`http://127.0.0.1:8000/docs`

<img width="1673" height="974" alt="image" src="https://github.com/user-attachments/assets/ee2f3f81-d2b9-47de-be67-ca656649eb66" />


#### 6️⃣ Run Streamlit Frontend
`streamlit run app.py`

<img width="783" height="1545" alt="image" src="https://github.com/user-attachments/assets/72adddd6-41ef-4cc5-858b-a543236ebe6e" />

#### Run Both Simultaneously
```
# This opens two windows: one for FastAPI, one for Streamlit
start powershell -NoExit -Command ".\venv\Scripts\Activate; uvicorn fastapi_crud.main:app --reload"
start powershell -NoExit -Command ".\venv\Scripts\Activate; streamlit run app.py"
```

---

## 📈 What This Project Demonstrates
REST API development with FastAPI
Database modeling with SQLAlchemy ORM
Docker-based database setup
Frontend/backend separation
Environment variable configuration
Real-world CRUD workflows

---

## 🔮 Future Improvements
Connect Streamlit frontend to FastAPI API
Authentication and authorization
Pagination & search
Dockerize FastAPI
Cloud deployment (AWS/GCP)

---

## 📄 License
Open-source, educational project.
=======
# Employee-Management-API
>>>>>>> 8ad1eca0979213e1b1554facf95a0bc0edcb19f6
