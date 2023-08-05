import csv
import os
from student_grade_calculator.utils import Student


def load_student_data(filename):
    students = []
    if not os.path.exists(filename):
        # If the file doesn't exist, create a new one with header
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Mathematics', 'Science', 'English'])  # Header row
    else:
        # If the file exists, load student data from it
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                name, *grades = row
                grades = [float(grade) for grade in grades]
                student = Student(name, grades)
                students.append(student)

    return students


def save_student_data(filename, students):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Mathematics', 'Science', 'English'])  # Header row
        for student in students:
            writer.writerow([student.name, *student.grades])


def calculate_average_grade(grades):
    return sum(grades) / len(grades)


def calculate_class_average(students):
    total_students = len(students)
    total_grade_sum = sum(sum(student.grades) for student in students)
    return total_grade_sum / (total_students * 3)


def find_highest_lowest_average(students):
    highest_average = float('-inf')
    lowest_average = float('inf')
    highest_student = None
    lowest_student = None

    for student in students:
        avg_grade = calculate_average_grade(student.grades)
        if avg_grade > highest_average:
            highest_average = avg_grade
            highest_student = student.name
        if avg_grade < lowest_average:
            lowest_average = avg_grade
            lowest_student = student.name

    return highest_student, highest_average, lowest_student, lowest_average


def main():
    print("Welcome to the Student Grade Calculator!\n")

    filename = "grades.csv"
    students = load_student_data(filename)

    while True:
        print("\n1. Add New Student")
        print("2. Update Grades")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Class Statistics")
        print("6. Save and Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter the student's name: ")
            math_grade = float(input("Enter Mathematics Grade: "))
            sci_grade = float(input("Enter Science Grade: "))
            eng_grade = float(input("Enter English Grade: "))
            new_student = Student(name, [math_grade, sci_grade, eng_grade])
            students.append(new_student)
            print(f"\nStudent '{name}' added successfully!")

        elif choice == "2":
            name = input("Enter the student's name to update grades: ")
            found = False
            for student in students:
                if student.name == name:
                    print(f"\nCurrent Grades for {name}: {student.grades}")
                    math_grade = float(input("Enter new Mathematics Grade: "))
                    sci_grade = float(input("Enter new Science Grade: "))
                    eng_grade = float(input("Enter new English Grade: "))
                    student.grades = [math_grade, sci_grade, eng_grade]
                    found = True
                    print(f"Grades updated for {name}!")
                    break
            if not found:
                print(f"Student '{name}' not found!")

        elif choice == "3":
            name = input("Enter the student's name to delete: ")
            for student in students:
                if student.name == name:
                    students.remove(student)
                    print(f"\nStudent '{name}' deleted successfully!")
                    break
            else:
                print(f"Student '{name}' not found!")

        elif choice == "4":
            print("\n----- All Students -----")
            for idx, student in enumerate(students, 1):
                avg_grade = calculate_average_grade(student.grades)
                print(f"{idx}. {student.name} - Average Grade: {avg_grade:.2f}")

        elif choice == "5":
            if len(students):
                class_avg = calculate_class_average(students)
                highest_student, highest_avg, lowest_student, lowest_avg = find_highest_lowest_average(students)

                print("\n----- Class Statistics -----")
                print(f"Total Students: {len(students)}")
                print(f"Class Average Grade: {class_avg:.2f}")
                print(f"Highest Average Grade: {highest_avg:.2f} ({highest_student})")
                print(f"Lowest Average Grade: {lowest_avg:.2f} ({lowest_student})")
            else:
                print("There are no student records, add at least 1 record.")


        elif choice == "6":
            save_student_data(filename, students)
            print("\nExiting the Student Grade Calculator... Have a great day!")
            break

        else:
            print("\nInvalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
