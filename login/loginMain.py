import sys
from databaseManager.database_manager import DatabaseManager
import dotenv
import os
dotenv.load_dotenv()
sys.path.append(os.environ["path"])
from classes.user import User



# Prompts the user to input their email and password.
# Returns a dictionary with keys 'email' and 'password'.
def getUserInput():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    return {"email": email, "password":password}



# Displays the welcome page with options to Login or Exit.
# Returns the user's choice as a string.
def welcome_page():
    print("Welcome to Learning Center System")
    print("1. Login")
    print("2. Exit")
    return input("Enter your choice: ")



# Handles the user's choice from the welcome page.
# - Exits the system if choice is '2' or invalid.
# - Assumes valid choice ('1') will be processed elsewhere.
def handle_choice (choice):
    if (choice == "2"):
        print("--- Exiting ---")
        sys.exit()
    if (choice != "1"):
        print("Invalid choice")
        sys.exit()



# Handles the user login process.
# - Displays the welcome page and validates the user's choice.
# - Retrieves user details from the database and checks password validity.
# - Returns the current user object if login is successful, otherwise returns None.
def loginMain():
    choice = welcome_page()
    handle_choice(choice)
    db_manager = DatabaseManager()
    userInput = getUserInput()
    user = db_manager.get_user(userInput['email'])

    if  user is not None:
        current_user = User(
            id=user["id"],
            name=user["name"],
            email=user["email"],
            password=user["password"],
            role=user["role"]
        )
        print("User is found")
        if current_user.password == userInput['password']:
            print("Password is correct")
            return (current_user)
        else:
            print("Password is incorrect")
            return None
    else:
        print("User is not found")
        return None

