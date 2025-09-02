"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    if student_id not in attendance:
        attendance[student_id] = {
            "name": name,
            "present_days": [],
            "absent": []
        }
    else:
        return f"Student {student_id} is already registered."
    return attendance
print(register_student("id1", "Bamshak"))


def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    for student_id in student_ids:
        if student_id in attendance:
            if today not in attendance[student_id]["present_days"]:
                attendance[student_id]["present_days"].append(today)
            # remove from absent if mistakenly added
            if today in attendance[student_id]["absent_days"]:
                attendance[student_id]["absent_days"].remove(today)
        else:
            print(f"Student {student_id} not found.")
mark_present("id1")
def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    #implement logic
    for student_id in student_ids:
        if student_id in attendance:
            if today not in attendance[student_id]["absent_days"]:
                attendance[student_id]["absent_days"].append(today)
            # remove from present if mistakenly added
            if today in attendance[student_id]["present_days"]:
                attendance[student_id]["present_days"].remove(today)
        else:
            print(f"Student {student_id} not found.")

def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}
    for student_id, data in attendance.items():
        # filter by student_id
        if "student_id" in kwargs and kwargs["student_id"] != student_id:
            continue

        # filter only_present
        if kwargs.get("only_present") and not data["present_days"]:
            continue

        # filter only_absent
        if kwargs.get("only_absent") and not data["absent_days"]:
            continue

    return report