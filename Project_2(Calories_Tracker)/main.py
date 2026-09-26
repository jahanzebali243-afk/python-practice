print ("=== Calories Tracker ===")
print ("Enter how much Calories u eat and how much calories have left we can track your calories perfectly")

#Find BMR
gender = input("Male/FeMale :- ").strip().lower()
age = int(input("Enter your age :- "))
weight = float(input("Enter your current weight in KG :- "))
height = float(input("Enter your height in cm :- "))
bmr_male = (10*weight)+(6.25*height)-(5*age)+5
bmr_female = (10*weight)+(6.25*height)-(5*age)-161
if gender in ["m" , "male"] :
    print (f"your current BMR is :{bmr_male} calories")
elif gender in ["f" , "female"] :  
    print (f"your current BMR is :{bmr_female} calories")
else:
    print ("404 Error")

#print (f"===your gender is {gender}===\n===your age is {age}===\n===your weight is {weight}lbs===\n===your height is {height}cm===")