#Make a class Student with __init__ taking name and marks. Add a method show() that prints "Name: X, Marks: Y". Create two students and call show() on both
class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
        print (f"Name :- {self.name}\nMarks -: {self.marks}/100")

s1 = Student("Jahanzeb",50)
s2 = Student("Rehan",67)

        