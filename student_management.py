import sqlite3

# -----------------------------
# Create Database and Table
# -----------------------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")

conn.commit()
conn.close()

# -----------------------------
# Add Student
# -----------------------------
def add_student(name, marks):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
    conn.commit()
    conn.close()
    print("Student added successfully!")


# -----------------------------
# View Students
# -----------------------------
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if rows:
        print("\n--- Student List ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Marks: {row[2]}")
    else:
        print("No students found.")

    conn.close()


# -----------------------------
# Update Student Marks
# -----------------------------
def update_student(student_id, new_marks):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (new_marks, student_id))
    conn.commit()
    
    if cursor.rowcount == 0:
        print("Student ID not found!")
    else:
        print("Student marks updated successfully!")

    conn.close()


# -----------------------------
# Delete Student
# -----------------------------
def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("Student ID not found!")
    else:
        print("Student deleted successfully!")

    conn.close()


# -----------------------------
# Menu System
# -----------------------------
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        add_student(name, marks)

    elif choice == "2":
        view_students()

    elif choice == "3":
        student_id = int(input("Enter student ID to update: "))
        new_marks = int(input("Enter new marks: "))
        update_student(student_id, new_marks)

    elif choice == "4":
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")