from classes.parent import Parent
from classes.student import Student
from classes.teacher import Teacher
from classes.employee import Employee
from classes.user import User
from classes.manager import Manager
import mysql.connector

DATABASE_NAME = "academy_of_tomorrow"

# Configuration dictionary for database connection parameters.
# - 'host': The address of the database server (e.g., 'localhost' for local server).
# - 'user': The username for connecting to the database.
# - 'password': The password associated with the username for authentication.
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
}



# Connects to the database using the MySQL connector.
# - Attempts to establish a connection using provided configuration values (host, user, password, port, timeout).
# - If successful, prints a success message and returns the connection object.
# - If there is a MySQL error or another exception, it prints the error message and exits the program.
def connect_to_database():
    try:
        print("Connecting .....")
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],

        )
        print("Connection successful!")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit(1)
    except Exception as e :
        print('here', e)



# Manages database connections and operations.
# - Initializes a connection to the database using the `connect_to_database` function.
# - Creates a cursor object for executing SQL queries.
# - Attempts to select the specified database using `USE` command.
# - If the database cannot be selected, an error message is printed, and the exception is re-raised to halt execution.
class DatabaseManager:
    """Handles database Connections."""
    def __init__(self, to_use_database = True):
        self.conn = connect_to_database()
        self.cursor = self.conn.cursor()
        try:
            # Set the database
            if to_use_database:
                self.cursor.execute(f"USE {DATABASE_NAME}")
        except Exception as e:
            print(f"Error selecting database '{DATABASE_NAME}': {e}")
            raise  # Re-raise the exception to stop execution if the database cannot be selected



# Initializes the database by checking if it exists and creating it if necessary.
# - Checks if the specified database exists using the `database_exists` method.
# - If the database does not exist, attempts to create it using the `create_database` method.
# - Handles any MySQL errors and prints an appropriate message if the database doesn't exist or cannot be created.
    # Database Initialization Functions
    def initialize_database(self):
        try:
            is_database_exists = self.database_exists(DATABASE_NAME)
            if not is_database_exists:
                self.create_database(DATABASE_NAME)
        except mysql.connector.Error as err:
            print(f"Database `{DATABASE_NAME}` does not exist. Creating it...")
    


# Checks if a specific database exists.
# - Executes the "SHOW DATABASES LIKE" query to check for the existence of the given database.
# - Returns True if the database exists, otherwise returns False.
    def database_exists(self,db_name):
        """
        Check if a database exists.
        """
        cursor = self.conn.cursor()
        cursor.execute("SHOW DATABASES LIKE %s", (db_name,))
        return cursor.fetchone() is not None



