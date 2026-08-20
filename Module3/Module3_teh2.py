hyttiluokan = input("Antaa hyttiluokan;(LUX, A, B, C) ").upper()
if hyttiluokan == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokan == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokan == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokan == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virhellinen hyttiluokka!")