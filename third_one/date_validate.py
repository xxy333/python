import datetime



class Tasks:
    def __init__(self, task, describtion, date):
        self.task = task
        self.describtion = describtion
        self.date = date



def users_inputs():
    task_input = input("zadejte task: ")
    describtion_input = input("Zadejte popisek: ")
    date_input = input("Zadejte datum formát %d.%m.%Y: ")
    date = parse_date(date_input)


    if date is not None:
        obj = Tasks(task_input, describtion_input, date)
        print(f"zadný task {task_input}")
        print(f"zadný task {describtion_input}")
        print(f"zadný task {date_input}")
    else:
        print("Chybně zadaný datum")


def parse_date(date_input):
    try:
        date = datetime.datetime.strptime(date_input, "%d.%m.%Y")
        return date
    except ValueError:
        print("Formát datumu je neplatný")
        return None


users_inputs()