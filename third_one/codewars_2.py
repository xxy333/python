numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Print in one line without square brackets, commas, or extra whitespace


def create_phone_number(n):
    first_part = ''.join(map(str, numbers[:3]))
    second_part = ''.join(map(str, numbers[3:6]))
    third_part = ''.join(map(str, numbers[6:]))

    formated_phone_number = f"({first_part}) {second_part}-{third_part}"

    return formated_phone_number


phone_number = create_phone_number(numbers)
print(phone_number)