import random
rolled_dice = []
def dice():
    while True:
        
        new_dice = random.randint(1, 6)
        if new_dice != 6:
            rolled_dice.append(new_dice)
        else:
            break
    rolled_dice.append(6)    
    return rolled_dice
dice()
for i in rolled_dice:
    print(f"The rolled dice are as followed: {i}")



