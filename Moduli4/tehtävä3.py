Numbers = []
while True:
    number = input("Enter any number.(Empty string to quit): ")
    if number == "":
        break
    
    else:
        Numbers.append(number)
highest = max(Numbers)
lowest = min(Numbers)
print("THe highest number is:", highest)
print("The lowest number is: ", lowest)

        

    