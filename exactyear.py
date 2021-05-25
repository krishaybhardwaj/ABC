# finding exact same calendar year
x = int(input("Enter the year: "))
if x>2021:
    print("This year has not come yet")
elif x%4==0:
    print("This is a leap year, and the exact same calendar year will next occur in " + x+28)
elif x%4==1:
    print("The exact same calendar year will next occur in " + str(x+6))
elif x%4==2:
    print("The exact same calendar year will next occur in " + str(x+11))
elif x%4==3:
    print("The exact same calendar year will next occur in " + str(x+11))
  