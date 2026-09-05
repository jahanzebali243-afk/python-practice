#1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
a = input ("enter a work u want meaning : ")
dict = {
    "Englis" : "language" ,
    "book" : "kittab",
    "boy" : "ladka"
}
if a in dict:
    print (f"{dict[a]}")