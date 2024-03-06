import random

random_number_bot = 0
random_number_player = 0




while True:

    condition = input("Pokud chcete hrát a házet kostkou proti počítači napiště hraj!\n").lower
    random_number_player = random.randint(1,10)
    random_number_bot = random.randint(1,10)

    if condition == "hraj":

        continue
    if random_number_player > random_number_bot:



        print(f"Vyhrál jsi! Hodil si {random_number_player} a počítač hodil {random_number_bot}")
        break
    
    else:

        print(f"Bohužel si nevyhrál, hodil jsi {random_number_player} a počítač hodil {random_number_bot}")

    











