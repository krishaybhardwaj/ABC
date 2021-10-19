y = int(input("Enter any number: "))
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-2) + fibonacci(x-1)
for x in range(y):
        
    print(fibonacci(x))
    