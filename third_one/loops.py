import random


generated_numbers = []
# generování náhodných 20 náhodných čísel pro range 1-500 čísel


while len(generated_numbers) < 20:
        random_int = random.randint(1,500)
        if random_int not in generated_numbers:
            generated_numbers.append(random_int)
        else:
            continue
generated_numbers.sort()

print(generated_numbers)








