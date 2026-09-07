import random
dices = []
def dice(random_dice):
    while True:
        rolled_dice = random.randint(1 , random_dice)
        if rolled_dice != random_dice:
            dices.append(rolled_dice)
        else:
            break
    return rolled_dice


dice_side = int(input("How many surface do you want the dice to have? "))

dice(dice_side)
print(f"It took {len(dices)} to get the maximum number.") 
for i  in dices:
    print(f"The number printed until the maximum numbers are {i}")   



