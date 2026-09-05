#1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poem.txt","r") as f :
    a = f.read()
    if "twinkle" in a :
        print ("Yes twinkle word exist in that file")
    else:
        print ("No there is no any word like twinkle")