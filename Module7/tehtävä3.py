airports = { "EFHK": "Helsinki-Vantaa-Airport", "OMBD": "Dubai International Airport" }


while True:
    query = input("Enter acoordingly to your need:\n Enter(new) for new airports. \n Enter(exist) for existing airport \n Enter (quit) for quitting. ").lower()
    

    if query == "new":
        icao = input("Enter the ICAO code of the airport: ").upper()
        if icao in airports:
            print(f"Airport with conde {icao} already exist. with name {airports[icao]} ")
            continue

        new_airport = input("Enter the name of the airport: ")
        airports[icao] = (new_airport)
        continue

    elif query == "exist":
        icao_code = input("Enter the icao code of the airport: ").upper()

        if icao_code in airports:
            print(f'The airport with ICAO CODE ("{icao_code}") is "{airports[icao_code]}". ')
        else:
            print("Code not found in the database. ")
        continue

    elif query == "quit":
        break
    else:
        print("Wrong input")


                