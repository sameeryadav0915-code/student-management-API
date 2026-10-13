
import sqlite3

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll INTEGER PRIMARY KEY,
            name TEXT,
            marks INTEGER
        )
    """)

    conn.commit()
    conn.close()

create_database()
print("Database created successfully")