leviskoina = float(input("Anta Leiviskät: "))
nauloina = float(input("Antaa naulat: "))
luoteina = float(input("Anna luodit: "))
leiviskä = leviskoina * 20
naula = (leiviskä + nauloina) * 32
luoti = (naula + luoteina) * 13.3

kg = int(luoti // 1000)
gramma = luoti % 1000

print("Massa nykymittojen mukaan:")
print(f"{kg} kilogrammaa ja {gramma:.2f} grammaa.")
