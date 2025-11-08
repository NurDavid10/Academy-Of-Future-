# Main script for handling user login and navigating to the appropriate menu based on the user role.
# - First, the user is prompted whether to seed the database; if 'y' is entered, it calls the `initiationMain` function to seed the database.
# - The user is then prompted to log in using `loginMain`, which returns a user object if the login is successful.
# - Based on the user's role (manager, parent, teacher, student, or employee), the corresponding menu function is called (e.g., `managerMain` for managers).
# - If the role is invalid or not recognized, the script exits.
# - If the login is unsuccessful, an error message is displayed.
import sys
import dotenv
import os
dotenv.load_dotenv()
sys.path.append(os.environ["path"])

from employeeMenu.employeeMenu import employeeMain
from parentsMenu.parentsMenu import parentMain
from studentMenu.studentMenu import studentMain
from teacherMenu.teacherMenu import teacherMain
from initiation.initiationMain import initiationMain
from login.loginMain import loginMain
from managerMenu.managerMenu import managerMain

def user_menu(user):
    match user.role:
        case 'manager':
            print("--- Manager Menu ---")
            managerMain(user)
        case 'parent':
            print("--- Parent Menu ---")
            parentMain(user)
        case 'teacher':
            print("--- Teacher Menu ---")
            teacherMain(user)
        case 'student':
            print("--- Student Menu ---")
            studentMain(user)
        case 'employee':
            print("--- Employee Menu ---")   
            employeeMain(user) 
        case _:
            print("Invalid role")
            sys.exit()

if __name__ == "__main__":
    seed = input("Do you want to seed the database? (y/n): ").strip().lower()
    if(seed == 'y'):
        initiationMain()
            
    user = loginMain()
    if user is not None:
        user_role = user.role
        print("Login successful! Welcome, ", user.name, '(Role: ' + user_role + ')')
        user_menu(user)
    
    else:
        print("Invalid email or password")
