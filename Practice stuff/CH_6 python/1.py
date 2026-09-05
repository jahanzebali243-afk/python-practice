#1. Write a program to find the greatest of four numbers entered by the user.

Ali = int(input("Enter a number :- "))
Rehan = int(input("Enter a number :- "))
Nomi = int(input("Enter a number :- "))
Aliza = int(input("Enter a number :- "))
if (Ali > Rehan and Ali > Nomi and Ali > Aliza)  :
    print(f"Ali number {Ali} is greatest number then others")
elif (Rehan > Ali and Rehan > Nomi and Rehan > Aliza) :
    print (f"Rehan number {Rehan} is greatest number then others")
elif (Nomi > Ali and Nomi > Rehan and Nomi > Aliza) :
    print (f"Nomi number {Nomi} is greatest number then others")
elif (Aliza > Ali and Aliza > Rehan and Aliza > Nomi) :
    print (f"Aliza number {Aliza} is greatest number then others")
else:
    print ("404 Error")
    
