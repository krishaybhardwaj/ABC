x = int(input("Enter any number: "))
steps = 0
while x > 1:
    if x%2 == 1:
        x = 3*x+1
    else : x = x/2
    steps+=1
print(steps)