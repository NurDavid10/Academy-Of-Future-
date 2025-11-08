# Represents a queue entry for a student waiting for a course.
# - Initializes the queue entry with an optional ID, course ID, student ID, and registration timestamp.
# - Stores information related to a student's position in the waitlist for a course.
class Queue:
    """Represents a queue entry with an ID, course ID, student ID, and registration timestamp."""

    def __init__(self, id=None, course_id=None, student_id=None, registered_at=None):
        self._id = id
        self._course_id = course_id
        self._student_id = student_id
        self._registered_at = registered_at



# Property getter for the private _id attribute.
# Allows read-only access to the unique identifier of the queue entry.
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



# Property getter for the private _course_id attribute.
# Allows read-only access to the course ID associated with the queue entry.
    @property
    def course_id(self):
        return self._course_id



# Property setter for the private _course_id attribute.
# - Validates that the value is an integer or None.
# - Raises a ValueError if the validation fails.
    @course_id.setter
    def course_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Course ID must be an integer or None.")
        self._course_id = value



# Property getter for the private _student_id attribute.
# Allows read-only access to the student ID associated with the queue entry.
    @property
    def student_id(self):
        return self._student_id



# Property setter for the private _student_id attribute.
# - Validates that the value is an integer or None.
# - Raises a ValueError if the validation fails.
    @student_id.setter
    def student_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Student ID must be an integer or None.")
        self._student_id = value



# Property getter for the private _registered_at attribute.
# Allows read-only access to the registration timestamp of the queue entry.
    @property
    def registered_at(self):
        return self._registered_at



# Property setter for the private _registered_at attribute.
# - Sets the value of the registration timestamp.
# - Assumes validation or conversion of the value is handled elsewhere.
    @registered_at.setter
    def registered_at(self, value):
        self._registered_at = value  # Assume validation/conversion is handled elsewhere
