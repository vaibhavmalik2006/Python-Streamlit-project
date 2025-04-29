import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="new_schema2"
)

cursor = connection.cursor()

# Create the table only if it doesn't already exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        sex VARCHAR(10),
        income FLOAT
    )
""")

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Update Employee")
    print("4. Read (income > 4000)")
    print("5. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        query = "INSERT INTO employee (id, name, sex, income) VALUES (%s, %s, %s, %s)"
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        sex = input("Enter employee sex: ")
        income = float(input("Enter employee income: "))
        cursor.execute(query, (emp_id, name, sex, income))
        print("✅ Employee Added Successfully.")

    elif ch == 2:
        emp_id = int(input("Enter employee ID to delete: "))
        query = "DELETE FROM employee WHERE id = %s"
        cursor.execute(query, (emp_id,))
        print("🗑️ Employee deleted successfully.")

    elif ch == 3:
        emp_id = int(input("Enter employee ID to update: "))
        name = input("Enter new employee name: ")
        sex = input("Enter new employee sex: ")
        income = float(input("Enter new employee income: "))
        query = "UPDATE employee SET name = %s, sex = %s, income = %s WHERE id = %s"
        cursor.execute(query, (name, sex, income, emp_id))
        print("🔁 Employee updated successfully.")

    elif ch == 4:
        query = "SELECT * FROM employee WHERE income > 4000"
        cursor.execute(query)
        data = cursor.fetchall()
        if data:
            print("\nEmployees with income > 4000:")
            for row in data:
                print(f"ID: {row[0]}, Name: {row[1]}, Sex: {row[2]}, Income: {row[3]}")
        else:
            print("No employees found with income greater than 4000.")

    elif ch == 5:
        print("👋 Exiting the system.")
        break

    else:
        print("❌ Invalid choice. Please try again.")

    connection.commit()

cursor.close()
connection.close()
df =  pd.DataFrame(
  np.random.randn(10,20),
  columns=('clo %d' % i for i in range(1,21))

)
st.table(df)
