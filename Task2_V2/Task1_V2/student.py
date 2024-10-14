class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"
