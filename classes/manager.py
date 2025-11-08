# Imports necessary classes and modules:
# - Classes: Course, CourseEnrollment, Parent, Student, Task, Teacher, Employee, User, Schedule.
# - Modules: date and datetime from the datetime library for handling dates and timestamps.
from classes.class_room import ClassRoom
from classes.course import Course
from classes.courses_enrollments import CourseEnrollment
from classes.parent import Parent
from classes.student import Student
from classes.task import Task
from classes.teacher import Teacher
from classes.employee import Employee
from classes.user import User
from classes.schedule import Schedule
from datetime import date,datetime



# Represents a Manager, inheriting from the User class.
# Initializes a manager with ID, name, email, and password.
# The role is automatically set to "manager".
class Manager(User):
    """Represents a Manager."""
    def __init__(self, id=None, name="", email="", password="111"):
        super().__init__(id, name, email, "manager", password)
    


# Adds a new user to the system.
# Interacts with the database manager to create and save a new user record.
    def add_new_user(self,db_manager):\
    
        """
        Collects input from the user to create a new user and adds it to the database.
        :param db_manager: An instance of DatabaseManager to handle database operations.
        """
        print("Enter the following details to add a new user")
        
        # Common fields
        full_name = input("Enter full name: ")
        email = input("Enter email: ")
        role = input("Enter role (student/parent/teacher/manager/employee): ").lower()

        # Initialize the user object based on role
        if role == 'student':
            parent_id = int(input("Enter parent ID: "))
            student_age = int(input("Enter student age: "))
            grade_level = input("Enter student grade level: ")
            user = Student(name=full_name, email=email, age=student_age, grade_level=grade_level, parent_id=parent_id)

        elif role == 'teacher':
            specialization = input("Enter teacher specialization: ")
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            hire_date = date.fromisoformat(hire_date)  # Convert string to date object
            salary = float(input("Enter salary: "))
            user = Teacher(name=full_name, email=email, specialization=specialization, hire_date=hire_date, salary=salary)

        elif role == 'employee':
            salary = float(input("Enter salary: "))
            user = Employee(name=full_name, email=email, salary=salary)

        elif role == 'manager':
            user = Manager(name=full_name, email=email)

        elif role == 'parent':
            user = Parent(name=full_name, email=email)

        else:
            print(f"Invalid role '{role}' entered.")
            return

        # Use the DatabaseManager to add the user
        user_id = db_manager.create_user(user)
        if user_id:
            print(f"User '{full_name}' with role '{role}' added successfully! User ID: {user_id}")
        else:
            print("Failed to add the user. Please check the details and try again.")



# Creates a new course and schedules it.
# - Prompts the user for course details such as name, description, teacher ID, classroom, capacity, date, and time.
# - Validates the date and time inputs using the correct format (YYYY-MM-DD for date and HH:MM for time).
# - Retrieves available classrooms from the database and displays options for selection.
# - Creates a new Course and Schedule object with the provided details.
# - Saves the course and schedule to the database using the database manager.
# - Prints a success message upon successful creation of the course.
    def create_new_course(self,db_manager):

        print("Enter the following details to add a new course")
        course_name = input("Enter course name: ").strip()
        course_description = input("Enter course description: ").strip()
        teacher_id = input("Enter teacher ID: ").strip()
        class_rooms = db_manager.get_class_rooms()
        for room in class_rooms:
            print(f"{room['id']}. {room['name']} - ({room['capacity']}) - classroom id =  {room['id']}")
        class_room_id = input("Enter classroom id from the above options: : ").strip()
        course_capacity = input("Enter Course capacity: ").strip()

    # Validate and parse course date
        while True:
            course_date = input("Enter Course Scheduled date (YYYY-MM-DD): ").strip()
            try:
                parsed_date = datetime.strptime(course_date, '%Y-%m-%d').date()
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

        # Validate and parse course time
        while True:
            course_time = input("Enter Course Scheduled time (HH:MM, 24-hour format): ").strip()
            try:
                parsed_time = datetime.strptime(course_time, '%H:%M').time()
                break
            except ValueError:
                print("Invalid time format. Please enter the time in HH:MM format.")
        new_course = Course(
            name = course_name,
            description = course_description,
            teacher_id = teacher_id,
            max_capacity = course_capacity,
            class_room_id = class_room_id
        )
        schedule = Schedule(
            teacher_id = teacher_id,
            date = parsed_date,
            time = parsed_time,
            class_room_id = class_room_id
        )
        db_manager.create_course(new_course,schedule)
        print(f'Course {course_name} created successfully!')
    


