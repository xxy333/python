

obj = []

class Students:
    def __init__(self, name, surename, age):
        self.name = name
        self.surename = surename
        self.age = age



while True:
    try:
        names_input = input("zadejte jméno: ")
        surenames_input = input("zadejte příjmení: ")
        ages_input = int(input("zadejte věk: "))
        students_obj = Students(names_input, surenames_input, ages_input)
        obj.append(students_obj)


    except ValueError:
        print("neplatně zadaný věk, zadejte věk znovu")

    finally:
        print("hodnoty byly uloženy")
        new_value = input("Přejete si pokračovat?(ano/ne)")
        if new_value.lower() != "ano":
            break
        else:
         print("pokračujete s novým zadáním")

for i, student_instance in enumerate(obj):
    print(f"Záznam č. {i + 1}:")
    print("Jméno:", student_instance.name)
    print("Příjmení:", student_instance.surename)
    print("Věk:", student_instance.age)






