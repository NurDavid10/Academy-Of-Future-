from classes.class_room import ClassRoom

# Represents a Course in the system.

# Attributes:
# - id: Unique identifier for the course (default: None).
# - name: Name or title of the course (default: empty string).
# - description: Detailed description of the course content (default: empty string).
# - teacher_id: ID of the teacher assigned to the course (default: None).
# - max_capacity: Maximum number of students allowed in the course (default: 30).
# - class_room_id: ID of the classroom associated with the course (default: None).
class Course:

    """Represents a Course."""
    def __init__(self, id=None, name="", description="", teacher_id=None, max_capacity=30,class_room_id=None):
        self._id = id
        self._name = name
        self._description = description
        self._teacher_id = teacher_id
        self._max_capacity = max_capacity
        self._class_room_id = class_room_id  # A ClassRoom instance or None


# Property getter for the private _id attribute.
# Allows read-only access to the unique identifier of the course.
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


# Property getter for the private _name attribute.
# Allows read-only access to the name of the course.
    @property
    def name(self):
        return self._name


# Property setter for the private _name attribute.
# - Validates that the value is not empty.
# - Raises a ValueError if the validation fails.
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Course name cannot be empty.")
        self._name = value


# Property getter for the private _description attribute.
# Allows read-only access to the course's description.
    @property
    def description(self):
        return self._description


# Property setter for the private _description attribute.
# - Directly assigns the provided value to the description.
# - Can be extended with validation or additional logic as needed.
    @description.setter
    def description(self, value):
        self._description = value


# Property getter for the private _teacher_id attribute.
# Allows read-only access to the ID of the teacher assigned to the course.
    @property
    def teacher_id(self):
        return self._teacher_id


# Property setter for the private _teacher_id attribute.
# - Validates that the value is an integer or None.
# - Raises a ValueError if the validation fails.
    @teacher_id.setter
    def teacher_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Teacher ID must be an integer or None.")
        self._teacher_id = value


# Property getter for the private _max_capacity attribute.
# Allows read-only access to the maximum number of students allowed in the course.
    @property
    def max_capacity(self):
        return self._max_capacity


# Property setter for the private _max_capacity attribute.
# - Validates that the value is an integer and at least 1.
# - Raises a ValueError if the validation fails.
    @max_capacity.setter
    def max_capacity(self, value):
        if value < 1:
            raise ValueError("Max capacity must be at least 1.")
        self._max_capacity = value


# Property getter for the private _classroom attribute.
# Allows read-only access to the classroom ID associated with the course.
# Note: Consider renaming the private attribute to _class_room_id for consistency.
    @property
    def class_room_id(self):
        return self._classroom


# Property setter for the private _class_room_id attribute.
# - Validates that the value is an integer or None.
# - Raises a ValueError if the validation fails.
    @class_room_id.setter
    def class_room_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Classroom must be an integer of ClassRoom or None.")
        self._class_room_id = value