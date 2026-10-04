with open ("name.txt" , "w") as f :
    num = int(input("Enter a num :- "))
    for i in range (1,11):
        f.write (f"{num} x {i} = {num*i}\n")
print (f"Table of your number -: {num} has been saved in your file")
