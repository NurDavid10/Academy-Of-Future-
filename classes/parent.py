# Imports necessary classes and modules:
# - CourseEnrollment: Represents a student's enrollment in a course.
# - User: Represents a generic user in the system.
# - Queue: Represents the waitlist or queue for a course.
# - Payment: Represents payment details made by users (e.g., parents).
# - datetime: Provides utilities for handling date and time operations.
from classes.courses_enrollments import CourseEnrollment
from classes.user import User
from classes.queue import Queue
from classes.payment import Payment
from datetime import datetime



# Represents a Parent, inheriting from the User class.
# Initializes a parent with ID, name, email, and password.
# The role is automatically set to "parent".
class Parent(User):
    """Represents a Parent."""
    def __init__(self, id=None, name="", email="", password="111"):
        super().__init__(id, name, email, "parent", password)



# Registers a child to a course or adds them to the waitlist if the course is full.
# - Prompts the user for the child's ID and the course ID.
# - Checks if the course exists and if the child is already registered or in the waitlist.
# - If the child is not registered and the course has space, the child is enrolled.
# - If the course is full, the child is added to the waitlist.
# - Prints relevant messages based on the action taken (registration or waitlist).
# - Displays the waitlist status if the child is added to the waitlist.
    def register_child_to_course(self,db_manager):
        child_id = input("Enter child id: ")
        course_id = input("Enter course id: ")
        course = db_manager.get_course(course_id)
        is_child_added_to_wait_list = False
        if course is not None:
            course_enrollment = CourseEnrollment(
                        student_id = child_id,
                        course_id = course_id,
                        grade = None,

                    )
            course_capacity = course['max_capacity']
            current_capacity = db_manager.fetch_enrollment_count_for_course(course_enrollment)
            is_child_registered = db_manager.is_child_registered(course_enrollment)
            is_child_in_waitlist = db_manager.is_child_in_waitlist(course_enrollment)
            if (is_child_registered):    
                print('child is already registered')
            elif(is_child_in_waitlist):
                print('child is already in waitlist')
            else:
                if(current_capacity < course_capacity):
                    is_child_added_to_course = db_manager.insert_child_to_course(course_enrollment)
                    if is_child_added_to_course:
                        print(f"Child {child_id} registered to course {course_id}")
                    else:
                        print(f"Something Went Wrong while registering child {child_id} to course {course_id}")
                else:
                    queue_entry = Queue(
                        student_id =child_id,
                        course_id =course_id,
                        registered_at = datetime.now()
                       )
                    is_child_added_to_wait_list = db_manager.add_child_to_waitlist(queue_entry)
                    if is_child_added_to_wait_list:
                        print(f"Course {course['name']} is full. your child has been added to the waitlist")
                    else:
                        print(f"Something went wrong while adding child {child_id} to waitlist")
            if(is_child_added_to_wait_list):
                print("--- Waitlist Status ---")
                course_waitlist = db_manager.get_waitlist(course_id)
                for i, student in enumerate(course_waitlist, start=1):
                    print(f"{i}. {student['student_name']} | Registered: {student['registered_at']}")
    


# Retrieves and returns the progress of children (students) for a parent.
# - Retrieves a list of students associated with the parent using the parent's ID.
# - If no students are found, returns a message indicating no students for the parent.
# - Retrieves course enrollments and waitlist status for the students.
# - Calls a method `build_student_progress` to compile and return the progress data.
    def get_children_progress(self,db_manager):
        """Main function to get children progress for a parent."""
        # Step 1: Retrieve students
        students = db_manager.get_students_by_parent_id(self.id)
        if not students:
            return f"No students found for parent_id {self.id}"

        # Step 2: Get student IDs
        student_ids = [student['student_id'] for student in students]

        # Step 3: Retrieve enrollments and waitlists
        enrollments = db_manager.get_course_enrollments(student_ids)
        waitlists = db_manager.get_waitlist_status(student_ids)

        # Step 4: Build and return the progress data
        return self.build_student_progress(students, enrollments, waitlists)
    


# Combines student data with course enrollments and waitlist status to build a progress report.
# - Iterates through the list of students and for each student, gathers their course enrollments and waitlist information.
# - Adds course names and grades for enrolled courses, and marks the course as "Waitlist" if the student is in the waitlist.
# - Compiles the student’s name along with their courses and status (enrolled or waitlisted) into a dictionary.
# - Returns a list of dictionaries containing each student's progress data.
    def build_student_progress(self,students, enrollments, waitlists):
        """Combine student data with course enrollments and waitlist status."""
        progress = []

        for student in students:
            student_data = {
                "student_name": student['student_name'],
                "courses": []
            }

            # Add course enrollments
            for enrollment in enrollments:
                if enrollment['student_id'] == student['student_id']:
                    student_data["courses"].append({
                        "course_name": enrollment['course_name'],
                        "grade": enrollment.get('grade')
                    })

            # Add waitlist courses
            for waitlist in waitlists:
                if waitlist['student_id'] == student['student_id']:
                    student_data["courses"].append({
                        "course_name": waitlist['course_name'],
                        "status": "Waitlist"
                    })

            progress.append(student_data)

        return progress



# Displays the progress of children (students) for a parent.
# - Calls the `get_children_progress` method to retrieve the progress data.
# - For each child, prints their name and details of their courses.
# - If a grade is available, it prints the course name and grade. If the child is on the waitlist, it prints the course name and status.
# - Adds a blank line between each child's progress for readability.
    def view_children_progress(self,db_manager):

        childrens = self.get_children_progress(db_manager)
        for children in childrens:
            print(f"Child: {children['student_name']}")
            for course in children['courses']:
                if 'grade' in course:
                    print(f"Course: {course['course_name']} | Grade: {course['grade']}")
                elif 'status' in course:
                    print(f"Course: {course['course_name']} | Status: {course['status']}")
            print()  # Add a blank line between students



# Checks and displays a child's position in the waitlist for a specific course.
# - Prompts the user for the child's ID and the course ID.
# - Retrieves the child's position in the waitlist using the database manager.
# - Prints the child's name and their position in the waitlist for the specified course.
    def check_waitlist_status(self,db_manager):
        child_id = input("Enter child id: ")
        course_id = input("Enter course id: ")
        child = db_manager.get_child_position_in_waitlist(child_id,course_id)
        print(f"Child {child['student_name']} is at position {child['position']} in the waitlist")



# Processes a payment for the parent.
# - Prompts the user to input the payment amount and validates that it is greater than zero.
# - Asks for a description of the payment.
# - Retrieves the current date and formats it correctly.
# - Creates a new Payment object with the provided information.
# - Calls the database manager's `add_payment` method to insert the payment into the database.
# - Prints a success or failure message based on whether the payment was successfully created.
# - Catches and prints any errors that occur during the process.
    def make_payment(self,db_manager):
        try:
            # Get and validate the amount
            while True:
                try:
                    amount = float(input("Enter amount: ").strip())
                    if amount <= 0:
                        raise ValueError("Amount must be greater than zero.")
                    break
                except ValueError as e:
                    print(f"Invalid amount: {e}. Please try again.")

            # Get description
            description = input("Enter description: ").strip()

            # Get the current date in the correct format
            payment_date = datetime.now().strftime('%Y-%m-%d')

            # Prepare payment information
            payment_info = Payment(
                parent_id = self.id,
                amount = amount,
                payment_date = payment_date,
                description = description
            )

            # Call add_payment to insert into the database
            if db_manager.add_payment( payment_info):
                print("Payment created successfully.")
            else:
                print("Failed to create payment.")
        except Exception as e:
            print(f"An error occurred while making the payment: {e}")