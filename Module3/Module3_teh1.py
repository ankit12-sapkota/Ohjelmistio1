Kuha_pituus = int(input("Anna kuhan piitus centimetrina: "))

puutu_piitus = 37 - Kuha_pituus
if Kuha_pituus < 37:
    print(f"Kuha on {puutu_piitus}cm alimmasta sallitusta pyyntimitasta. Laske kuha takaisin järveen.")
else:
    print("kuha piitus on hyvää")