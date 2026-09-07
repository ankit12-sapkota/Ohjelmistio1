#Write a function that receives two parameters: the diameter of a round pizza in centimeters
#  and the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. 
# The main program asks the user to enter the diameter and price of two pizzas and 
# tells the user which pizza provides better value for money (which of them has a lower unit price).
#  You must use the function you wrote for calculating the unit prices.
import math

#Changing the centimeter diameter to the area in square meter
def pizza_area(diameter, price):
    cm_meter = diameter / 100  #cm to meter
    radius = cm_meter / 2
    area_square_meter = math.pi*(radius**2)
    unit_price = price / area_square_meter 
    return unit_price

def main():
        first_diameter = int(input("Enter the diameter of first prizza in centimeters: "))
        first_pizza_price = int(input("Enter the price of first pizza in euro. "))
        second_diameter = int(input("Enter the diameter of second in centimeters: "))
        second_pizza_price = int(input("Enter the price of second pizza in euro. "))

        first_unit_price = pizza_area(first_diameter, first_pizza_price)
        second_unit_price = pizza_area(second_diameter, second_pizza_price)

        if first_unit_price > second_unit_price:
              print(f"The second pizza is value for  money with the unit price of {second_unit_price:.2f} euro per square meter")
        elif first_unit_price == second_unit_price:
              print("The unit price of both pizza is same. ")
        
        else:
            print(f"The first pizza is value for  money with the unit price of {first_unit_price:.2f} euro per square meter")


main()


