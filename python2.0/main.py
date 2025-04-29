import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",  # change if needed
    password="root",
    database="new_schema2"
)

cursor = connection.cursor()

# Uncomment if table not created
cursor.execute("CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(255), grades VARCHAR(50));")

while True:
    print("Student Management System")
    print("1. Add Student")
    print("2. Delete")
    print("3. Update")
    print("4. Read")
    print("5. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        query = "INSERT INTO students (id, name, grades) VALUES (%s, %s, %s)"
        stud_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        cursor.execute(query, (stud_id, name, grade))
        print("Student added successfully.")

    elif ch == 2:
        stud_id = int(input("Enter student ID: "))
        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (stud_id,))
        print("Student deleted successfully.")

    elif ch == 3:
        stud_id = int(input("Enter student ID: "))
        name = input("Enter new name: ")
        grade = input("Enter new grade: ")
        query = "UPDATE students SET name = %s, grades = %s WHERE id = %s"
        cursor.execute(query, (name, grade, stud_id))
        print("Student updated successfully.")

    elif ch == 4:
        query = "SELECT * FROM students"
        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            print(row)

    elif ch == 5:
        break

    else:
        print("Invalid choice. Try again.")

    connection.commit()

cursor.close()
connection.close()
