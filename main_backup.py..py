
from fastapi import FastAPI

app = FastAPI()

students = []

@app.get("/")
def home():
    return {"message": "My API is working!"}

@app.get("/student")
def get_students():
    return students

@app.post("/student")
def add_student(student: dict):
    students.append(student)
    return {
        "message": "Student added successfully",
        "student": student
    }

@app.put("/student/{roll}")
def update_student(roll: int, marks: int):
    for student in students:
        if student["roll"] == roll:
            student["marks"] = marks
            return {
                "message": "Marks updated successfully",
                "student": student
            }

    return {"message": "Student not found"}

@app.delete("/student/{roll}")
def delete_student(roll: int):
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            return {
                "message": "Student deleted successfully"
            }

    return {"message": "Student not found"}
