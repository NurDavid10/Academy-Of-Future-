import sys
from classes.teacher import Teacher
from databaseManager.database_manager import DatabaseManager


# Handles teacher menu actions based on user input.
# 1: View courses, 2: Enter grades, 3: Report issues, 4: Logout.
# Default: Displays 'Welcome guest' for invalid options.

def teacher_menu(option,current_teacher: Teacher,db_manager: DatabaseManager):
    match option:
        case 1:
            print("--- view teacher Courses ---")
            current_teacher.view_teacher_courses(db_manager)
        case 2:
            print("--- Enter Gardes  ---")
            current_teacher.enter_grades(db_manager)
        case 3:
            print("--- report class issue ---")   
            current_teacher.report_class_issue(db_manager) 
        case 4:
            print("--- Update password ---")   
            current_teacher.update_password(db_manager) 
        case 5:
            print("--- Loggin out ---")
            sys.exit() 
        case _:
            print("Welcome guest")



# Displays a menu of options and returns the user's choice.
# Options: 1-View courses, 2-Enter grades, 3-Report issue, 4-Logout.

def list_options():
    print("1. View my Courses ")
    print("2. Enter Grades for students") 
    print("3. report class issue")
    print("4. Update password")
    print("5. Logout")
    return input("Choose an option: ")



# Main function for teacher operations.
# - Displays menu, initializes database and teacher objects.
# - Passes user choice, teacher, and database manager to the menu handler.

def teacherMain(user):
    choice = list_options()
    db_manager = DatabaseManager()
    current_teacher = Teacher(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password
    )
    teacher_menu(int(choice),current_teacher,db_manager)