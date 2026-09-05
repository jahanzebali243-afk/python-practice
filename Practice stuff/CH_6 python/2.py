#2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

math = int(input("Enter your marks :-  "))
english = int(input("Enter your marks :-  "))
science = int(input("Enter your marks :-  "))
percentage = (math+english+science)/3
if (math>=33 and english>=33 and science >= 33 and percentage >= 40 ) :
    print (f"You have been passed \n your percentage is :- {percentage}")
elif (math>=33 or english>=33 or science >= 33 ):
    print (f"you have been failed \n your percentage is :- {percentage} \n but you have been failed in subject cause you scored less then 33 marks in one sub")
elif (math>=33 and english>=33 and science >= 33 or percentage >= 40):
    print (f"you have been failed \n your percentage is :- {percentage} \n you secured passing marks in subjects but failed to secured 40% percentage in your exam")
else:
    print ("404 Error")

