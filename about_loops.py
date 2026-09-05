#1. Simple Iteration (fixed )
N = 4 
for i in range(N):
    print ("Pakistan")

#2. Accumulator Pattern (for building results)
result = 5   # sum ke liye 0, product ke liye 1
for i in range(10):
    result = result + i    # ya *, ya koi bhi operation
print(result)

#3. Filter Pattern (checking coundition)
collection = 23
for item in collection:
    if collection /2 :
        pass
        # us item pe kaam karo

#4. Search + Flag Pattern (Finding something)
target = 5
collection = 4
found = False
for item in collection:
    if item == target:
        found = True
        break
if found:
    print("Found")
else:
    print("Not Found")
    pass

#5.Nested Loop (loop ke andar loop)
for i in range("rows"):
    for j in range("col"):
         pass

#6. Whgile with Counter (condition + manual update)
i = 10
while i>8:
    i % 2 == 0
    print (i)
    i = i + 1    
    

#7. Reverse/Step Loop
for i in range(9, 90, 10):
    print (i)