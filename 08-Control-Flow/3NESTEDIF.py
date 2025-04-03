


ing1 = "pasta"
ing2 = "pesce"

if ing1 == "pasta":
    if ing2 == "carne":
        print("prepara pasta e carne")
    elif ing2 == "pesce":
        print("fai pasta e pesce")
    else:
        print("pasta e basta")


if ing1 == "pasta" and ing2 == "carne":
    print("pasta e carne")
elif ing1 == "pasta" and ing2 == "pesce":
    print("pasta e pesce")