# Creates a new database with the specified name.
# - Executes the SQL command to create the database with the default UTF-8 character set.
# - Prints a success message if the database is created successfully.
# - If an error occurs during the creation, it prints the error message and exits the program.
    def create_database(self,db_name):
        """
        Create the database.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"CREATE DATABASE {db_name} DEFAULT CHARACTER SET 'utf8'")
            print(f"Database `{db_name}` created successfully.")
        except mysql.connector.Error as err:
            print(f"Failed to create database: {err}")
            exit(1)
    


# Creates tables in the specified database based on the provided table definitions.
# - Switches to the specified database using the `USE` command.
# - Iterates over the `tables` dictionary, where each table name is paired with its corresponding SQL creation query.
# - Executes each SQL query to create the respective table.
# - Prints a success message if the table is created successfully.
# - If an error occurs while creating a table, it prints the error message and exits the program.
    # Table Creation Functions
    def create_tables(self,tables): 
        cursor = self.conn.cursor()
        cursor.execute(f"USE {DATABASE_NAME}")
        for table_name, table_query in tables.items():
            try:
                print(f"Creating table `{table_name}`...")
                cursor.execute(table_query)
                print(f"Table `{table_name}` created successfully.")
            except mysql.connector.Error as err:
                print(f"Error creating table `{table_name}`: {err}")
                exit(1)
    


                                                     # User Functions


# Fetches a user from the database by email.
# - Executes a SELECT query to retrieve user details from the "Users" table where the email matches.
# - Uses a dictionary cursor to return results in dictionary format.
# - Returns the first matching user if found, otherwise returns None.
# - If an error occurs while fetching the user, it prints the error message and returns None.
    def get_user(self, email):
        try:
            cursor = self.conn.cursor(dictionary=True)
            # Execute the SQL query
             # Execute the SQL query
            cursor.execute("SELECT * FROM Users WHERE email = %s", (email,))
            return cursor.fetchone()
        except Exception as e:
            # Log the error and return None if an exception occurs
            print(f"An error occurred while fetching the user: {e}")
            return None 
        
    def update_user_password(self, id, new_password):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE Users SET password = %s WHERE id = %s", (new_password, id))  # Execute the SQL query
            self.conn.commit()  # Commit the transaction
            print("Password updated successfully.")
        except Exception as e:
            print(f"An error occurred while updating the password: {e}")    


                                             # Manager Functions

# Inserts a user into the database and handles role-specific insertion into the corresponding tables.
# - Inserts the user's basic information into the "Users" table.
# - Based on the user type (Manager, Parent, Student, Teacher, or Employee), inserts additional information into the appropriate table.
# - Retrieves and sets the ID of the newly created user.
# - Commits the transaction if all insertions are successful, or rolls back in case of an error.
# - Returns the user ID upon successful creation or None if an error occurs.
    def create_user(self, user):
        """
        Inserts a user object into the database.
        :param user: An instance of User or its subclass.
        :return: The ID of the created user, or None on failure.
        """
        cursor = self.conn.cursor()
        try:
            # Insert into Users table
            cursor.execute("""
                INSERT INTO Users (name, email, role, password)
                VALUES (%s, %s, %s, %s)
            """, (user.name, user.email, user.role, user.password))

            # Get the user ID of the inserted user
            user.id = cursor.lastrowid

            # Insert into role-specific tables
            if isinstance(user, Manager):
                cursor.execute("INSERT INTO Managers (manager_id) VALUES (%s)", (user.id,))

            elif isinstance(user, Parent):
                cursor.execute("INSERT INTO Parents (parent_id) VALUES (%s)", (user.id,))

            elif isinstance(user, Student):
                cursor.execute("""
                    INSERT INTO Students (student_id, age, grade_level, parent_id)
                    VALUES (%s, %s, %s, %s)
                """, (user.id, user.age, user.grade_level, user.parent_id))

            elif isinstance(user, Teacher):
                cursor.execute("""
                    INSERT INTO Teachers (teacher_id, specialization, hire_date, salary)
                    VALUES (%s, %s, %s, %s)
                """, (user.id, user.specialization, user.hire_date, user.salary))

            elif isinstance(user, Employee):
                cursor.execute("""
                    INSERT INTO Employees (employee_id, salary)
                    VALUES (%s, %s)
                """, (user.id, user.salary))

            # Commit the transaction
            self.conn.commit()
            return user.id

        except Exception as e:
            self.conn.rollback()
            print(f"Error creating user: {e}")
            return None

        finally:
            cursor.close()



# Creates a new course in the database and inserts the associated schedule.
# - Inserts the course details (name, description, teacher ID, max capacity) into the "Courses" table.
# - Commits the transaction and retrieves the ID of the newly inserted course.
# - Sets the course ID in the schedule object and calls `insert_into_schedule` to insert the schedule into the database.
# - Returns the ID of the newly created course or None if an error occurs.
    def create_course(self,course, schedule): 
        try:
            # Execute the SQL query
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Courses (name, description, teacher_id, max_capacity) VALUES (%s, %s, %s, %s)",
                (course.name, course.description, course.teacher_id, course.max_capacity)
            )
            # Commit the transaction
            self.conn.commit()
            schedule.course_id = cursor.lastrowid
            self.insert_into_schedule(schedule)
            # Return the ID of the last inserted row
            return cursor.lastrowid
        except Exception as e:
            # Log the error and return None if an exception occurs
            print(f"An error occurred while creating the course: {e}")
            return None



# Fetches all the classrooms from the "ClassRooms" table.
# - Executes a SELECT query to retrieve all classroom details.
# - Uses a dictionary cursor to return results in dictionary format.
# - Returns a list of all classrooms or None if an error occurs during the process.
    def get_class_rooms(self):  

        try:
            # Execute the SQL query
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM ClassRooms")
            # Fetch all the results
            class_rooms = cursor.fetchall()
            return class_rooms  # Return the results
        except Exception as e:
            # Log the error and return None if an exception occurs
            print(f"An error occurred while fetching class rooms: {e}")
            return None



# Inserts a new schedule entry into the "Schedules" table.
# - Executes an SQL query to insert the course ID, teacher ID, date, time, and classroom ID into the schedule.
# - Commits the transaction if successful and retrieves the ID of the last inserted schedule entry.
# - Returns the ID of the newly inserted schedule or None if an error occurs during the insertion.  
    def insert_into_schedule(self, schedule):

        try:
            # Execute the SQL query
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Schedules (course_id, teacher_id, date, time, class_room_id) VALUES (%s, %s, %s, %s, %s)",
                (schedule.course_id, schedule.teacher_id, schedule.date, schedule.time, schedule.class_room_id))
            
            # Commit the transaction
            self.conn.commit()
            return cursor.lastrowid
        except Exception as e:
            # Log the error and return None if an exception occurs
            print(f"An error occurred while inserting into the schedule: {e}")
            return None
   


# Fetches a course from the "Courses" table based on the provided course ID.
# - Executes a SELECT query to retrieve course details where the ID matches.
# - Returns the first matching course if found or None if no course is found or an error occurs.
# - Uses a dictionary cursor to return the results in dictionary format.
    def get_course(self,course_id):
        try:
            # Execute the SQL query
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Courses WHERE id = %s", (course_id,))
            # Fetch the result
            course = cursor.fetchone()
            return course  # Return the result
        except Exception as e:
            # Log the error and return None if an exception occurs
            print(f"An error occurred while fetching course: {e}")
            return None



# Removes a student from the waitlist for a specific course.
# - Executes a DELETE query to remove the student from the "Queue" table where the student ID and course ID match.
# - Commits the transaction if successful and returns True.
# - If an error occurs, it logs the error and returns False.
    def remove_student_from_waitlist(self,student_id,course_id):


        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                DELETE FROM Queue
                WHERE student_id = %s AND course_id = %s
            """, (student_id, course_id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"An error occurred while removing the student from the waitlist: {e}")
            return False
    


