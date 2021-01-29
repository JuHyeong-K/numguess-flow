import random

num = random.randint(0, 50)
while True:
    user_guess = int(input("Guess the number: "))
    if user_guess == num:
        print("Correct! Congraturation!")
        break
    else:
        print("you are wrong! Try again!")