# Manages the waitlist for a specific course.
# - Prompts the user to input the course ID and retrieves the course details from the database.
# - If the course is found, retrieves and displays the list of students on the course's waitlist.
# - Provides options to:
#   1. Assign the first student in the waitlist to the course.
#   2. Remove the first student from the waitlist.
#   3. Exit the waitlist management menu.
# - Uses the database manager to update the waitlist or course enrollments based on the selected option.
# - Prints appropriate messages for each action taken and returns the success status of the operation.
    def manage_waitlists(self,db_manager):
        self.wait_list_courses_status(db_manager)
        course_id = input("Enter course ID: ")
        course = db_manager.get_course(course_id)
        if not course:
            print("Course not found. Check the course ID and try again.")
            return
        print(f"--- Waitlist for Course: {course['name']} ---")
        print('\n')
        waitlists = db_manager.get_waitlist(course_id)
        if not waitlists:
            print("No students in the waitlist.")
        else:
            for i, student in enumerate(waitlists, start=1):
                        print(f"{i}. {student['student_name']} | Registered: {student['registered_at']}")
            print('\n')
        option = view_manage_waitlist_options()
        print('\n')
        student = Student(
            id = waitlists[0]['student_id'],
            name = waitlists[0]['student_name'],
        )
        if option == '1':
            course_enrollment = CourseEnrollment(
                student_id = student.id,
                course_id = course_id
            )
            db_manager.insert_child_to_course(course_enrollment)
            db_manager.remove_student_from_waitlist(student.id,course_id)
            print("Student assigned to the course successfully.")
            print('\n')
            return True
        elif option == '2':
            db_manager.remove_student_from_waitlist(student.id,course_id)
            print("Student removed from the waitlist.")
            print('\n')
            return True
        elif option == '3':
            return True
        else:
            print("Invalid option. Please try again.")
            return False



# Manages tasks for employees.
# - Prompts the user with task management options and performs actions based on the selected option:
#   1. Create a new task and assign it to an employee:
#      - Retrieves available classrooms and prompts the user to select one.
#      - Collects issue details and creates a new Task object.
#      - Saves the task to the database and assigns it to a specific employee.
#      - Prints a success message upon successful assignment.
#   2. View all tasks:
#      - Retrieves and displays a list of all tasks, including their ID, description, status, and assigned employee.
#      - Prints a message if no tasks are found.
#   3. Update task status:
#      - Prompts the user to input a task ID and a new status (Completed/In Progress/Pending).
#      - Updates the task status in the database and prints a success message.
#   4. Exit the task management menu.
# - Returns a success or failure status for the operation based on the selected option.
    def manage_employee_tasks(self,db_manager):
        option = view_manage_employy_tasks_options()
        print('\n')
        if option == '1':
            class_rooms = db_manager.get_class_rooms()
            for room in class_rooms:
                print(f"{room['id']}. {room['name']} - ({room['capacity']}) - classroom id =  {room['id']}")
            class_room_id = input("Enter classroom id from the above options: : ").strip()
            issue = input("Enter the issue description: ")
            new_issue = Task(
                description = issue,
                status = "Pending",
                class_room_id = class_room_id
            )
            task_id = db_manager.create_task_issue(new_issue)
            employee_id = input("Enter employee ID: ")
            db_manager.assign_task_to_employee(employee_id,task_id)
            print("Task assigned to employee successfully.")
            return True
        elif option == '2':
            tasks = db_manager.get_all_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. taskId: {task['id']} | {task['description']} | Status: {task['status']} | assigned to: {task['employee_name']}")
            print('\n')
            return True
        elif option == '3':
            task_id = input("Enter task ID: ")
            new_status = input("Enter new status: (Completed/In progress/Pending)").strip()
            db_manager.update_task_status(task_id,new_status)
            print("Task status updated successfully.")
            print('\n')
            return True
        elif option == '4':
            return True
        else:
            print("Invalid option. Please try again.")
            return False



