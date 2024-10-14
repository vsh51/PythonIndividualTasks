from Task1_V2.course import Course
from Task1_V2.student import Student
import csv

def main():
    with open('course.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

        course = Course(data[1][0], data[1][1])

        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            
            for row in data[1:]:
                # Add student to the course method used
                course.add_student(Student(row[0], row[1], row[2]))

        # __str__ method used
        print("__str__ method used")
        print(course)

        # Get student method used
        print()
        print("Get student method used")
        print("Student with ID 123: ", f"\"{course['123']}\"")

        # Delete student method used
        print()
        print("Delete student method used")
        course.remove_student("123")
        print("Student with ID 123: ", f"\"{course['123']}\"")

        # Check if student is enrolled method used
        print()
        print("Check if student is enrolled method used")
        print("Is student with ID 123 enrolled? ", course.is_student_enrolled("123"))
        print("Is student with ID 124 enrolled? ", course.is_student_enrolled("124"))


if __name__ == "__main__":
    main()
