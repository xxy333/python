def number_adder(numbers_add):
    numbers_count = sum(numbers_add)
    return numbers_count

data_numbers = [10, 15, 50, 16, 22, 13, 5]

print("Součet je: ", number_adder(data_numbers))

def number_max(numbers_high):
    numbers_high = max(numbers_high)
    return numbers_high


print("Největší číslo je: ", number_max(data_numbers))


def text_split():
    user_input = input("Zadejte slova oddělené mezerou: ").split()
    print("Zadaná slova byly: ", user_input)

text_split()





