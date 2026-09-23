#create a class student and take average of 3 subjects

class student :
    def __init__(self ,name , total_marks):
        self.name = name 
        self.total_marks = total_marks
    def average (self ):
        sum = 0
        for  eachValue in self.total_marks:
            sum = sum+eachValue
               
        average =  sum/3
        print (f"Average of your marks is : {average}")

student1 = student ("jahanzeb" , [66,66,66])
student1.average()
        




    


        