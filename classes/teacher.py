from classes.task import Task
from classes.user import User
from datetime import date



# Represents a Teacher, inheriting from the User class.
# Initializes a teacher with ID, name, email, specialization, hire date, salary, and password.
# The role is automatically set to "teacher".
# Stores specialization, hire date (default to current date), and salary as private attributes for the teacher.
class Teacher(User):
    """Represents a Teacher."""
    def __init__(self, id=None, name="", email="", specialization="", hire_date=None, salary=0.0,password="111"):
        super().__init__(id, name, email, "teacher", password)
        self._specialization = specialization
        self._hire_date = hire_date or date.today()
        self._salary = salary



# Property getter for the private _specialization attribute.
# Allows read-only access to the specialization of the teacher.
    @property
    def specialization(self):
        return self._specialization



# Property setter for the private _specialization attribute.
# - Sets the value of the teacher's specialization.
# - No validation is performed on the value.
    @specialization.setter
    def specialization(self, value):
        self._specialization = value



# Property getter for the private _hire_date attribute.
# Allows read-only access to the hire date of the teacher.
    @property
    def hire_date(self):
        return self._hire_date



# Property setter for the private _hire_date attribute.
# - Validates that the value is a valid date object.
# - Raises a ValueError if the validation fails.
    @hire_date.setter
    def hire_date(self, value):
        if not isinstance(value, date):
            raise ValueError("Hire date must be a valid date object.")
        self._hire_date = value



# Property getter for the private _salary attribute.
# Allows read-only access to the salary of the teacher.
    @property
    def salary(self):
        return self._salary



# Property setter for the private _salary attribute.
# - Validates that the salary is non-negative.
# - Raises a ValueError if the validation fails.
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value



# Fetches and displays the courses assigned to the teacher.
# - Retrieves the list of courses for the teacher from the database.
# - Prints the course name and associated classroom name for each course.
    def view_teacher_courses(self,db_manager):
        teacher_courses = db_manager.fetch_courses_for_teacher(self.id)
        for course in teacher_courses:
            print(f"Course Name: {course['name']}, Class Room: {course['class_room_name']}")



# Allows the teacher to enter grades for students in a specific course.
# - Prompts the teacher to input the course ID and retrieves the list of students enrolled in the course.
# - For each student, displays their current grade and asks the teacher to input a new grade.
# - Updates the student's grade in the database.
# - Prints a success message after entering the grades or an error message if no students are found or the course is not assigned to the teacher.
    def enter_grades(self, db_manager):
        print("Enter Grades")
        course_id = input("Enter course id: ")
        students = db_manager.fetch_students_in_course(course_id, self.id)
        if students:
            for student in students:
                grade = input(f"Student id: {student['student_id']} | name {student['student_name']} | current grade: {student ['current_grade']} | Enter new grade: ").strip()
                db_manager.set_student_grade(student['student_id'],course_id,grade)

            print("Grade entered successfully")
        else:
            print("No students found for the given course id or the course isn't assigned to you.")



# Allows the teacher to report an issue with a classroom.
# - Retrieves and displays the list of available classrooms.
# - Prompts the teacher to select a classroom and enter a description of the issue.
# - Creates a new task with the issue details and sets its status to "Pending."
# - Saves the issue to the database and prints a success message with the task ID.
# - Handles any exceptions that occur during the process and prints an error message.
    def report_class_issue(self,db_manager):
        try:
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
            if task_id:
                print(f"Task created successfully with ID: {task_id}")
        except Exception as e:
            print(f"An error occurred while making the payment: {e}")