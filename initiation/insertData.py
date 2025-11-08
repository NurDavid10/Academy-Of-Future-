import json

# Function to insert data from JSON


# Reads data from a JSON file and inserts it into database tables.
# - Expects a JSON file with keys corresponding to table names.
# - Iterates over each key and inserts data into the respective table.
# - Commits changes to the database after all records are inserted.
def insert_data_from_json(db_manager, file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    conn = db_manager.conn  # Access the database connection from the manager
    cursor = conn.cursor()  # Create a cursor object for executing queries

    # Insert Users
    for user in data["Users"]:
        cursor.execute("""
            INSERT INTO Users (id, name, email, role, password, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (user["id"], user["name"], user["email"], user["role"], user["password"], user["created_at"]))

    # Insert Managers
    for manager in data["Managers"]:
        cursor.execute("""
            INSERT INTO Managers (manager_id)
            VALUES (%s)
        """, (manager["manager_id"],))

    # Insert Parents
    for parent in data["Parents"]:
        cursor.execute("""
            INSERT INTO Parents (parent_id)
            VALUES (%s)
        """, (parent["parent_id"],))

    # Insert Students
    for student in data["Students"]:
        cursor.execute("""
            INSERT INTO Students (student_id, age, grade_level, parent_id)
            VALUES (%s, %s, %s, %s)
        """, (student["student_id"], student["age"], student["grade_level"], student["parent_id"]))

    # Insert Teachers
    for teacher in data["Teachers"]:
        cursor.execute("""
            INSERT INTO Teachers (teacher_id, specialization, hire_date, salary)
            VALUES (%s, %s, %s, %s)
        """, (teacher["teacher_id"], teacher["specialization"], teacher["hire_date"], teacher["salary"]))

    # Insert Employees
    for employee in data["Employees"]:
        cursor.execute("""
            INSERT INTO Employees (employee_id, salary)
            VALUES (%s, %s)
        """, (employee["employee_id"], employee["salary"]))

    # Insert ClassRooms
    for classroom in data["ClassRooms"]:
        cursor.execute("""
            INSERT INTO ClassRooms (id, name, capacity, location, created_at)
            VALUES (%s, %s, %s, %s, %s)
        """, (classroom["id"], classroom["name"], classroom["capacity"], classroom["location"], classroom["created_at"]))

    # Insert Courses
    for course in data["Courses"]:
        cursor.execute("""
            INSERT INTO Courses (id, name, description, teacher_id, max_capacity, class_room_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (course["id"], course["name"], course["description"], course["teacher_id"], course["max_capacity"], course["class_room_id"]))

    # Insert CourseEnrollments
    for enrollment in data["CourseEnrollments"]:
        cursor.execute("""
            INSERT INTO CourseEnrollments (id, course_id, student_id, grade)
            VALUES (%s, %s, %s, %s)
        """, (enrollment["id"], enrollment["course_id"], enrollment["student_id"], enrollment["grade"]))

    # Insert Queue
    for queue in data["Queue"]:
        cursor.execute("""
            INSERT INTO Queue (id, course_id, student_id, registered_at)
            VALUES (%s, %s, %s, %s)
        """, (queue["id"], queue["course_id"], queue["student_id"], queue["registered_at"]))

    # Insert Tasks
    for task in data["Tasks"]:
        cursor.execute("""
            INSERT INTO Tasks (id, description, assigned_to, status, updated_at, class_room_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (task["id"], task["description"], task["assigned_to"], task["status"], task["updated_at"], task["class_room_id"]))

    # Insert Payments
    for payment in data["Payments"]:
        cursor.execute("""
            INSERT INTO Payments (id, parent_id, amount, payment_date, description)
            VALUES (%s, %s, %s, %s, %s)
        """, (payment["id"], payment["parent_id"], payment["amount"], payment["payment_date"], payment["description"]))

    # Insert Schedules
    for schedule in data["Schedules"]:
        cursor.execute("""
            INSERT INTO Schedules (id, course_id, teacher_id, date, time, class_room_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (schedule["id"], schedule["course_id"], schedule["teacher_id"], 
              schedule["date"], schedule["time"], schedule["class_room_id"]))

    # Commit changes
    conn.commit()
