result = 0

while True:
    operator = input("Zadejte jakou operaci chcete použít (+, -, *, /)\n")
    if operator == "-":
        val_1 = input("Zvolil jste odčítání, zadejte první hodnotu: ")
        val_2 = input("Zadejte druhou hodnotu: ")
        result = int(val_1) - int(val_2)
        print(f"Výsledek je {result}" )
        break
        

    if operator == "+":
        val_1 = input("Zvolil jste sčítání, zadejte první hodnotu: ")
        val_2 = input("Zadejte druhou hodnotu: ")
        result = int(val_1) + int(val_2)
        print(f"Výsledek je {result}" )
        break

    if operator == "/":
        val_1 = input("Zvolil jste dělení, zadejte první hodnotu: ")
        val_2 = input("Zadejte druhou hodnotu: ")
        result = int(val_1) / int(val_2)
        print(f"Výsledek je {result}" )
        break

    if operator == "*":
        val_1 = input("Zvolil jste násobení, zadejte první hodnotu: ")
        val_2 = input("Zadejte druhou hodnotu: ")
        result = int(val_1) * int(val_2)
        print(f"Výsledek je {result}" )
        break
    else:
        print("Neplatné zadání, zkuste to znovu :)")
1
    

