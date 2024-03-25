import random
import string





def password_generator(length):
    signs = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(signs) for _ in range(length))
    return password



password = password_generator(12)
print(f"{password}")