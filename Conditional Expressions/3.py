# A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams
   

c1=("Make a lot of money")
c2=("buy now")
c3=("Subscribe this")
c4=("Click here")

c=input("Enter your comment :- ").lower()

if(c1 in c or c2 in c or c3 in c or c4 in c) :
    print("THIS IS AN SPAM COMMENT SO PLAEASE IGNORE THIS OR DO THIS ON YOUR OWN CONCERN")
else :
    print("This comment is safe as regular comment ")