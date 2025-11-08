import sys
from classes.student import Student

from databaseManager.database_manager import DatabaseManager


# Handles student menu actions based on user input.
# 1: View schedule, 2: View grades, 3: Logout.
# Default: Displays 'Welcome guest' for invalid options.
def student_menu(option,current_student: Student,db_manager: DatabaseManager):
    match option:
        case 1:
            print("--- View my Schedule ---")
            current_student.view_schedule(db_manager)
        case 2:
            print("--- View my Grades  ---")
            current_student.view_grades(db_manager)
        case 3:
            print("--- Update password  ---")
            current_student.update_password(db_manager)
        case 4:
            print("--- Loggin out ---")
            sys.exit() 
        case _:
            print("Welcome guest")



# Displays a menu of options for the student and returns the user's choice.
# Options: 1-View schedule, 2-View grades, 3-Logout.
def list_options():
    print("1. View my Schedule")
    print("2. View my grades")
    print("3. Update password")
    print("4. Logout")
    return input("Choose an option: ")



# Main function for student operations.
# - Displays menu, initializes database and student objects.
# - Passes user choice, student, and database manager to the menu handler.
def studentMain(user):
    choice = list_options()
    db_manager = DatabaseManager()
    current_student = Student(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password
    )
    student_menu(int(choice),current_student,db_manager)