vuosi = int(input("Anna vuosi: "))

if vuosi == 2020:
    print("Ei ollut olympialasia vuonna koronan takia")
elif vuosi == 2021:
    print("Oli olumpiavuosi poikkeuksellisesti.")
elif vuosi == 1916:
    print("Cancelled due to world war first")
elif vuosi == 1940 or vuosi == 1944:
    print("Cancelled due to world war 2")
elif vuosi % 4 == 0:
    print("Oli olympiavuosi")
else: 
    print("Ei oli olumpiavuosi.")