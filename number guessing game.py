import random

user_input = int(input("Enter a number: "))

random_number = random.randint(0, user_input)

while True:
    guess = int(input("Guess the number - "))

    if guess == random_number:
        print("Correct, you won!")
        break
    
    elif guess > random_number:
        print("Go lower")
        
    else:
        print("Go higher")
    
    