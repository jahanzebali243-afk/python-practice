#4. Write a program to find whether a given number is prime or not.
a = int(input("Enter your num -: "))
for i in range (2,a):
    if (a%i==0):
        print (f"your given number {a} is prime")
    else:
        print (f"your given number {a} is not prime")

    
