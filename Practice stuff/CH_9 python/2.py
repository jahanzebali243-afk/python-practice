#2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score
import os

def game(new_score):
    try:
        with open("highscore.txt", "r") as f:
            high_score = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        high_score = 0  
    
    if new_score > high_score:
        with open("highscore.txt", "w") as f:
            f.write(str(new_score))
        print(f" New High Score: {new_score}!")
    else:
        print(f"Try again! Current High Score: {high_score}")

game(43)