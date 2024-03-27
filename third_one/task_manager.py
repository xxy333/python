import datetime


class Tasks:
    def __init__(self, task, description, date):
        self.task = task
        self.description = description
        self.date = date


def action_choosed(action):
    if action == "1":
        print("Vybral jste vytvoření nového úkolu: ")
        task_inputter()
    elif action == "2":
        print("Vybral jste operaci 2")
    elif action == "3":
        print("Vybral jste operaci 3")
    elif action == "4":
        print("Vybral jste operaci 4")
    elif action == "5":
        print("Vybral jste operaci 5")
    elif action == "6":
        print("Vybral jste operaci 6")


def task_inputter():
    task_input = input("Název: ")
    description_input = input("Popis: ")
    date_input = input("Datum splnění (dd.mm.yyyy): ")
    date = parse_date(date_input)

    if date is not None:
        obj = Tasks(task_input, description_input, date)
        print("Úkol vytvořen:")
        print("Název:", obj.task)
        print("Popis:", obj.description)
        print("Datum splnění:", obj.date.strftime("%d.%m.%Y"))
    else:
        print("Neplatně zadané datum.")


def parse_date(date_input):
    try:
        date = datetime.datetime.strptime(date_input, "%d.%m.%Y")
        return date
    except ValueError:
        print("Formát datumu je neplatný")
        return None


while True:
    action = input(
        "Vyberte akci:\n1. Vytvořit nový úkol\n2. Prohédnout úkoly\n3. Označit úkol jako hotový\n4. Upravit existující úkol\n5. Smazat úkol\n6. Filtrovat úkoly\n7. Konec\n")

    if action in ["1", "2", "3", "4", "5", "6"]:
        action_choosed(action)

    elif action == "7":
        break

    else:
        print("Neplatná volba")
