import random

number = random.randint(1 , 10)
while True:
    guessed_value = int(input("Guess the number between 1-10:"))
    if guessed_value == number:
        print("Correct")
        break
    elif guessed_value < number:
        print("Too low")
    elif guessed_value > number:
        print("Too high")
    else:
        print("Wrong input")