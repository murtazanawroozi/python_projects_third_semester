class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())


# Page 19
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"

class Student(Person):
    def study(self):
        return f"{self.name} is studying"

s = Student("Ahmad")
print(s.introduce())
print(s.study())