while True:
    number = int(input("Enter the value in inches. Program ends when you enter negetive numbers."))
    if number > 0:
        centimeter = number * 2.54
        print("Value in centimeters:", centimeter)
    elif number < 0:
        break