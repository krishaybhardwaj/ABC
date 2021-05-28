x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
steps_x= 0
while x > 1:
    if x%2 == 1:
        x = 3*x+1
    else : x = x/2
    steps_x+=1
print(str(x) + " will take " + str(steps_x) + " steps")
steps_y=0
while y>1:
    if y%2==1:
        y=3*y+1
    else : y = y/2
    steps_y+=1
print(str(y) + " will take " + str(steps_y) + "steps")   
if steps_x>steps_y:
    print(str(x) +" took more steps than " + str(y))
else : 
        print(str(y) +" Number took more steps than " + str(x))