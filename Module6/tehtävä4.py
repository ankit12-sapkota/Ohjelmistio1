#Write a function that gets a list of integers as a parameter.
#  The function returns the sum of all the numbers in the list. For testing,
#  write a main program where you create a list, call the function, and print out the value it returned.

def addition(numbers):
    added_total = sum(numbers)
    return added_total


Total = []
while True:
    number = input("Enter the numbers and enter to print the sum.")
    if number == "":
         break
        
    else:
        Total.append(int(number))
     
        
        
results = addition(Total)
print(f"The total sum of the given integer is: {results}")    
