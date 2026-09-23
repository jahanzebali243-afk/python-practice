#make a OOP  program to find out is number is even or not 

class even :
    @staticmethod
    def __init__(num):
        if num % 2 == 0 :
            print (f"Given Number {num} is Even Number")
        else:
            print (f"Given Number {num} is ODD Number")

num = even(800)