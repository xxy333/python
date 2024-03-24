import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Příklad použití: Generuj heslo o délce 12 znaků
password = generate_password(12)
print(password)
