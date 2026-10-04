with open ("table.txt" , "a")as f:
    num = 1
    for i in range (1,11):
        f.write (f"{num} x {i} = {num*i}\n")

        