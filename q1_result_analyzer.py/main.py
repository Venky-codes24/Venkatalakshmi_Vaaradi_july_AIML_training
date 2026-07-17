def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    # Grade Calculation
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Display Student Details
    print("Student:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Grade:", grade)

    # Subjects below 40
    print("Subjects below 40:")

    found = False
    for i in range(len(marks)):
        if marks[i] < 40:
            print("Subject", i + 1)
            found = True

    if not found:
        print("None")


# Main Program
name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))

marks = []

print("Enter marks of 5 subjects:")
for i in range(5):
    mark = float(input(f"Subject {i+1}: "))
    marks.append(mark)

analyze_result(name, roll, marks)
