
import sqlite3
from fastapi import FastAPI, HTTPException
from database import create_database

app = FastAPI()

create_database()


def get_connection():
    return sqlite3.connect("students.db")


@app.get("/")
def home():
    return {"message": "My API is working!"}


@app.get("/student")
def get_students():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return students


@app.post("/student")
def add_student(student: dict):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (roll, name, marks) VALUES (?, ?, ?)",
            (student["roll"], student["name"], student["marks"])
        )
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Student roll number already exists"
        )
    finally:
        conn.close()

    return {
        "message": "Student added successfully",
        "student": student
    }


@app.put("/student/{roll}")
def update_student(roll: int, marks: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET marks = ? WHERE roll = ?",
        (marks, roll)
    )
    conn.commit()
    updated = cursor.rowcount
    conn.close()

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"message": "Student updated successfully"}


@app.delete("/student/{roll}")
def delete_student(roll: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE roll = ?",
        (roll,)
    )
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"message": "Student deleted successfully"}
