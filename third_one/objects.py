



specie = []
class Species:
    def __init__(self, name, specie, age):
        self.name = name
        self.specie = specie
        self.age = age


while True:
    try:
        name_input = input("Zadejte jméno: ")
        specie_input = input("Zadejte druh: ")
        age_input = int(input("Zadejte věk: "))

        new_species = Species(name_input, specie_input, age_input)
        specie.append(new_species)
    except ValueError:
        print("Chyba: Neplatný vstup pro věk. Zadejte číslo. ")
    finally:
        continue_input = input("Chcete přidat další druh? (ano/ne): ")
        if continue_input.lower() != "ano":
            break

for i, species_instance in enumerate(specie):
    print(f"Druh {i + 1}:")
    print("Jmeno", species_instance.name)
    print("Druh", species_instance.specie)
    print("Věk", species_instance.age)