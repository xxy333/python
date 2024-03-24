def perform_operation(operator, val_1, val_2):
    if operator == "+":
        return int(val_1) + int(val_2)

    if operator == "-":
        return int(val_1) - int(val_2)
    
    if operator == "/":
        return int(val_1) / int(val_2)
    
    if operator == "*":
        return int(val_1) * int(val_2)
    
    else:
        return None
    

operator = input("zadejte jakou operaci chcete provést(+, -, /, *)")

if operator in ("+", "-", "/", "*"):
    val_1 = input("Zadejte první číslo")
    val_2 = input("Zadejte druhé číslo")
    result = perform_operation(operator, val_1, val_2)
    if result is not None:
        print(f"{result}")


    else:
        print("Neplatné zadání")

else:
    print("Neplatný operátor")
    