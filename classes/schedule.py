# Represents a schedule for a course with details like course ID, teacher ID, date, time, and classroom ID.
# - Initializes the schedule object with optional values for ID, course ID, teacher ID, date, time, and classroom ID.
# - Stores information about when and where a course is scheduled to take place.
class Schedule:
    """Represents a schedule with an ID, course ID, teacher ID, date, time, and classroom ID."""

    def __init__(self, id=None, course_id=None, teacher_id=None, date=None, time=None, class_room_id=None):
        self._id = id
        self._course_id = course_id
        self._teacher_id = teacher_id
        self._date = date
        self._time = time
        self._class_room_id = class_room_id



# Property getter for the private _id attribute.
# Allows read-only access to the unique identifier of the schedule entry.
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
# Allows read-only access to the course ID associated with the schedule.
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



# Property getter for the private _teacher_id attribute.
# Allows read-only access to the teacher ID associated with the schedule.
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



# Property getter for the private _date attribute.
# Allows read-only access to the date of the schedule.
    @property
    def date(self):
        return self._date



# Property setter for the private _date attribute.
# - Validates that the value is a string in the format 'YYYY-MM-DD' or None.
# - Raises a ValueError if the validation fails.
    @date.setter
    def date(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Date must be a string in the format 'YYYY-MM-DD' or None.")
        self._date = value



# Property getter for the private _time attribute.
# Allows read-only access to the time of the schedule.
    @property
    def time(self):
        return self._time



# Property setter for the private _time attribute.
# - Validates that the value is a string in the format 'HH:MM:SS' or None.
# - Raises a ValueError if the validation fails.
    @time.setter
    def time(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Time must be a string in the format 'HH:MM:SS' or None.")
        self._time = value



# Property getter for the private _class_room_id attribute.
# Allows read-only access to the classroom ID associated with the schedule.
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
