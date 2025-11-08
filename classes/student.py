# Represents a Student, inheriting from the User class.
# Initializes a student with ID, name, email, age, grade level, parent ID, and password.
# The role is automatically set to "student".
# Stores age, grade level, and parent ID as private attributes for the student.
from classes.user import User
from datetime import datetime,timedelta

class Student(User):
    """Represents a Student."""
    def __init__(self, id=None, name="", email="", age=0, grade_level="", parent_id=None, password="111"):
        super().__init__(id, name, email, "student", password)
        self._age = age
        self._grade_level = grade_level
        self._parent_id = parent_id



# Property getter for the private _age attribute.
# Allows read-only access to the age of the student.
    @property
    def age(self):
        return self._age



# Property setter for the private _age attribute.
# - Validates that the value is a positive integer or float between 1 and 18.
# - Raises a ValueError if the validation fails.
    @age.setter
    def age(self, value):
        if isinstance(value, (int, float)) and (0 < value <= 18):
            self._age = value
        else:
            raise ValueError("Age must be a positive integer.")



# Property getter for the private _grade_level attribute.
# Allows read-only access to the grade level of the student.
    @property
    def grade_level(self):
        return self._grade_level



# Property setter for the private _grade_level attribute.
# - Validates that the value is a number between 0 and 100.
# - Raises a ValueError if the validation fails.
    @grade_level.setter
    def grade_level(self, value):
        if isinstance(value, (int, float)) and (0 <= value <= 100):
            self._grades = value
        else:
            raise ValueError("Grades must be a number between 0 and 100.")



# Property getter for the private _parent_id attribute.
# Allows read-only access to the parent ID associated with the student.
    @property
    def parent_id(self):
        return self._parent_id



# Property setter for the private _parent_id attribute.
# - Validates that the value is an integer or None.
# - Raises a ValueError if the validation fails.
    @parent_id.setter
    def parent_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Parent ID must be an integer or None.")
        self._parent_id = value



# Fetches, groups, and displays the course schedule for the student.
# - Retrieves courses associated with the student from the database.
# - If no courses are found, it prints a message indicating this.
# - Groups the courses by day of the week using the group_courses_by_day function.
# - Formats the grouped courses into a readable schedule format using the format_course_schedule function.
# - Prints the formatted schedule for the student.
    def view_schedule(self,db_manager):
        """Main function to fetch, group, and display the course schedule."""
        # Step 1: Fetch courses for the student
        courses = db_manager.fetch_courses_for_student(self.id)
        if not courses:
            print("No courses found for this student.")
            return

        # Step 2: Group courses by the day of the week
        schedule_by_day = group_courses_by_day(courses)
        # print(schedule_by_day)
        # Step 3: Format the schedule for display
        formatted_schedule = format_course_schedule(schedule_by_day)

        # Step 4: Print the schedule
        print(formatted_schedule)



# Fetches and displays the student's grades for each course.
# - Retrieves the grades for the student from the database.
# - For each course, it checks if the grade is available; if not, it displays "In Progress".
# - Prints the course name along with the corresponding grade or "In Progress" if no grade is assigned.
    def view_grades(self,db_manager):
        grades = db_manager.fetch_grades(self.id)
        for course in grades:
            course_name = course['course_name']
            grade = course['grade']
            grade_display = "In Progress" if grade is None else grade
            print("Course: ", course_name, "| Grade: ", grade_display)



# Groups courses by the day of the week based on their scheduled date.
# - Iterates over each course and checks its `course_date`, which can be a datetime or string.
# - Converts the `course_date` to a `datetime.date` object if it's a string or datetime.
# - Extracts the day of the week from the date and groups courses by that day.
# - Stores the grouped courses (course name, time, classroom) in a dictionary, where keys are days of the week.
# - Returns the dictionary of courses grouped by day.
# Helper functions      
def group_courses_by_day(courses):
    """Group courses by the day of the week."""
    schedule_by_day = {}
    for course in courses:
        try:
            # Use the course_date directly if it's already a datetime.date object
            if isinstance(course['course_date'], datetime):
                course_date = course['course_date'].date()
            elif isinstance(course['course_date'], str):
                course_date = datetime.strptime(course['course_date'], '%Y-%m-%d').date()
            else:
                course_date = course['course_date']  # Assume it's a datetime.date object

            # Get the day of the week
            day_of_week = course_date.strftime('%A')

            # Add the course to the respective day
            if day_of_week not in schedule_by_day:
                schedule_by_day[day_of_week] = []

            schedule_by_day[day_of_week].append({
                "course_name": course['course_name'],
                "course_time": course['course_time'],
                "class_room_name": course['class_room_name']
            })
        except Exception as e:
            print(f"An error occurred while grouping courses: {e}")
    return schedule_by_day



# Formats the course schedule for display in a readable format.
# - Iterates through the `schedule_by_day` dictionary, which contains courses grouped by day.
# - For each course, if the course time is a `timedelta`, it converts it to a formatted string in "HH:MM AM/PM" format.
# - If the course time is invalid, it raises a ValueError.
# - Adds course details such as name, time, and classroom to the formatted schedule.
# - The final formatted schedule is returned as a string, with days and courses neatly displayed.
def format_course_schedule(schedule_by_day):
    """Format the course schedule for display."""
    formatted_schedule = "\n"
    for day, courses in schedule_by_day.items():
        formatted_schedule += f"{day}:\n"  # Add the day header
        for course in courses:
            try:
                # Convert timedelta to time
                if isinstance(course['course_time'], timedelta):
                    total_seconds = course['course_time'].total_seconds()
                    hours = int(total_seconds // 3600)
                    minutes = int((total_seconds % 3600) // 60)
                    # Format the time as AM/PM
                    time_formatted = datetime.strptime(f"{hours:02}:{minutes:02}", "%H:%M").strftime("%I:%M %p")
                else:
                    raise ValueError("Invalid time format")

                # Add formatted course details to the schedule
                formatted_schedule += f"- {course['course_name']} | {time_formatted} | Room {course['class_room_name']}\n"
            except Exception as e:
                print(f"An error occurred while formatting course: {e}")
        formatted_schedule += "\n"  # Add a blank line between days
    return formatted_schedule