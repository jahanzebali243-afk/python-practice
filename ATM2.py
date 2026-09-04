
users = {
    "Anwar32": 3222,
    "Ali45": 4567,
    "Sara99": 7890
}

card = input("Scan your card code: ")

if card in users:
    print(f"Welcome {card}! Please enter your PIN code.")
    pin = int(input("Enter your PIN code: "))
    
    if pin == users[card]:
        print("Welcome! How much amount do you want to transact?")
    else:
        print("Invalid PIN! Please try again.")
else:
    print("Your card is not listed. Please contact the bank.")