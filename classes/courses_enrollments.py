# Represents a student's enrollment in a course.

# Attributes:
# - id: Unique identifier for the enrollment record (default: None).
# - course_id: ID of the course associated with the enrollment (default: None).
# - student_id: ID of the student associated with the enrollment (default: None).
# - grade: Grade achieved by the student in the course (default: None).
class CourseEnrollment:
    """Represents a student's enrollment in a course."""
    def __init__(self, id=None, course_id=None, student_id=None, grade=None):
        self._id = id
        self._course_id = course_id
        self._student_id = student_id
        self._grade = grade


# Property getter for the private _id attribute.
# Allows read-only access to the unique identifier of the enrollment record.
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
# Allows read-only access to the ID of the course associated with the enrollment.
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
# Allows read-only access to the ID of the student associated with the enrollment.
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


# Property getter for the private _grade attribute.
# Allows read-only access to the grade associated with the course enrollment.
    @property
    def grade(self):
        return self._grade


# Property setter for the private _grade attribute.
# - Validates that the grade is a number between 0.0 and 100.0, or None.
# - Raises a ValueError if the validation fails.
    @grade.setter
    def grade(self, value):
        if value is None or (value < 0.0 or value > 100.0):
            raise ValueError("Grade must be between 0.0 and 100.0 or None")
        self._grade = value