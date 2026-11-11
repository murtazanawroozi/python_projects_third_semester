class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def introduce(self):
        return f"{self.name} - {self.department}"

s1 = Student("Ahmad", "Software Engineering")
print(s1.introduce())
