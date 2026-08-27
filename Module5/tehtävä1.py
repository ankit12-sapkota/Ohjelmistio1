#Tehtava 5
import random
dice = int(input("Enter the number of dice?"))
add = []
for i in range(dice):
    roll_dice = random.randint(1, 6)
    add.append(roll_dice)
    

print("The total sum of rolled dice is: ",(sum(add)) )


