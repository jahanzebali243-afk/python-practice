#4. Write a recursive function to calculate the sum of first n natural numbers.
def calc_natural_num(a):
    if a == 0:
        return 0
    else :
        return a + calc_natural_num (a-1)
        
print (calc_natural_num(10))

