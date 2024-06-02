class Student():
    def __init__(self) -> None:
        self.numbers = {}
        pass
    def input_marks(self,number_of_students):
        for i in range(number_of_students):
            student = f'student{i}'
            self.numbers[student] = float(input(f'Enter the marks obtained by student{i}'))
    
    def display_marks(self):
        print(self.numbers)

student = Student()

student.input_marks(10)
student.display_marks()