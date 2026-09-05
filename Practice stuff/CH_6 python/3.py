#6. Write a program to calculate the grade of a student from his marks from the following scheme: 90 – 100 => Ex 80 – 90 => A 70 – 80 => B 60 – 70 => C 50 – 60 => D <50 => F
math = int(input("Enter your marks :-  "))
english = int(input("Enter your marks :-  "))
science = int(input("Enter your marks :-  "))
perc = (math + english + science )/3

if perc == 100 or perc >= 91 :
    print (f"You got Ex grade and you percentage is {perc}")
elif perc == 90 or perc >= 81 :
    print (f"You got A grade and you percentage is {perc}")
elif perc == 80 or perc >= 71 :
    print (f"You got B grade and you percentage is {perc}")
elif perc == 70 or perc >= 61 :
    print (f"You got C grade and you percentage is {perc}")
elif perc == 60 or perc >= 50 :
    print (f"You got D grade and you percentage is {perc}")
else:
    print (f"You got F grade cause your percentage is {perc}")
