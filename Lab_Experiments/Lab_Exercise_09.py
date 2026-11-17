students = {}
# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
# Input student details
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("\nEnter student name: ")
    marks = float(input("Enter marks (0-100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")
        continue
    students[name] = marks
# Display student results
print("\n===== STUDENT GRADING SYSTEM =====")
print("Name\t\tMarks\tGrade")
print("----------------------------------")
for name, marks in students.items():
    grade = calculate_grade(marks)
    print(f"{name}\t\t{marks}\t{grade}")
print("----------------------------------")
print("Results displayed successfully!")
