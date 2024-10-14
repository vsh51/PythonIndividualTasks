from .student import Student

class Course:
    def __init__(self, course_name, hours_count):
        self.course_name = course_name
        self.hours_count = hours_count
        self.students: list[Student] = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def is_student_enrolled(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return True
        return False

    def __add__(self, student: Student):
        return self.add_student(student)

    def __str__(self):
        if len(self.students) != 0:
            student_list = "\n".join([str(student) for student in self.students])
        else:
            student_list = "No students enrolled"

        return f"Course name: {self.course_name}\n" \
                f"Hours: {self.hours_count}\n" \
                "Students:\n" \
                f"{student_list}"

    def __getitem__(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
