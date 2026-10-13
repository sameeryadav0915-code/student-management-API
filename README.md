
<div align="center">

# 🎓 Student Management API

### ⚡ A Smart & Simple Student Record Management System

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/REST_API-Developer-blueviolet?style=for-the-badge" alt="REST API"/>
</p>

<p>
  <b>Built with Python • Powered by FastAPI • Backed by SQLite</b>
</p>

<p>
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-api-endpoints">API Endpoints</a> •
  <a href="#-future-enhancements">Future Enhancements</a>
</p>

</div>

---

## 🌌 Overview

**Student Management API** is a lightweight backend application designed to manage student records through RESTful API endpoints.

Built using **Python, FastAPI, and SQLite**, it supports creating, viewing, updating, and deleting student records. Interactive API documentation makes it easy to test the available operations.

> 💡 **Project goal:** Learn backend development, REST API design, database integration, and CRUD operations through a practical project.

---

## ✨ Key Features

<table>
  <tr>
    <td width="50%">
      <h3>➕ Create</h3>
      Add student records with roll number, name, and marks.
    </td>
    <td width="50%">
      <h3>📋 Read</h3>
      Retrieve student records through an API request.
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>✏️ Update</h3>
      Update a student's marks using their roll number.
    </td>
    <td width="50%">
      <h3>🗑️ Delete</h3>
      Remove a student record from the database.
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>💾 Persistent Storage</h3>
      Store records in an SQLite database.
    </td>
    <td width="50%">
      <h3>📚 Interactive Docs</h3>
      Explore and test endpoints using Swagger UI.
    </td>
  </tr>
</table>

---

## 🧰 Technology Stack

| Technology | Role |
|:--|:--|
| 🐍 **Python** | Core programming language |
| ⚡ **FastAPI** | API framework |
| 🗄️ **SQLite** | Database storage |
| 🚀 **Uvicorn** | ASGI server |
| 📖 **Swagger UI** | Interactive API testing |

---

## 📂 Project Structure

```text
student-management-api/
│
├── main.py          # API routes and application logic
├── database.py      # Database setup
├── README.md        # Project documentation
└── students.db      # Local SQLite database
```

> 🔒 **Security note:** Do not upload a database containing private student information. Keep `students.db` local if it contains sensitive data.

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/student-management-api.git
```

### 2. Enter the project directory

```bash
cd student-management-api
```

### 3. Install dependencies

```bash
python -m pip install fastapi uvicorn
```

### 4. Start the server

```bash
python -m uvicorn main:app --reload
```

### 5. Explore the API

Once the server starts, open these links in your browser:

| Resource | URL |
|:--|:--|
| 🧪 Swagger UI | http://127.0.0.1:8000/docs |
| 📘 ReDoc | http://127.0.0.1:8000/redoc |
| 🏠 Home endpoint | http://127.0.0.1:8000/ |

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|:--:|:--|:--|
| 🟢 GET | `/` | Check API status |
| 🔵 GET | `/student` | Retrieve all students |
| 🟠 POST | `/student` | Add a student |
| 🟣 PUT | `/student/{roll}?marks=90` | Update student marks |
| 🔴 DELETE | `/student/{roll}` | Delete a student |

---

## 🧪 Example API Request

### ➕ Create a student

**Method:** `POST`

**Endpoint:** `/student`

**Request body:**

```json
{
  "roll": 101,
  "name": "Rahul",
  "marks": 85
}
```

**Example response:**

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

*Example data only. The roll number must not already exist.*

---

## 🧠 What I Learned

Through this project, I practised:

- Understanding REST API architecture.
- Implementing GET, POST, PUT, and DELETE methods.
- Creating API routes with FastAPI.
- Connecting Python with an SQLite database.
- Performing CRUD operations.
- Testing endpoints through Swagger UI.
- Handling database errors and missing records.

---

## 🚀 Future Enhancements

- [ ] Add Pydantic models for input validation.
- [ ] Retrieve an individual student by roll number.
- [ ] Update student names and other details.
- [ ] Add automated tests using Pytest.
- [ ] Implement authentication and authorization.
- [ ] Deploy the API online.

---

## 👨‍💻 About the Developer

<div align="center">

### Hi, I'm YOUR-NAME! 👋

🎓 B.Tech Student  
💻 Aspiring Python & Backend Developer  
🚀 Learning by building real-world projects

**One project at a time. One skill at a time.**

<a href="https://github.com/YOUR-USERNAME">
  <img src="https://img.shields.io/badge/GitHub-Visit_My_Profile-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile"/>
</a>

</div>

---

<div align="center">

### ⭐ Enjoyed this project?

If you find this project useful, consider giving the repository a star!

**Made with ❤️ and Python**

</div>
