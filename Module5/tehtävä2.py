numbers = []
while True:
    number = input("Enter number and press enter to exit: ")
    if number == "":
        break
    else:
        numbers.append(int(number))
numbers.sort(reverse=True)        
print("The highest five numbers are: ", numbers[0:5])