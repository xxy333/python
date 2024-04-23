# Data k uložení
data_to_save = [
    "První řádek",
    "Druhý řádek",
    "Třetí řádek"
]

# Cesta k souboru
file_path = "data.txt"

# Zápis dat do souboru
with open(file_path, "w") as file:
    for item in data_to_save:
        file.write(item + "\n")  # Oddělovač řádků

# Čtení dat ze souboru
data_from_file = []
with open(file_path, "r") as file:
    for line in file:
        data_from_file.append(line.strip())  # Odstranění znaku nového řádku

# Výpis načtených dat
print("Načtená data:")
for item in data_from_file:
    print(item)
