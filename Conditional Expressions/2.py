#Write a program to find out whether a student has passed or failed if it requires a total of40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

Math = (int(input("Enter your marks in Math :- " )))
Physics = (int(input("Enter your marks in Physics :- " )))
Urdu = (int(input("Enter your marks in Urdu :- " )))
Total_percentage = (Math+Physics+Urdu) /3 
if(Math>=33) and (Physics>=33) and (Urdu>=33) and (Total_percentage>=40 ) :
    print("Congortulations and Celebration ")
else :
    print("Sorry you are failed ,Dont worry budyy , Try Next time")
print(f"Your Total_percentage is {Total_percentage :.2f}%")