# Assigns a task to a specific employee.
# - Executes an UPDATE query to set the `assigned_to` field in the "tasks" table, linking the task to the employee by their ID.
# - Commits the transaction if successful and returns True.
# - If an error occurs, it logs the error and returns False.
    def assign_task_to_employee(self,employee_id,task_id):
    
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""
                UPDATE tasks
                SET assigned_to = %s
                WHERE id = %s
            """, (employee_id, task_id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"An error occurred while managing the employee tasks: {e}")
            return False



# Retrieves all tasks from the "tasks" table, including the assigned employee's name.
# - Executes a SELECT query that joins the "tasks" table with the "users" table to fetch employee names for assigned tasks.
# - Returns a list of tasks with their details, including the employee's name, or None if an error occurs.
    def get_all_tasks(self):

        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""SELECT tt.*, us.name as employee_name FROM tasks tt
                           LEFT JOIN users us ON tt.assigned_to = us.id
                           """)
            return cursor.fetchall()
        except Exception as e:
            print(f"An error occurred while fetching all tasks: {e}")
            return None
    


# Retrieves the total income details from the "payments" table.
# - Executes a SELECT query to fetch payment amounts, parent names, and descriptions by joining the "payments" table with the "users" table.
# - Returns a list of income details, including amount, parent name, and description, or None if an error occurs.
    def get_total_income(self):
        try:
            cursor = self.conn.cursor(dictionary=True)

            # Fetch income details from payments
            cursor.execute("""
                SELECT p.amount, u.name AS parent_name, p.description 
                FROM payments p
                JOIN users u ON p.parent_id = u.id
            """)
            return cursor.fetchall()
        except Exception as e:
            print(f"An error occurred while fetching income details: {e}")
            return None
        


