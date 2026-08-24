#write a program to find the greatest of four numbers enterd by the user

n1=int(input("Enter your Marks :- " ))
n2=int(input("Enter your Marks :- " ))
n3=int(input("Enter your Marks :- " ))
n4=int(input("Enter your Marks :- " ))

if (n1>n2 and n1<n3 and n1>n4) :
    print("n1 gets highest marks in a class" )

elif (n2>n1 and n2>n3 and n2>n4) :
    print("n2 gets highest marks in a class" )

elif (n3>n1 and n3>n2 and n3>n4) :
    print("n3 gets highest marks in a class" )

elif (n4>n1 and n4>n2 and n4>n3) :
    print("n4 gets highest marks in a class")