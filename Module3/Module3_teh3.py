sukupuoli = input("Mikä on sukupuoli Mies tai Nainen?: ").lower()
hemoglobiiniarvo = int(input("Mitä on hemoglobiiiniarvon(g/l)"))
if sukupuoli == "nainen" and hemoglobiiniarvo <= 175 and hemoglobiiniarvo >= 117:
    print("Hemoglobiiniarvo on normaali")
elif sukupuoli == "nainen" and hemoglobiiniarvo < 117:
    print("Hemoglobiiniarvo on alainen")
elif sukupuoli == "nainen" and hemoglobiiniarvo > 175:
    print("Hemoglobiiniarvo on korkea")
elif sukupuoli == "mies" and hemoglobiiniarvo <=  195 and hemoglobiiniarvo >= 134:
    print("Hemoglobiiiniarvo on normaali")
elif sukupuoli == "mies" and hemoglobiiniarvo < 134:
    print("Hemoglobiiniarvo on alainen.")
elif sukupuoli == "mies" and hemoglobiiniarvo > 195:
    print("Hemoglobiniarvo on korkea")
else:
    print("Virhellinen syöte")