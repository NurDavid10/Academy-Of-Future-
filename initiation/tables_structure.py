# Defines the database schema using SQL CREATE TABLE statements.
# - Each key corresponds to a table name, and the value contains the SQL to create the table.
# - Includes relationships using foreign keys to enforce referential integrity.
tables = {
    "Users": """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            role ENUM('manager', 'parent', 'student', 'teacher', 'employee') NOT NULL,
            password VARCHAR(255) DEFAULT 111,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """,
    "Managers": """
        CREATE TABLE IF NOT EXISTS managers (
                manager_id INT PRIMARY KEY,
                FOREIGN KEY (manager_id) REFERENCES users(id) ON DELETE CASCADE
            );
    """,
    "Parents": """
        CREATE TABLE IF NOT EXISTS parents (
                parent_id INT PRIMARY KEY,
                FOREIGN KEY (parent_id) REFERENCES users(id) ON DELETE CASCADE
            );
    """,
    "Students": """
        CREATE TABLE IF NOT EXISTS students (
                student_id INT PRIMARY KEY,
                age INT NOT NULL,
                grade_level VARCHAR(50),
                parent_id INT,
                FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (parent_id) REFERENCES parents(parent_id) ON DELETE SET NULL);
    """,
    "Teachers": """
        CREATE TABLE IF NOT EXISTS teachers (
                    teacher_id INT PRIMARY KEY,
                    hire_date DATE,
                    specialization VARCHAR(100),
                    salary DECIMAL(10, 2),
                    FOREIGN KEY (teacher_id) REFERENCES users(id) ON DELETE CASCADE
                );
    """,
    "Employees": """
        CREATE TABLE IF NOT EXISTS employees (
                employee_id INT PRIMARY KEY,
                salary DECIMAL(10, 2),
                FOREIGN KEY (employee_id) REFERENCES users(id) ON DELETE CASCADE
            );
    """,
    "ClassRooms": """
        CREATE TABLE IF NOT EXISTS classRooms (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            capacity INT DEFAULT 30,
            location VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """,
    "Courses": """
        CREATE TABLE IF NOT EXISTS courses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            teacher_id INT,
            max_capacity INT DEFAULT 30,
            class_room_id INT,
            FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
            FOREIGN KEY (class_room_id) REFERENCES classRooms(id) ON DELETE SET NULL

        )
    """,
    "CourseEnrollments": """
        CREATE TABLE IF NOT EXISTS courseEnrollments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            course_id INT,
            student_id INT,
            grade DECIMAL(4, 2),
            FOREIGN KEY (course_id) REFERENCES courses(id),
            FOREIGN KEY (student_id) REFERENCES students(student_id)
        )
    """,
    "Queue": """
        CREATE TABLE IF NOT EXISTS queue (
            id INT AUTO_INCREMENT PRIMARY KEY,
            course_id INT,
            student_id INT,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (course_id) REFERENCES courses(id),
            FOREIGN KEY (student_id) REFERENCES students(student_id)
        )
    """,
    "Tasks": """
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            description TEXT NOT NULL,
            assigned_to INT,
            status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
            class_room_id INT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (assigned_to) REFERENCES employees(employee_id),
            FOREIGN KEY (class_room_id) REFERENCES classRooms(id)

        )
    """,
    "Payments": """
        CREATE TABLE IF NOT EXISTS payments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            parent_id INT,
            amount DECIMAL(10, 2) NOT NULL,
            payment_date DATE NOT NULL,
            description TEXT,
            FOREIGN KEY (parent_id) REFERENCES parents(parent_id)
        )
    """,
    "Schedules": """
        CREATE TABLE IF NOT EXISTS schedules (
            id INT AUTO_INCREMENT PRIMARY KEY,
            course_id INT,
            teacher_id INT,
            date DATE NOT NULL,
            time TIME NOT NULL,
            class_room_id INT,
            FOREIGN KEY (course_id) REFERENCES courses(id),
            FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
            FOREIGN KEY (class_room_id) REFERENCES classRooms(id) ON DELETE SET NULL

        )
    """,
}