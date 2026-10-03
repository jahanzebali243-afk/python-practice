#Add a method is_pass() to Student that returns True if marks ≥ 40, else False. Print the result for each student.

class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
        print (f"Name :- {self.name}\nMarks -: {self.marks}/100")
    def result (self):
        if self.marks >=40:
            print ("Result :- PASS")
        else :
            print ("Result :- FAIL")


s1 = Student("Jahanzeb",50)
s1.result()
s2 = Student("Rehan",67)
s2.result()
s3 = Student("Ayesha",32)
s3.result()