# Manages financial reports for the system.
# - Retrieves total income details from the database and displays them using the view_income_report function.
# - Retrieves teacher salaries and displays them using the view_teachers_salaries function.
# - Retrieves employee salaries and displays them using the view_employees_salaries function.
# - Calculates the total expenses by summing teacher and employee salaries.
# - Prints the total outcome (expenses) and the net balance (income minus expenses).
    def manage_financial_reports(self,db_manager):
        income_details = db_manager.get_total_income()
        total_income = view_income_report(income_details)
        teacher_salaries = db_manager.get_teachers_salary()
        total_teachers_outcome = view_teachers_salaries(teacher_salaries)
        employees_salaries = db_manager.get_employees_salary()
        total_employees_outcome = view_employees_salaries(employees_salaries)
        total_outcome = total_teachers_outcome + total_employees_outcome
        print(f"\nTotal Outcome: {total_outcome:.2f}\n")
        # Print net balance
        net_balance = total_income - total_outcome
        print(f"Net Balance: {net_balance:.2f}")

    def add_new_classroom(self,db_manager):
        classroom_name = input("Enter classroom name: ")
        capacity = input("Enter classroom capacity: ")
        location = input("Enter classroom location: ")
        new_class_room = ClassRoom(
            name = classroom_name,
            capacity = capacity,
            location =  location
        )

        db_manager.create_classroom(new_class_room)
        print("Classroom added successfully.")    

    def wait_list_courses_status(self,db_manager):
        wait_list_courses = db_manager.waitlist_course_status()
        if not wait_list_courses:
            print("No courses with waitlist found.")
        else:
            for i, course in enumerate(wait_list_courses, start=1):
                if(course['registered_students'] >= 5):
                    print(f"{course['registered_students']} Registered students for : {course['name']} | is grater than 5 , the system reccomend to open a new course ")
                    print('\n')
        return True

# Displays options for managing a course waitlist.
# - Option 1: Assign a student from the waitlist to the course.
# - Option 2: Remove a student from the waitlist.
# - Option 3: Return to the main menu.
# Prompts the user to choose an option and returns the selected input.
# helper functions
def view_manage_waitlist_options():
    print("Enter '1' to assign a student to the course")
    print("Enter '2' to remove a student from the waitlist")
    print("Enter '3' to return to the main menu")
    return input("Choose an option: ")



# Displays options for managing employee tasks.
# - Option 1: Assign a new task to an employee.
# - Option 2: View all tasks in the system.
# - Option 3: Update the status of an existing task.
# - Option 4: Return to the main menu.
# Prompts the user to choose an option and returns the selected input.
def view_manage_employy_tasks_options():
    print("1. Assign task to employee")
    print("2. View all tasks")
    print("3. Update task status")
    print("4. Return to main menu")
    return input("Choose an option: ")



# Displays the income report and calculates the total income.
# - Iterates through the provided income_details, which include payments made by parents.
# - For each payment, displays the parent's name, payment amount, and description.
# - Calculates and prints the total income from all payments.
# - Returns the calculated total income.
def view_income_report(income_details):
    total_income = 0
    print("\nIncome Details:")
    for payment in income_details:
        total_income += payment["amount"]
        print(f"Parent: {payment['parent_name']} | Amount: {payment['amount']:.2f} | Description: {payment['description']}")
    print(f"Total Income: {total_income:.2f}\n")
    return total_income



# Displays teacher salary details and calculates the total expense for teacher salaries.
# - Iterates through the provided teacher_salaries, which include teacher names and their respective salaries.
# - For each teacher, displays the teacher's name and salary amount.
# - Calculates and prints the total expense for all teacher salaries.
# - Returns the calculated total expense.
def view_teachers_salaries(teacher_salaries):
    total_outcome = 0
    print("Outcome Details:")
    print("\nTeacher Salaries:")
    for teacher in teacher_salaries:
        total_outcome += teacher["salary"]
        print(f"Teacher: {teacher['teacher_name']} | Salary: {teacher['salary']:.2f}")
    print('total teachers salaries:',total_outcome,'\n')
    return total_outcome



# Displays employee salary details and calculates the total expense for employee salaries.
# - Iterates through the provided employee_salaries, which include employee names and their respective salaries.
# - For each employee, displays the employee's name and salary amount.
# - Calculates and prints the total expense for all employee salaries.
# - Returns the calculated total expense.
def view_employees_salaries(employee_salaries):
    total_outcome = 0
    print("\nEmployee Salaries:")
    for employee in employee_salaries:
        total_outcome += employee["salary"]
        print(f"Employee: {employee['employee_name']} | Salary: {employee['salary']:.2f}")
    print('total employees salaries:',total_outcome,'\n')
    return total_outcome

