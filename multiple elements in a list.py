# make your own list
list = []
user_input = int(input("How long should the list be? "))  

steps = 1
for i in range(0, user_input ):
    element = int(input(f'Enter element number {steps}: '))
    steps+=1

    list.append(element) 
print(f'The list you made: {list}\n')


# find how many times an element has
x = int(input("Enter any element from the list you just made: "))
count = 0
for y in list:
    if(y==x):
        count+=1
        
print(f'{x} has occured {count} times')