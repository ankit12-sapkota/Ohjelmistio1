#Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
#  Write a main program that asks for a volume in gallons from the user and converts the value to liters. 
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

def converter(gasoline):
    liters = float(gasoline) * 3.785
    return liters



while True:
    gas = float(input("Enter the amount of gasoline to be converted? "))
    if gas >= 0:
        converted_gas = converter(gas)
        print(f"The {gas} in gallons is {converted_gas:.3f} liters.")
    else:
        print("Your number is negetive.")
        break
    

    
        

