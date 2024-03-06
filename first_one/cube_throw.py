import random
cube = [1, 2, 3, 4, 5, 6]
random_throw = 0
print("Vítejte ve hře KOSTKA! Pojďte zkusit štěstí :-)")


while True:
    user_input = input("Zkuste si hodit a uvidíme, jestli jste porazil/a/o počítač :). Napište házej: ").lower()

    if user_input == "házej":
        computer_throw = random.randint(1, 6)
        human_throw = random.randint(1, 6)
    #if computer_throw != human_throw:
        
    if computer_throw > human_throw:

        print(f"Počítáč hodil {computer_throw} a vy {human_throw} a proto jste prohrál :()")

    elif human_throw > computer_throw:

        print(f"Počítáč hodil {computer_throw} a vy {human_throw} a proto jste vyhrál!)")
    # else:
    #     stay = input("Chcete pokračovat? Zmáčkněte jakoukoliv klávesu mimo Q.").lower
    #     if stay == "Q":
    #         break
    #     else:
    #         continue

                    



#while True:



