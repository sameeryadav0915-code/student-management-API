
# 🎓 Student Management API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Project Status"/>
</p>

<p align="center">
  <b>A simple, efficient, and beginner-friendly REST API for managing student records.</b>
  <br/>
  Built with Python, FastAPI, and SQLite.
</p>

---

## 📌 About the Project

The **Student Management API** is a backend project developed using Python and FastAPI. It provides REST API endpoints to create, retrieve, update, and delete student records.

Student information is stored in an SQLite database, allowing records to remain available after the API is restarted.

This project helped me practice REST API development, HTTP methods, database operations, and backend programming fundamentals.

## ✨ Features

- ➕ **Add Students** — Register a student with a roll number, name, and marks.
- 📋 **View Students** — Retrieve all student records.
- ✏️ **Update Marks** — Update a student's marks using their roll number.
- 🗑️ **Delete Students** — Remove a student record.
- 💾 **Database Storage** — Store records using SQLite.
- 📚 **Interactive API Docs** — Test endpoints through Swagger UI.
- ⚠️ **Error Handling** — Handle duplicate roll numbers and missing students.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming language |
| ⚡ FastAPI | REST API framework |
| 🗄️ SQLite | Database |
| 🚀 Uvicorn | Development server |
| 📖 Swagger UI | API testing and documentation |

## 📂 Project Structure

```text
student-management-api/
│
├── main.py          # API endpoints and application logic
├── database.py      # Database initialization
├── README.md        # Project documentation
└── students.db      # SQLite database (created locally)
```

> **Note:** `students.db` is generated locally. You generally should not commit the database file if it contains real or private student information.

## ⚙️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/student-management-api.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2️⃣ Open the Project Folder

```bash
cd student-management-api
```

### 3️⃣ Install Dependencies

```bash
python -m pip install fastapi uvicorn
```

### 4️⃣ Run the API

```bash
python -m uvicorn main:app --reload
```

### 5️⃣ Open the API Documentation

Once the server is running, open:

**Swagger UI:** http://127.0.0.1:8000/docs

**API Home:** http://127.0.0.1:8000/

You can test the API endpoints directly from Swagger UI.

## 🔗 API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/student` | Get all students |
| POST | `/student` | Add a new student |
| PUT | `/student/{roll}?marks=90` | Update student marks |
| DELETE | `/student/{roll}` | Delete a student |

## 🧪 Example Request

### Add a Student

**Endpoint:** `POST /student`

**JSON Request Body:**

```json
{
  "roll": 101,
  "name": "Rahul",
  "marks": 85
}
```

**Example Response:**

```json
{
  "message": "Student added successfully",
  "student": {
    "roll": 101,
    "name": "Rahul",
    "marks": 85
  }
}
```

*Example data only. Use a roll number that does not already exist in your database.*

## 🎯 Learning Outcomes

Through this project, I practised:

- Understanding REST API architecture.
- Working with GET, POST, PUT, and DELETE methods.
- Building endpoints with FastAPI.
- Connecting Python applications to SQLite.
- Performing database CRUD operations.
- Testing APIs using Swagger UI.
- Handling common database errors.

## 🚀 Future Improvements

- [ ] Add Pydantic models for request validation.
- [ ] Add an endpoint to retrieve a student by roll number.
- [ ] Support updating student names as well as marks.
- [ ] Add automated tests using Pytest.
- [ ] Add authentication and authorization.
- [ ] Deploy the API online.

## 👨‍💻 Author

**Your Name**

🎓 B.Tech Student | Aspiring Python Developer

🔗 GitHub: https://github.com/YOUR-USERNAME

---

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
  <br/><br/>
  <b>Built with Python, curiosity, and a passion for learning. 💙</b>
</p>
