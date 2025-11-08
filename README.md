```markdown
# 📚 Learning Center Management System - "Academy of Tomorrow"

## 📝 Project Description
This system is designed to manage the "Academy of Tomorrow" learning center, providing an advanced solution for managing students, courses, teachers, general employees, payments, and course waitlists.
The system is based on **Object-Oriented Programming (OOP)** in Python and uses **MySQL** as its database management system.

---

## 🚀 **Installation & Execution**
### 1️⃣ **System Requirements**
- Python 3.8 or higher
- MySQL Server
- External libraries (if required)

### 2️⃣ **Installing Required Libraries**
If the project requires additional libraries, install them using:
```bash
pip install -r requirements.txt
```

### 3️⃣ **Running the Project**
```bash
python main.py
```

---

## 📂 **Project Structure**
```
📁 project_root/
│── 📁 classes/
│    │── all_classes.py        # Centralized class definitions
│    │── class_room.py         # Classroom class
│    │── course.py             # Course class
│    │── courses_enrollments.py # Course enrollment class
│    │── employee.py           # Employee class
│    │── manager.py            # Manager class
│    │── parent.py             # Parent class
│    │── payment.py            # Payment class
│    │── queue.py              # Course waitlist class
│    │── schedule.py           # Scheduling class
│    │── student.py            # Student class
│    │── task.py               # Task management class
│    │── teacher.py            # Teacher class
│    │── user.py               # User base class
│── database_manager.py        # Database manager
│── main.py                    # Main entry point
│── requirements.txt           # Required libraries (if any)
│── README.md                  # Project documentation
```

---

## 📝 **Key Classes Description**
- **`ClassRoom`**: Represents a classroom with an ID, name, location, and maximum capacity.
- **`Course`**: Represents a course, including ID, name, description, assigned teacher, and location.
- **`CourseEnrollment`**: Manages student enrollments and grades.
- **`Employee`**: Represents a general employee responsible for maintenance tasks.
- **`Manager`**: Represents the system administrator, with privileges to add users, manage courses, and oversee administrative tasks.
- **`Parent`**: Represents a parent who can enroll children in courses, check their queue position, and make payments.
- **`Payment`**: Handles payments made by parents for courses.
- **`Queue`**: Manages waitlists for popular courses.
- **`Schedule`**: Manages course schedules, including time and location.
- **`Student`**: Represents students enrolled in the system, storing personal data and grades.
- **`Task`**: Manages tasks such as classroom maintenance and issue reporting.
- **`Teacher`**: Represents a teacher with the ability to enter grades and manage courses.
- **`User`**: A base class for all system users (teachers, students, parents, etc.).
- **`DatabaseManager`**: Handles database connections and CRUD operations.

---

## 🔍 **Main Features**
- **🔍 Student & Parent Management**: Parents can register their children for courses, track progress, and make payments.
- **🔍 Course Enrollment & Management**: Students can enroll in courses, and if full, they are placed on a waitlist.
- **🔍 Teacher & Classroom Management**: Teachers can enter grades and manage their classrooms.
- **🔍 Task & Maintenance Management**: General employees receive maintenance tasks and update their completion status.
- **🔍 Financial Management**: Parents can make payments, and the system generates periodic financial reports.
- **🔍 User Administration**: Managers can add/remove users and manage roles.

---

## 🛠 **Potential Enhancements**
- Integration with a graphical user interface (GUI).
- Advanced waitlist management for courses.
- Expanded analytics and reporting features.
- Integration with existing learning management systems (LMS).


