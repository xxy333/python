import random


random_number = 0
count_try = 0


while True:

    count_try += 1
    entered_number = input("Zahrajte si hru a zadejte číslo od 1 do 10, uvidíme jestli se trefíte!  ")
    random_number = random.randint(1,10)

    if int(entered_number) == random_number:
        print(f"Ano! Náhodné číslo je {entered_number} !! Gratuluji, náhodné číslo jste uhádl na {count_try} pokus!")
        break

    elif int(entered_number) > random_number:
        print(f"Bohužel, vložené číslo {entered_number} je větší než náhodné číslo {random_number}.")
        
        

    elif int(entered_number) < random_number:
        print(f"Bohužel, vložené číslo {entered_number} je menší než náhodné číslo {random_number}.")

    else:

        print("Vložte prosím validní")
        




