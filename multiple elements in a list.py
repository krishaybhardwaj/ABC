import random

list = [random.randrange(1, 21, 1) for i in range(10)]

print (f'Random number list is : {list}')

list_k=[]
for i in list:
    if i not in list_k:
        list_k.append(i)
    else:
        print(i)
