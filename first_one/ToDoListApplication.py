

print("\nWelcome in To-Do LIST!\n----------------------\nHere u can work with your tasks. Choose your option.\n----------------------")


def get_last_task_number():

    try:
        with open('tasks.txt', 'r') as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                last_task_number_str = last_line.split('.')[0].strip()
                if last_task_number_str.isdigit():
                    return int(last_task_number_str)
            else:
                return 1
    except FileNotFoundError:
        return 1
    
def delete_tasks(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Zadejte číslo úkolu, který chcete smazat: "))
        if 1 <= task_index <= len(tasks):
            delete_task = tasks.pop(task_index - 1)
            print(f"Úkol '{delete_task}' byl úspěšně smazán.")

        else:
            print("Neplatné číslo úkolu. Zkuste to znovu.")
    except ValueError:
        print("Neplatný vstup. Zadejte číslo úkolu.")
        



    except FileNotFoundError:
        return 1


task_number = get_last_task_number() or 1

while True:
 
    operation = input("1. Add a task to scheduler\n2. See all your tasks\n3. Delete tasks\n4. Quit\n----------------------\n")
    if operation == "1":
        task = input("Napište, jaký by jste chtěli přidat úkol: ")
        with open('tasks.txt', 'a') as f:
            f.write(str(task_number) + "." + task + "\n")
            task_number += 1
        continue
    
    if operation == "2":
        with open('tasks.txt', 'r') as f:
            for line in f.readlines():
                print(line.strip())

        continue

    if operation == "3":

        delete_tasks(tasks)

    if operation == "4":
        break



'''
if operation == 1:
    task = input('What task would u like to add? ')
    with open('task-manager.txt', 'a') as f:
            f.write(operation + task + "\n")


else:
      quit'''