import random

num = random.randint(0, 50)
print("debug num is {}".format(num))
user_guess = int(input("Guess the number: "))
if user_guess == num:
    print("Correct! Congraturation!")
else:
    print("you are wrong! The answer is {}".format(num))

