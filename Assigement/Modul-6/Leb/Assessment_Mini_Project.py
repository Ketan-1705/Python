class Student:
    def __init__(self):
        self.marks = []

    def get_data(self):
        for i in range(1, 4):
            mark = int(input(f"Subject {i}: "))
            self.marks.append(mark)

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 3

    def grade(self):
        per = self.percentage()

        if per >= 90:
            return "A+"
        elif per >= 75:
            return "A"
        elif per >= 60:
            return "B"
        elif per >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())


while True:
    student = Student()
    student.get_data()
    student.display()
