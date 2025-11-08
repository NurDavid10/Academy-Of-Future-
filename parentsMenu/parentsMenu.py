from classes.parent import Parent
import sys

from databaseManager.database_manager import DatabaseManager


# Handles parent menu actions based on user input.
# 1: Register a child, 2: View children's progress, 3: Make a payment,
# 4: Check waitlist status, 5: Logout.
# Default: Displays 'Welcome guest' for invalid options.
def parent_menu(option,db_manager: DatabaseManager,current_parent: Parent):
    match option:
        case 1:
            print("--- Register a child ---")
            current_parent.register_child_to_course(db_manager)
        case 2:
            print("--- View my childern's progress ---")
            current_parent.view_children_progress(db_manager)
        case 3:
            print("--- Make a payment ---")
            current_parent.make_payment(db_manager)
        case 4:
            print("--- Check Waitlist Status ---")
            current_parent.check_waitlist_status(db_manager)
        case 5:
            print("--- Update password ---")
            current_parent.update_password(db_manager) 
        case 6:
            print("--- Loggin out ---")
            sys.exit() 
        case _:
            print("Welcome guest")



# Displays a menu of options for parents and returns the user's choice.
# Options: 1-Register child, 2-View progress, 3-Make payment, 4-Check waitlist, 5-Logout.
def list_options():
    print("1. Register a child to a course")
    print("2. View my childern's progress")
    print("3. Make a payment")
    print("4. Check Waitlist Status")
    print("5. Update password")
    print("6. Logout")
    return input("Choose an option: ")



# Main function for parent operations.
# - Displays menu, initializes database and parent objects.
# - Passes user choice, parent, and database manager to the menu handler.
def parentMain(user):
    choice = list_options()
    db_manager = DatabaseManager()
    current_parent = Parent(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password
    )
    parent_menu(int(choice),db_manager,current_parent)