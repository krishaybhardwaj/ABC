x = int(input("Enter a number - "))
y = int(input("Enter another number - "))
steps = 0
while range(x, y, 1) > 1:
    if range(x, y, 1)%2==0:
        range(x, y, 1)/2 = range(x, y)
    else:
        range(x, y) = 3 * range(x, y) + 1
        return steps
        
def conjecture(i):
    for i in range(x, y):
        steps_i is max in steps
        steps_i == 0
    while i > 1:
        if i%2==0:
           i=i/2
           steps_i+=1
        else:
            i=i*3+1
            steps_i+=1
    return steps_i
    print(conjecture(7))
    