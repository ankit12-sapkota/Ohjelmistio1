#Kirjoita while-toistorakennetta käyttävä ohjelma, 
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000
numbers = 1
while numbers <= 1000:
    if numbers % 3 == 0:
        print (numbers)
    numbers +=1
