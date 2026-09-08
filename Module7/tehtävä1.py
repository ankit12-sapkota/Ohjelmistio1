#Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). 
# Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.

season = ("Winter", "Spring", "Summer", "Autum")
month = int(input("Enter the month in number from (1-12) "))
if month == 12 or month == 1 or month == 2:
    print(f"Its {(season[0])} season")
elif month == 3 or month == 4 or month == 5:
    print(f"Its {(season[1])}")
elif month == 6 or month == 7 or month == 8:
    print(f"Its {(season[2])} season")
elif month == 9 or month == 10 or month == 11:
    print(f"Its {(season[3])} season")
else:
    print("Enter a valid number for month form (1-12)")

