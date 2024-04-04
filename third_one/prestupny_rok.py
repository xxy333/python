year = int(input("Zadejte jaký rok chcete zkontrlovat: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("jedná se přestupný rok")
        else:
            print("Nejedný se o přestupný rok")

    else:
        print("Jedná se o přestupný rok")

else:
    print("nejedná se o přestupný rok")