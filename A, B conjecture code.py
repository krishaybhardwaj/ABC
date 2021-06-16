def conjecture(n):
    count = 0
    while n != 1:
        if n%2==0:
            n = n//2
        else:
            n = 3*n+1
        count+=1
    return count
 
x = int(input("Enter any number: "))
y = int(input("Enter any number: "))

steps_x = conjecture(x)
steps_y = conjecture(y)

dictionary = {}        
for i in range(x, y+1):
    dictionary[i] = conjecture(i)

t = max(dictionary, key=dictionary.get)
print("The maximum number of steps will be taken by", t, "which is", conjecture(t), " steps")