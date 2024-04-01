import string
import random


def password_generator(length):
    characters = string.punctuation + string.digits + string.ascii_letters
    password_generate = "".join(random.choice(characters)for _ in range(length))
    return password_generate




while True:
    try:
        add_variable = input("Zadejte počet znaků pro heslo: ")
        add_variable_int = int(add_variable)
        password = password_generator(add_variable_int)
        print(password)
        break

    except ValueError:
        print("Zadal jste neplatnou hodnotu")
        quit()






