#Write a function that gets a list of integers as a parameter. 
# The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed.
# For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.
def even_number(numbers):
    listing = []

    for number in numbers:
        if number % 2 == 0:
            listing.append(number)

    return listing    

number = []
def main():
    while True: 
        new_number = input("Enter the list of numbers or perss enter to exit: ")
        if new_number == "":
            break
        elif new_number <= "0":
            print("Enter number greater than zero: ")
            continue
        else:
            number.append(int(new_number))

main()             

print("The list of original numbers are as following: ", number)

print("The even number from the original list are: ", even_number(number))





             


    