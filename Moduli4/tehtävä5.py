username = "python"
password = "rules"

i = 0
while i < 5:
    user = input("Enter your username: " )
    passi = input("Enter your password  ")

    if user == username and passi == password:
        print("Welcome")
        break
    else:
        print("Wrong credentials, TRY AGAIN")
        i += 1   
        
if i == 5:
    print("Access denied")