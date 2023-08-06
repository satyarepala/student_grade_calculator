class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Name: {self.name}, Grades: {self.grades}"
