#PROJECT 1
#ROCK PAPER SCISSOR GAME

import random 
outcome_a = ("Match DRAW !!!")
outcome_b = ("Computer WON !!")
outcome_c = ("YOU WON !!")
def game():
    computer = random.choice (["rock" , "paper" , "scissor"])
    print ("Please Choose from rock ,paper, scissor")
    you = input ("enter your choice -:  ").strip().lower()
    print (f"you choose {you} and computer choose {computer}")
    if computer == you :
        print (outcome_a)

    else:
        if computer == "rock" and you == "scissor" or computer == "scissor" and you == "paper" or computer == "paper" and you == "rock":
            print (outcome_b)
        elif you == "rock" and computer == "scissor" or you == "scissor" and computer == "paper" or you == "paper" and computer == "rock":
            print (outcome_c)
        else:
            print ("Please Enter valid input from rock , paper , scissor ") 

def game_2():
    while True:
        game()
        ask = input ("Want to play next round ? \n Yes or No :  ").strip
        ().lower()
        if ask in ["y" , "yes"]:
          print ("Next Round Begin!!")            
        else : 
            print("Thanks For Playing")
            break

def result ():
    your_score = 0
    computer_score = 0
    match_draw = 0
    if outcome_b == "Computer WON !!" :
        return computer_score+1
    elif outcome_c =="You WON !!":
        return your_score+1
    elif outcome_a == "MATCH DARW !!":
        return match_draw+1
result()
game_2()