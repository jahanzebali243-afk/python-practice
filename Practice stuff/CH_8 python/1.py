#1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if a > b and a >c :
        return "a is greatest"
    elif b > a and b > c :
        return "b is greatest"
    elif c > a and c > b :
        return "c is greatest"
print(greatest(42,445,34))