# Represents an Employee, inheriting from the User class.

# Attributes:
# - id: Unique identifier for the employee (inherited from User).
# - name: Name of the employee (inherited from User).
# - email: Email address of the employee (inherited from User).
# - password: Password for the employee (inherited from User).
# - salary: The salary of the employee.
from classes.task import Task
from classes.user import User

class Employee(User):
    """Represents an Employee."""
    def __init__(self, id=None, name="", email="", salary=0.0, password="111"):
        super().__init__(id, name, email, "employee", password)
        self._salary = salary


# Property getter for the private _salary attribute.
# Allows read-only access to the salary of the employee.
    @property
    def salary(self):
        return self._salary


# Property setter for the private _salary attribute.
# - Validates that the salary is non-negative.
# - Raises a ValueError if the value is less than 0.
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value


# Fetches and displays all tasks assigned to the employee.
# - Uses the employee's ID to retrieve tasks from the database.
# - Prints each task's ID, description, and status.
    def view_my_tasks(self,db_manager):
        tasks = db_manager.fetch_all_employee_tasks(self.id)
        for task in tasks:
            print(f"taskId: {task['id']} | task description: {task['description']} | task status: {task['status']}")    


# Updates the status of a task assigned to the employee.
# - Prompts the user to input the task ID and new status.
# - Verifies that the task is assigned to the employee using the database.
# - Updates the task status in the database if valid and prints the result.
# - Handles and displays any errors that occur during the process.
    def update_task_status(self,db_manager):
        try:
            # קבלת קלט מהמשתמש
            task_id = input("Enter the task ID: ")
            is_assigned = db_manager.check_task_assignee(task_id,self.id)
            if not is_assigned:
                print("Task not assigned to you")
                return
            status = input("Enter the new status (Completed\ In progress): ")
            is_update = db_manager.update_task_status(task_id,status)
            if is_update:
                print("Task updated successfully")
            else:
                print("Task not updated")
        except Exception as e:
            print(f"An error occurred while making the payment: {e}")


# Reports an issue related to a classroom.
# - Retrieves and displays all available classrooms from the database.
# - Prompts the user to select a classroom ID and enter an issue description.
# - Creates a new task with the issue details and sets its status to "Pending."
# - Saves the task to the database and displays the task ID upon successful creation.
# - Handles and displays any errors that occur during the process.
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