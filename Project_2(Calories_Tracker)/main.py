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

# --- Activity Level ---
print("\nSelect your activity level:")
print("1. Sedentary (no exercise)")
print("2. Light exercise (1-3 days/week)")
print("3. Moderate exercise (3-5 days/week)")
print("4. Heavy exercise (6-7 days/week)")
print("5. Athlete (2x per day)")

activity = input("Enter choice (1-5): ").strip()

activity_factors = {
    "1": 1.2,
    "2": 1.375,
    "3": 1.55,
    "4": 1.725,
    "5": 1.9
}

if activity in activity_factors:
    factor = activity_factors[activity]
    if gender in ["m", "male"]:
        tdee = bmr_male * factor
    else:
        tdee = bmr_female * factor
    print(f"\nYour daily calorie needs (TDEE): {tdee:.0f} calories")
else:
    print("Invalid activity choice.")
    tdee = 0