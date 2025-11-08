# Represents a task with details like ID, description, assigned employee, status, classroom ID, and last updated timestamp.
# - Initializes the task object with optional values for ID, description, employee assignment, status, classroom ID, and last updated timestamp.
# - Stores information related to a task's details and status.
class Task:
    """Represents a task with an ID, description, assigned employee, status, classroom ID, and last updated timestamp."""

    def __init__(self, id=None, description="", assigned_to=None, status="Pending", class_room_id=None, updated_at=None):
        self._id = id
        self._description = description
        self._assigned_to = assigned_to
        self._status = status
        self._class_room_id = class_room_id
        self._updated_at = updated_at



# Property getter for the private _id attribute.
# Allows read-only access to the unique identifier of the task.
    @property
    def id(self):
        return self._id



# Property setter for the private _id attribute.
# - Validates that the value is an integer or None.
# - Raises a ValueError if the validation fails.
    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID must be an integer or None.")
        self._id = value



# Property getter for the private _description attribute.
# Allows read-only access to the description of the task.
    @property
    def description(self):
        return self._description



# Property setter for the private _description attribute.
# - Validates that the description is not empty or just whitespace.
# - Raises a ValueError if the validation fails.
    @description.setter
    def description(self, value):
        if not value.strip():
            raise ValueError("Description cannot be empty or whitespace.")
        self._description = value



# Property getter for the private _assigned_to attribute.
# Allows read-only access to the ID of the employee assigned to the task.
    @property
    def assigned_to(self):
        return self._assigned_to



# Property setter for the private _assigned_to attribute.
# - Validates that the value is an integer or None.
# - Raises a ValueError if the validation fails.
    @assigned_to.setter
    def assigned_to(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Assigned to must be an integer or None.")
        self._assigned_to = value



# Property getter for the private _status attribute.
# Allows read-only access to the status of the task.
    @property
    def status(self):
        return self._status



# Property setter for the private _status attribute.
# - Validates that the value is one of the allowed statuses: "Pending", "In Progress", or "Completed".
# - Raises a ValueError if the validation fails.
    @status.setter
    def status(self, value):
        allowed_statuses = ["Pending", "In Progress", "Completed"]
        if value not in allowed_statuses:
            raise ValueError(f"Status must be one of {allowed_statuses}.")
        self._status = value



# Property getter for the private _class_room_id attribute.
# Allows read-only access to the classroom ID associated with the task.
    @property
    def class_room_id(self):
        return self._class_room_id



# Property setter for the private _class_room_id attribute.
# - Validates that the value is an integer or None.
# - Raises a ValueError if the validation fails.
    @class_room_id.setter
    def class_room_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Classroom ID must be an integer or None.")
        self._class_room_id = value



# Property getter for the private _updated_at attribute.
# Allows read-only access to the last updated timestamp of the task.
    @property
    def updated_at(self):
        return self._updated_at



# Property setter for the private _updated_at attribute.
# - Sets the value of the last updated timestamp.
# - Assumes validation or conversion of the value is handled elsewhere.
    @updated_at.setter
    def updated_at(self, value):
        self._updated_at = value  # Assume validation/conversion is handled elsewhere
