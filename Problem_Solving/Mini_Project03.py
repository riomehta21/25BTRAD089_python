students = []
# Add a new student
def add_student():
    name = input("Enter student name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists!")
            return
    student = {
        "name": name,
        "attendance": []
    }
    students.append(student)
    print("Student added successfully!")
# Mark attendance
def mark_attendance():
    name = input("Enter student name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            status = input("Enter attendance (P/A): ").upper()
            if status in ["P", "A"]:
                student["attendance"].append(status)
                print("Attendance recorded successfully!")
            else:
                print("Invalid status! Enter P or A.")
            return
    print("Student not found!")
# Update the attendance of a previous class
def update_attendance():
    name = input("Enter student name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            if not student["attendance"]:
                print("No attendance records available!")
                return
            print("Attendance records:", student["attendance"])
            try:
                day = int(input("Enter class number to update: "))
                if 1 <= day <= len(student["attendance"]):
                    status = input("Enter new status (P/A): ").upper()
                    if status in ["P", "A"]:
                        student["attendance"][day - 1] = status
                        print("Attendance updated successfully!")
                    else:
                        print("Invalid status! Enter P or A.")
                else:
                    print("Invalid class number!")
            except ValueError:
                print("Please enter a valid class number.")
            return
    print("Student not found!")
# Display attendance details
def display_attendance():
    if not students:
        print("No students available!")
        return
    print("\n----- ATTENDANCE REPORT -----")
    print("Name\t\tPresent\tTotal\tPercentage")
    for student in students:
        records = student["attendance"]
        total = len(records)
        present = records.count("P")
        percentage = (present / total * 100) if total > 0 else 0
        print(
            f"{student['name']}\t\t{present}\t{total}\t"
            f"{percentage:.2f}%"
        )
# Identify students below the attendance threshold
def check_shortage():
    try:
        threshold = float(input("Enter attendance threshold (%): "))
        if not 0 <= threshold <= 100:
            print("Threshold must be between 0 and 100.")
            return
        print("\nStudents below attendance threshold:")
        found = False
        for student in students:
            records = student["attendance"]
            total = len(records)
            present = records.count("P")
            percentage = (present / total * 100) if total > 0 else 0
            if total > 0 and percentage < threshold:
                print(f"{student['name']}: {percentage:.2f}%")
                found = True
        if not found:
            print("No students below the threshold.")
    except ValueError:
        print("Please enter a valid threshold.")
# Main menu
while True:
    print("\n===== ATTENDANCE TRACKER =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Update Attendance")
    print("4. Display Attendance Report")
    print("5. Check Attendance Shortage")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        update_attendance()
    elif choice == "4":
        display_attendance()
    elif choice == "5":
        check_shortage()
    elif choice == "6":
        print("Exiting Attendance Tracker.")
        break
    else:
        print("Invalid choice! Try again.")
