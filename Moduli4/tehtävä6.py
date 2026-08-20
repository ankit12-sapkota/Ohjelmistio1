import random
initial_points = 0
numbers = int(input("How many random points to generate: "))

i = 0
while i < numbers:
    x = random.uniform(-1 , 1)
    y = random.uniform(1 , -1 )

    if x**2 + y**2 < 1:
        initial_points += 1

    i += 1

#n/N= pi/4       
#pi = 4 * n/N
pi = 4 * initial_points / numbers
print("Approximation of pi is:", pi)

