name = input("Enter student name: ")
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
total = marks1 + marks2 + marks3
percentage = total / 3
print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)
