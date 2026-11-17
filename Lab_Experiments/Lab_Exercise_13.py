import csv
import os
file = "employees.csv"
# Create sample CSV file
if not os.path.exists(file):
    with open(file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Name", "Basic", "HRA", "Allowance", "Rate"])
        w.writerow([101, "Rahul", 30000, 5000, 2000, 10])
        w.writerow([102, "Priya", 40000, 8000, 3000, 12])
        w.writerow([103, "Amit", 25000, 4000, 1500, 8])
# Read records and calculate salaries
total_gross = total_deduction = total_net = 0
count = 0
with open(file, "r") as f:
    for e in csv.DictReader(f):
        basic = float(e["Basic"])

        hra = float(e["HRA"])
        allowance = float(e["Allowance"])
        rate = float(e["Rate"])
        gross = basic + hra + allowance
        deduction = gross * rate / 100
        net = gross - deduction
        print(e["ID"], e["Name"],
              "Gross:", gross,
              "Deduction:", deduction,
              "Net Salary:", net)
        total_gross += gross
        total_deduction += deduction
        total_net += net
        count += 1
print("\nTotal Employees:", count)
print("Total Gross Salary:", total_gross)
print("Total Deductions:", total_deduction)
print("Total Net Salary:", total_net)
