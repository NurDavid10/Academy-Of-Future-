import sys
from classes.employee import Employee
from databaseManager.database_manager import DatabaseManager


# Handles employee menu actions based on the selected option.
# 1: View tasks, 2: Update task status, 3: Report class issue, 4: Logout.
# Default: Displays 'Welcome guest' for invalid options.
def employee_menu(option,current_employee: Employee,db_manager: DatabaseManager):
    match option:
        case 1:
            print("--- View my Tasks ---")
            current_employee.view_my_tasks(db_manager)
        case 2:
            print("--- Update Task Status ---")
            current_employee.update_task_status(db_manager)
        case 3:
            print("--- report class issue ---")   
            current_employee.report_class_issue(db_manager) 
        case 4:
            print("--- Loggin out ---")
            sys.exit() 
        case _:
            print("Welcome guest")



# Displays a menu of options for employees and returns the user's choice.
# Options: 1-View tasks, 2-Update task status, 3-Report issue, 4-Logout.
def list_options():
    print("1. View my Tasks ")
    print("2. update Task status") 
    print("3. report a new issue")
    print("4. Logout")
    return input("Choose an option: ")



# Main function for employee operations.
# - Displays the menu, initializes database and employee objects.
# - Passes user choice, employee, and database manager to the menu handler.
def employeeMain(user):
    choice = list_options()
    db_manager = DatabaseManager()
    current_employee = Employee(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password
    )
    employee_menu(int(choice),current_employee,db_manager)