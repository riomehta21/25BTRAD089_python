import json
import os
file = "students.json"
def load():
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {}
def save(students):
    with open(file, "w") as f:
        json.dump(students, f)
while True:
    students = load()

    print("\n1.Add  2.Search  3.Update  4.Display  5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        roll = input("Enter roll number: ")
        if roll in students:
            print("Student already exists!")
            continue
        name = input("Enter name: ")
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))
        students[roll] = {
            "name": name,
            "course": course,
            "marks": marks
        }
        save(students)
        print("Record added successfully!")
    elif choice == "2":
        roll = input("Enter roll number: ")
        if roll in students:
            print(students[roll])
        else:
            print("Student not found!")
    elif choice == "3":
        roll = input("Enter roll number: ")
        if roll in students:
            students[roll]["marks"] = float(input("Enter new marks: "))
            save(students)
            print("Record updated!")
        else:
            print("Student not found!")
    elif choice == "4":
        for roll, details in students.items():
            print(roll, details)
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
