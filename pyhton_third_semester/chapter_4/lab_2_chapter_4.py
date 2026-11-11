class InvalidGradeError(Exception):
    def __init__(self, grade):
        self.grade = grade
        super().__init__(f"Grade {grade} out of range (0-100).")

try:
    with open("grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
                
            value = int(cleaned_line)
            if not (0 <= value <= 100):
                raise InvalidGradeError(value)
                
            print("Processed grade:", value)

except FileNotFoundError:
    print("The grades.txt file could not be found.")

except ValueError:
    print("Failed to parse non-numeric grade text.")

except InvalidGradeError as error:
    print("Encountered an invalid value:", error)