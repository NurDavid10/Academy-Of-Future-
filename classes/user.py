# Represents a generic User with attributes such as ID, name, email, role, and password.
# - Initializes the user object with optional values for ID, name, email, role, and password.
# - Stores the user details, with the password being assigned a default value of "111".
# - This class serves as the base for different user types (e.g., teacher, student, parent).
import re
class User:
    def __init__(self, id=None, name="", email="", role="", password="111"):
        self._id = id
        self._name = name
        self._email = email
        self._role = role
        self._password = password



# Property getter for the private _id attribute.
# Allows read-only access to the unique identifier of the user.
    @property
    def id(self):
        return self._id



# Property setter for the private _id attribute.
# - Validates that the value is an integer.
# - Raises a ValueError if the validation fails.
    @id.setter
    def id(self, value):
        if isinstance(value, int):
            self._id = value
        else:
            raise ValueError("User ID must be a number.")



# Property getter for the private _name attribute.
# Allows read-only access to the name of the user.
    @property
    def name(self):
        return self._name



# Property setter for the private _name attribute.
# - Validates that the name starts with an uppercase letter, contains at least 2 letters, and does not include numbers.
# - Raises a ValueError if the validation fails.
    @name.setter
    def name(self, value):
        if re.match(r"^[A-Z][a-zA-Z]{1,}$", value):
            self._name = value
        else:
            raise ValueError(
                "Username must start with an uppercase letter, contain at least 2 letters, "
                "and not include numbers."
            )



# Property getter for the private _email attribute.
# Allows read-only access to the email of the user.
    @property
    def email(self):
        return self._email



# Property setter for the private _email attribute.
# - Validates that the email follows the standard email format using a regular expression.
# - Raises a ValueError if the email format is invalid.
    @email.setter
    def email(self, email):
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format.")
        self._email = email



# Property getter for the private _role attribute.
# Allows read-only access to the role of the user (e.g., 'teacher', 'student').
    @property
    def role(self):
        return self._role



# Property getter for the private _password attribute.
# Allows read-only access to the user's password.
    @property
    def password(self):
        return self._password



# Property setter for the private _password attribute.
# - Validates that the password meets the following criteria:
#   - At least 8 characters long.
#   - Contains at least one uppercase letter, one lowercase letter, one number, and one special character.
# - Raises a ValueError if the password doesn't meet the criteria.
    @password.setter
    def password(self, value):
        if re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
            value,
        ):
            self._password = value
        else:
            raise ValueError(
                "Password must be at least 8 characters long, include an uppercase letter, "
                "a lowercase letter, a number, and a special character (!@#$%^&*)."
            )


    def update_password(self,db_manager):
        old_password = input("Please Enter old password: ")
        if old_password == self._password:
            new_password = input("Please Enter new password: ")
            db_manager.update_user_password(self._id, new_password)
        else:
            print("Incorrect old password. Password update failed.")