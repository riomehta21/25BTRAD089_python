from collections import Counter
filename = input("Enter log file name: ")
try:
    with open(filename, "r") as file:
        lines = file.readlines()
    if not lines:
        print("The log file is empty.")
    else:
        counts = Counter()
        for line in lines:
            if "ERROR" in line.upper():
                counts["ERROR"] += 1
            elif "WARNING" in line.upper():
                counts["WARNING"] += 1
            elif "INFO" in line.upper():
                counts["INFO"] += 1
        print("\n===== LOG FILE SUMMARY =====")
        print("Total lines:", len(lines))
        print("ERROR count:", counts["ERROR"])
        print("WARNING count:", counts["WARNING"])
        print("INFO count:", counts["INFO"])
        print("\n===== LOG ANALYSIS =====")
        if counts["ERROR"] > 0:
            print("Errors found! Check the log for problems.")
        else:
            print("No errors found.")
        if counts["WARNING"] > 0:
            print("Warnings found! Review potential issues.")
        else:

            print("No warnings found.")
except FileNotFoundError:
    print("Error: Log file not found!")
except PermissionError:
    print("Error: Permission denied while reading the file!")
