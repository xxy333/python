class Tasks:
    def __init__(self, task, describtion, date):
        self.task = task
        self.describtion = describtion
        self.date = date



task_list = []

task_input = "Prani"
describtion_input = "Vyndat pracku"
date_input = "Datum"

task_instance = Tasks(task_input, describtion_input, date_input)

task_list.append(task_instance)



