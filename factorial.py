#code to find factorial of a number

user_input = int(input("Enter any number: "))

def factorial(n):
    
    constant = 1
    
    if n == 0:
        print(1)
    
    while n > 0:
        
        fact_range = range(1, n + 1)
        
        for i in fact_range:
            
            constant *= i
            
        return constant

print(factorial(user_input))