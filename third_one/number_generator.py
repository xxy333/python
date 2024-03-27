import random


def random_generator():
    random_numbers = []
    i = 1
    while i < 50:
        random_number = random.randint(1, 740)
        random_numbers.append(random_number)
        i += 1

    sorted_numbers = sorted(random_numbers)
    return sorted_numbers




sorted_random_numbers = random_generator()
print(sorted_random_numbers)