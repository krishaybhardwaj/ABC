# Code to reverse the digits of a number
x = int(input("Enter a number: "))
rev_num = 0
 
while(x > 0):
    a = x % 10
    rev_num = rev_num * 10 + a
    x = x // 10
 
print(rev_num)