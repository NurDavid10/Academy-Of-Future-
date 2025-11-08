
import dotenv
import pandas as pd
from datetime import datetime
import os
dotenv.load_dotenv()
# Step 1: Load Excel Data and Print Overview
def load_excel_data(file_path):
    try:
        # Load all sheets
        all_sheets = pd.read_excel(file_path, sheet_name=None)
        print("Data loaded successfully!")
        print("Sheets loaded:")
        for sheet_name in all_sheets.keys():
            print(f"- {sheet_name}")
        return all_sheets
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Step 2: Perform Long Waitlist Analysis
def analyze_waitlist(waitlist_df, courses_df):
    waitlist_analysis = (
        waitlist_df.merge(courses_df, on="CourseID")
        .groupby("CourseName")
        .agg(
            Number_of_Students=("StudentID", "count"),
            Average_Wait_Time=("RequestDate", lambda x: (pd.to_datetime("today") - pd.to_datetime(x)).dt.days.mean()),
        )
        .reset_index()
    )

    print("--- Long Waitlist Analysis ---")
    for _, row in waitlist_analysis.iterrows():
        print(f"Course: {row['CourseName']}")
        print(f"Number of Students in Waitlist: {int(row['Number_of_Students'])}")
        print(f"Average Wait Time: {int(row['Average_Wait_Time'])} days")
    return waitlist_analysis

# Step 3: Allocation Algorithm
def allocate_students(students_df, courses_df, waitlist_df, teachers_df):
    allocations = []
    new_classes = []
    overflow_students = []

    for _, course_row in courses_df.iterrows():
        course_name = course_row["CourseName"]
        course_id = course_row["CourseID"]
        capacity = course_row["Capacity"]
        registered_students = course_row["RegisteredStudents"]

        print(f"Processing Course: {course_name}")

        # Students in waitlist for this course
        course_waitlist = waitlist_df[waitlist_df["CourseID"] == course_id]

        if not course_waitlist.empty:
            if registered_students < capacity:
                available_spots = capacity - registered_students
                students_to_add = min(len(course_waitlist), available_spots)
                allocations.extend(course_waitlist.head(students_to_add)["StudentID"].tolist())
                registered_students += students_to_add
                remaining_waitlist = len(course_waitlist) - students_to_add

                print(f"- Successfully added {students_to_add} students from waitlist.")
                print(f"- Remaining students in waitlist: {remaining_waitlist}")
            else:
                print(f"- Course is full. Transferred {len(course_waitlist)} students to Chemistry Basics.")
                overflow_students.extend(course_waitlist["StudentID"].tolist())
        else:
            print(f"- No students in waitlist.")

    # Handle overflow students
    if len(overflow_students) > 30:
        new_class_name = "Class Overflow"
        print(f"Opening New Class: \"{new_class_name}\"")
        print(f"- Added {len(overflow_students)} students from remaining waitlists.")
        print(f"Total Cost: $500")
        new_classes.append({
            "CourseName": new_class_name,
            "Capacity": len(overflow_students),
            "RegisteredStudents": len(overflow_students),
        })

    return allocations, new_classes

# Step 4: Save Results to Excel
def save_results_to_excel(waitlist_analysis, allocations, new_classes, output_file):
    with pd.ExcelWriter(output_file) as writer:
        # Sheet 1: Long Waitlist Analysis
        waitlist_analysis.to_excel(writer, sheet_name="Long Waitlist Analysis", index=False)

        # Sheet 2: Transferred Students
        pd.DataFrame(allocations, columns=["StudentID"]).to_excel(writer, sheet_name="Transferred Students", index=False)

        # Sheet 3: New Classes Opened
        pd.DataFrame(new_classes).to_excel(writer, sheet_name="New Classes Opened", index=False)

    print("Reports saved successfully!")
    print("Contents:")
    print("- Sheet 1: Long Waitlist Analysis")
    print("- Sheet 2: Transferred Students")
    print("- Sheet 3: New Classes Opened")
# Main Execution5
file_path = f"{os.environ['path']}/Pandas/learning_center_project_data.xlsx"
data = load_excel_data(file_path)
print(data)
if data:
    students_df = data["Students"]
    courses_df = data["Courses"]
    waitlist_df = data["Waitlist"]
    teachers_df = data["Teachers"]
waitlist_analysis = analyze_waitlist(waitlist_df, courses_df)    
allocations, new_classes = allocate_students(students_df, courses_df, waitlist_df, teachers_df)
output_file = "Pandas/advanced_waitlist_report.xlsx"
save_results_to_excel(waitlist_analysis, allocations, new_classes, output_file)

