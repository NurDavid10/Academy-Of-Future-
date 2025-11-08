from databaseManager.database_manager import DatabaseManager
import sys
from classes.all_classes import *



# Handles manager menu actions based on user input.
# 1: Add new user, 2: Create new course, 3: Manage financial reports,
# 4: Manage waitlists, 5: Manage employee tasks, 6: Logout.
# Default: Displays an error message and exits for invalid options.
def manager_menu(option,current_manager: Manager,db_manager: DatabaseManager):
    match option:
        case 1:
            print("--- Add New User ---")
            current_manager.add_new_user(db_manager)
        case 2:
            print("--- Create New Course ---")
            current_manager.create_new_course(db_manager)
        case 3:
            print("--- Manage Financial Reports ---")
            current_manager.manage_financial_reports(db_manager)
        case 4:
            print("--- Manage Waitlists ---")
            return_to_main = current_manager.manage_waitlists(db_manager)
            if return_to_main:
                managerMain(current_manager)
        case 5:
            print("--- Manage Employee Tasks ---")
            return_to_main = current_manager.manage_employee_tasks(db_manager)
            if return_to_main:
                managerMain(current_manager)
        case 6:
            print("--- Add New Class Room ---")
            current_manager. add_new_classroom(db_manager)
            
        case 7:
            print("--- Update password ---")
            current_manager.update_password(db_manager)        
        case 8:
            print("--- Logging out ---")
            sys.exit()

        case _:
            print("Wrong option ")
            sys.exit()



# Displays a menu of options for managers and returns the user's choice.
# Options: 1-Add user, 2-Create course, 3-Manage financials,
# 4-Manage waitlists, 5-Manage tasks, 6-Logout.
def list_options():
    print("1. Add New User")
    print("2. Create New Course")
    print("3. Manage Financial Reports")
    print("4. Manage Waitlists")
    print("5. Manage Employee Tasks")
    print("6. Add New Class Room")
    print("7. update password")
    print("8. Logout")
    return input("Choose an option: ")



# Main function for manager operations.
# - Displays menu, initializes database and manager objects.
# - Passes user choice, manager, and database manager to the menu handler.
def managerMain(user):
    db_manager = DatabaseManager()
    current_manager = Manager(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password
    )
    current_manager.wait_list_courses_status(db_manager)
    choice = list_options()
    manager_menu(int(choice),current_manager,db_manager)