# Retrieves salary details for all teachers from the "teachers" table.
# - Executes a SELECT query to fetch teacher salaries and their names by joining the "teachers" table with the "users" table.
# - Returns a list of teachers' salaries and names, or None if an error occurs.
    def get_teachers_salary(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            # Fetch outcome details from teachers (salary)
            cursor.execute("""
                SELECT t.salary, u.name AS teacher_name
                FROM teachers t
                JOIN users u ON t.teacher_id = u.id
            """)
            return cursor.fetchall()

        except Exception as e:
            print(f"An error occurred while fetching teachers' salaries: {e}")
            return None



# Retrieves salary details for all employees from the "employees" table.
# - Executes a SELECT query to fetch employee salaries and their names by joining the "employees" table with the "users" table.
# - Returns a list of employees' salaries and names, or None if an error occurs.
    def get_employees_salary(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            # Fetch outcome details from teachers (salary)
            cursor.execute("""
            SELECT e.salary, u.name AS employee_name
            FROM employees e
            JOIN users u ON e.employee_id = u.id
            """)
            return cursor.fetchall()

        except Exception as e:
            print(f"An error occurred while fetching teachers' salaries: {e}")
            return None

    def create_classroom(self,class_room):    
        try:
            cursor = self.conn.cursor()
            cursor.execute("""  INSERT INTO ClassRooms (name, capacity, location) VALUES (%s, %s, %s) """, (class_room.name, class_room.capacity, class_room.location))
            self.conn.commit()
            print("Classroom created successfully.")
        except Exception as e:
            print(f"An error occurred while creating the classroom: {e}")    

    def waitlist_course_status(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""
            SELECT 
            c.id, 
            c.name, 
            COUNT(q.student_id) AS registered_students
            FROM queue q
            JOIN courses c ON q.course_id = c.id
            GROUP BY c.id, c.name
            ORDER BY registered_students DESC;""")
            return cursor.fetchall()
        except Exception as e:  
            print(f"An error occurred while fetching the course waitlist status: {e}")    
                           

                                                    # Parent Functions



# Fetches the number of students enrolled in a specific course.
# - Executes a SELECT query to count the number of records in the "CourseEnrollments" table for the given course ID.
# - Returns the count of enrollments for the course or None if an error occurs.
    def fetch_enrollment_count_for_course(self, course_enrollment):

        try:
            # Execute the SQL query
            cursor = self.conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM CourseEnrollments WHERE course_id = %s", (course_enrollment.course_id,))
            # Fetch the result
            count = cursor.fetchone()[0]
            return count  # Return the result
        except Exception as e:
            # Log the error and return None if an exception occurs
            print(f"An error occurred while fetching enrollment count: {e}")
            return None



# Checks if a student is already registered in a specific course.
# - Executes a SELECT query to count the number of enrollments for the given student and course.
# - Returns True if the student is enrolled in the course, otherwise returns False.
# - Handles any exceptions that occur during the process and logs the error.
    def is_child_registered(self,course_enrollment):
        try:
            cursor = self.conn.cursor(dictionary=True)
            # Execute the SQL query with parameterized input for safety
            cursor.execute(
                "SELECT COUNT(*) as count FROM CourseEnrollments WHERE course_id = %s AND student_id = %s",
                (course_enrollment.course_id, course_enrollment.student_id)
            )
            result = cursor.fetchone()
            return result["count"] >= 1 if result else False
        except Exception as e:
            # Log the error and return False if an exception occurs
            print(f"An error occurred while checking if the student is registered: {e}")
            return False
        


# Checks if a student is in the waitlist for a specific course.
# - Executes a SELECT query to check if the student is present in the "Queue" table for the given course ID.
# - Returns True if the student is found in the waitlist, otherwise returns False.
# - Handles any exceptions that occur during the process and logs the error.
    def is_child_in_waitlist(self,course_enrollment):
        try:
            cursor = self.conn.cursor()
            # Execute the SQL query with parameterized input for safety
            cursor.execute("""
                SELECT 1 
                FROM Queue 
                WHERE course_id = %s AND student_id = %s 
                LIMIT 1
            """, (course_enrollment.course_id, course_enrollment.student_id))
            result = cursor.fetchone()
            return result is not None
        except Exception as e:
            # Log the error and return False if an exception occurs
            print(f"An error occurred while checking if the student is in the waitlist: {e}")
            return False



# Inserts a student into a course's enrollment list.
# - Executes an INSERT query to add the student ID and course ID to the "CourseEnrollments" table.
# - Commits the transaction if the insertion is successful and returns True.
# - If an error occurs during the insertion, it logs the error and returns False.
    def insert_child_to_course(self, course_enrollment):
        try:
            cursor = self.conn.cursor()
            # Execute the SQL query with parameterized input for safety
            cursor.execute(
                "INSERT INTO CourseEnrollments (student_id, course_id) VALUES (%s, %s)",
                (course_enrollment.student_id, course_enrollment.course_id)
            )
            # Commit the transaction
            self.conn.commit()
            return True
        except Exception as e:
            # Log the error and return False if an exception occurs
            print(f"An error occurred while inserting the student to the course: {e}")
            return False



# Adds a student to the waitlist for a specific course.
# - Executes an INSERT query to add the student ID and course ID to the "Queue" table.
# - Commits the transaction if the insertion is successful and returns True.
# - If an error occurs during the insertion, it logs the error and returns False.  
    def add_child_to_waitlist(self, queue_entry):
        try:
            cursor = self.conn.cursor()
            # Execute the SQL query with parameterized input for safety
            cursor.execute(
                "INSERT INTO Queue (student_id, course_id) VALUES (%s, %s)",
                (queue_entry.student_id, queue_entry.course_id)
            )
            # Commit the transaction
            self.conn.commit()
            return True
        except Exception as e:
            # Log the error and return False if an exception occurs
            print(f"An error occurred while adding the student to the waitlist: {e}")
            return False
        


# Fetches the waitlist for a specific course, including student names and registration dates.
# - Executes a SELECT query to retrieve the student ID, student name, and registration date from the "Queue" and "users" tables.
# - Orders the students by their registration date in ascending order.
# - Returns the list of students on the waitlist, or None if an error occurs during the process.
    def get_waitlist(self, course_id):

    
        """
        Fetch the waitlist for a specific course, including student names and registration dates.
        """
        try:
            cursor = self.conn.cursor(dictionary=True)
            # Execute the SQL query to join Users and Queue tables
            cursor.execute("""
                SELECT 
                    Queue.student_id, 
                    Users.name AS student_name, 
                    Queue.registered_at
                FROM Queue
                JOIN users ON Queue.student_id = Users.id
                WHERE Queue.course_id = %s
                ORDER BY Queue.registered_at ASC
            """, (course_id,))
            return cursor.fetchall()
        except Exception as e:
            # Log the error and return None if an exception occurs
            print(f"An error occurred while fetching the waitlist: {e}")
            return None
        


# Retrieves all students (children) associated with a given parent.
# - Executes a SELECT query to join the "Students" and "Users" tables, filtering by the parent's ID.
# - Returns a list of student IDs and names for the given parent, or an empty list if no students are found or an error occurs.
    def get_students_by_parent_id(self, parent_id):
        """Retrieve all students (children) for a given parent."""
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT s.student_id, u.name AS student_name
                FROM Students s
                JOIN Users u ON s.student_id = u.id
                WHERE s.parent_id = %s
            """, (parent_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching students for parent_id {parent_id}: {e}")
            return []
    


# Retrieves all course enrollments for a list of student IDs.
# - Executes a SELECT query that joins the "CourseEnrollments" and "Courses" tables to fetch the course name and grade for each student.
# - Uses dynamic placeholders to handle multiple student IDs in the WHERE clause.
# - Returns a list of course enrollments (student ID, course name, grade) or an empty list if an error occurs or no enrollments are found.
    def get_course_enrollments(self,  student_ids):
        """Retrieve all course enrollments for a list of student IDs."""
        try:
            cursor = self.conn.cursor(dictionary=True)

    # Generate the correct number of placeholders
            placeholders = ','.join(['%s'] * len(student_ids))
            query = f"""
                SELECT ce.student_id, c.name AS course_name, ce.grade
                FROM CourseEnrollments ce
                JOIN Courses c ON ce.course_id = c.id
                WHERE ce.student_id IN ({placeholders})
            """
            # Execute the query with the list of student_ids unpacked
            cursor.execute(query, student_ids)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching course enrollments: {e}")
            return []



# Retrieves the waitlist status for a list of student IDs.
# - Executes a SELECT query that joins the "Queue" and "Courses" tables to fetch the course name for each student on the waitlist.
# - Uses dynamic placeholders to handle multiple student IDs in the WHERE clause.
# - Returns a list of waitlist entries (student ID, course name) or an empty list if an error occurs or no students are found.  
    def get_waitlist_status(self, student_ids):
        """Retrieve waitlist status for a list of student IDs."""
        try:
            cursor = self.conn.cursor(dictionary=True)
            placeholders = ','.join(['%s'] * len(student_ids))
            query = f"""
                SELECT q.student_id, c.name AS course_name
                FROM Queue q
                JOIN Courses c ON q.course_id = c.id
                WHERE q.student_id IN ({placeholders})
            """
            cursor.execute(query, student_ids)
            return cursor.fetchall()
        
        except Exception as e:
            print(f"Error fetching waitlist status: {e}")
            return []



# Retrieves the position of a student in the waitlist for a specific course.
# - Executes a query to calculate the position of the student in the waitlist based on their registration time relative to other students.
# - Fetches the student's name for display purposes.
# - Returns a dictionary containing the student's position and name, or None if an error occurs or no data is found.
    def get_child_position_in_waitlist(self, student_id, course_id):

        try:
            cursor = self.conn.cursor(dictionary=True)
            # Query to calculate the position
            cursor.execute("""
            SELECT COUNT(*) + 1 AS position
            FROM Queue
            WHERE course_id = %s
            AND registered_at < (
                SELECT registered_at
                FROM Queue
                WHERE course_id = %s AND student_id = %s
            )
            """, (course_id, course_id, student_id))
            position_result = cursor.fetchone()

            # Fetch student name for display purposes
            cursor.execute("""
            SELECT name
            FROM users
            WHERE id = %s
            """, (student_id,))
            name_result = cursor.fetchone()

            # Combine results into a dictionary
            if position_result and name_result:
                return {
                    "position": position_result["position"],
                    "student_name": name_result["name"]
                }
            return None
        except Exception as e:
            # Log the error and return None if an exception occurs
            print(f"An error occurred while fetching the child's position in the waitlist: {e}")
            return None



# Adds a payment record to the "Payments" table.
# - Executes an INSERT query to add the parent ID, amount, payment date, and description into the payments table.
# - Commits the transaction if the insertion is successful and returns True.
# - If an error occurs during the insertion, it logs the error and returns None.  
    def add_payment(self,payment_info):
        try:
            cursor = self.conn.cursor()
            # Execute the SQL query
            cursor.execute("""
                INSERT INTO Payments (parent_id, amount, payment_date, description)
                VALUES (%s, %s, %s, %s)
            """, (payment_info.parent_id, payment_info.amount, payment_info.payment_date, payment_info.description))
            # Commit the transaction
            self.conn.commit()
            return True
        except Exception as e:
            # Log the error and return None if an exception occurs
            print(f"An error occurred while adding the payment: {e}")
            return None
    


                                                        # Student Functions



# Fetches course details, including schedule and classroom information, for a specific student.
# - Executes a SELECT query that joins "CourseEnrollments", "Schedules", "Courses", and "classRooms" tables to retrieve relevant details.
# - Orders the results by the course date and time.
# - Returns a list of course details (course name, date, time, and classroom name) or an empty list if an error occurs or no courses are found.
    def fetch_courses_for_student(self, student_id):
        """Fetch courses, schedule details, and classroom names for the given student ID."""
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT 
                    ce.course_id, 
                    c.name AS course_name, 
                    s.date AS course_date, 
                    s.time AS course_time, 
                    cr.name AS class_room_name
                FROM CourseEnrollments ce
                JOIN Schedules s ON ce.course_id = s.course_id
                JOIN Courses c ON ce.course_id = c.id
                JOIN classRooms cr ON s.class_room_id = cr.id
                WHERE ce.student_id = %s
                ORDER BY s.date, s.time
            """, (student_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"An error occurred while fetching courses: {e}")
            return []



# Fetches the grades for a specific student.
# - Executes a SELECT query that joins the "CourseEnrollments" and "Courses" tables to retrieve the course name and grade for the student.
# - Returns a list of grades for the courses the student is enrolled in, or an empty list if no grades are found or an error occurs.
    def fetch_grades(self, student_id):

        """Fetch grades for the given student ID."""
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT ce.course_id, c.name AS course_name, ce.grade
                FROM CourseEnrollments ce
                JOIN Courses c ON ce.course_id = c.id
                WHERE ce.student_id = %s
            """, (student_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"An error occurred while fetching grades: {e}")
            return []
            


                                                # Teacher Functions


# Fetches all courses assigned to a specific teacher, including schedule and classroom information.
# - Executes a SELECT query that joins the "Courses", "Schedules", and "ClassRooms" tables to retrieve course details.
# - Orders the results by the course date and time.
# - Returns a list of course details (course name, description, schedule, and classroom) or an empty list if an error occurs or no courses are found.
    def fetch_courses_for_teacher(self,teacher_id):

        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT c.id, c.name, c.description, c.max_capacity, s.date, s.time, cr.name as class_room_name
                FROM Courses c
                JOIN Schedules s ON c.id = s.course_id
                JOIN ClassRooms cr ON s.class_room_id = cr.id
                WHERE c.teacher_id = %s
                ORDER BY s.date, s.time
            """, (teacher_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"An error occurred while fetching courses: {e}")
            return []
    


# Fetches the students enrolled in a specific course taught by a teacher, including their grades.
# - Executes a SELECT query that joins the "CourseEnrollments", "Users", and "Courses" tables to retrieve student details and their current grade.
# - Returns a list of students (student ID, name, and grade) enrolled in the course, or an empty list if an error occurs or no students are found.
    def fetch_students_in_course(self,course_id, teacher_id):

        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT u.id as student_id, u.name as student_name , ce.grade as current_grade
                FROM CourseEnrollments ce
                JOIN Users u ON ce.student_id = u.id
                JOIN Courses c ON ce.course_id = c.id
                WHERE ce.course_id = %s AND c.teacher_id = %s
            """, (course_id,teacher_id))
            return cursor.fetchall()
        except Exception as e:
            print(f"An error occurred while fetching students: {e}")
            return []
    


# Updates the grade of a student in a specific course.
# - Executes an UPDATE query to set the student's grade in the "CourseEnrollments" table for the given student and course IDs.
# - Commits the transaction if successful and returns True.
# - If an error occurs during the update, it logs the error and returns False.
    def set_student_grade(self, student_id,course_id,grade):

        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE CourseEnrollments
                SET grade = %s
                WHERE student_id = %s AND course_id = %s
            """, (grade, student_id, course_id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"An error occurred while setting the student grade: {e}")
            return False 



                                                        # Employee Functions 


# Fetches all tasks assigned to a specific employee.
# - Executes a SELECT query to retrieve all tasks from the "tasks" table where the employee is assigned.
# - Returns a list of tasks for the employee, or None if an error occurs or no tasks are found.
# - Handles any exceptions that occur during the process and logs the error.
    def fetch_all_employee_tasks(self,emplyee_id):
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(""" 
                SELECT * FROM tasks 
                WHERE assigned_to = %s
            """, (emplyee_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"An error occurred while setting the student grade: {e}")
            return None 
        


# Updates the status of a specific task.
# - Executes an UPDATE query to set the task status in the "tasks" table based on the provided task ID.
# - Commits the transaction if the update is successful and returns True.
# - If an error occurs during the update, it logs the error and returns False.
    def update_task_status(self,task_id,status):
        try:
            cursor = self.conn.cursor(dictionary=True)

            cursor.execute("""
                UPDATE tasks
                SET status = %s
                WHERE id = %s
            """, (status, task_id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"An error occurred while updating the task status: {e}")
    


# Checks if a specific task is assigned to a given employee.
# - Executes a SELECT query to check if the task ID is assigned to the employee ID in the "tasks" table.
# - Returns True if the task is assigned to the employee, otherwise returns False.
# - If an error occurs during the check, it logs the error and returns None.
    def check_task_assignee(self,task_id,employee_id):
        try:
            cursor = self.conn.cursor(dictionary=True)
            # בדיקה אם המשימה שייכת לעובד
            cursor.execute("""
                SELECT id FROM tasks
                WHERE id = %s AND assigned_to = %s
            """, (task_id, employee_id))
            if cursor.fetchone() is None:
                return False
            return True
        except Exception as e:
            print(f"An error occurred while checking the task assignee: {e}")
            return None



# Creates a new task issue in the "tasks" table.
# - Executes an INSERT query to add the task description, status, and classroom ID to the "tasks" table.
# - Commits the transaction and returns the ID of the newly created task.
# - If an error occurs during task creation, it logs the error and returns None.
    def create_task_issue(self,task):

        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""
                INSERT INTO tasks (description, status, class_room_id)
                VALUES (%s, %s, %s)
            """, (task.description, task.status, task.class_room_id))
            self.conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"An error occurred while creating the task: {e}")
            return None
    
