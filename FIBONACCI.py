x = int(input("Enter a number: "))
term_1 = 0
term_2 = 1
count = 0
if x < 0:
    print("please enter a positive integer")
else:
    
    print("The fibonacci sequence upto ", x, " terms is :\n")
    while count < x :
        print(term_1)
        term_x = term_1 + term_2
        term_1 = term_2    
        term_2 = term_x
        count+=1
    
