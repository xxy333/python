from dataclasses import dataclass

@dataclass
class Students:
    name: str
    age: int
    city: str


student_list = []

while True:
    try:
        name_input = input("Zadejte jméno: ")
        age_input = int(input("Zadejte věk: "))
        city_input = input("Zadejte město: ")

        obj = Students(name_input, age_input, city_input)

        student_list.append(obj)
        repeat_val = input("Chcete pokračovat?(ano/ne): ")
        if repeat_val.lower() != "ano":
            break
        else:
            print("Zadejte dalšího studenta")

    except ValueError:
        print("Neplatná hodnota věku")
        break


for i, student_instances in enumerate(student_list):
    print("Jméno: ", student_instances.name)
    print("Věk: ", student_instances.age)
    print("Město: ", student_instances.city)







