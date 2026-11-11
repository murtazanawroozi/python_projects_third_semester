class Student:
    university = "KU"

    def __init__(self, name):
        self.name = name

    def display(self):
        return self.name

    @classmethod
    def university_name(cls):
        return cls.university

    @staticmethod
    def valid_age(age):
        return age >= 16