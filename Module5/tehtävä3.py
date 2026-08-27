number = int(input("Enter a number to check if it is prime: "))
reminders = []
for n in range(2,number):
    divide = number % n
    reminders.append(divide)
if 0 in reminders:
    print("It is a composite number")

else:
    print("Its a prime number")




   