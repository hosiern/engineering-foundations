def display_menu():
    print(f'\n *Task Tracker Main Menu*')
    print('')
    print(f'1- Create New Task')
    print(f'2- Delete Task')
    print(f'3- View Tasks')
    print(f'4- Exit Program')
    print('')    

def add_task(tasks):
    task_input = input('Enter your task name: ')
    tasks.append(task_input)
    print(f'--{task_input} successfully added to task list!')
    print('')

def delete_task(tasks):
    if not tasks:
        print(f'Task list is empty. Please create a new task to continue.')
        return
        
    print(f'Current task list:')
    for i, task in enumerate(tasks, start=1):
        print(f'{i}. {task}')

    print('')
    user_input = input('Enter the task number to delete: ').strip()

    try:
        index = int(user_input)

        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f'\n{removed} successully removed.\n')
        else:
            print('\nInvalid task number, please try again.\n')

    except ValueError:
        print('\nPlease enter a valid task number.\n')

def view_tasks(tasks):
    if not tasks:
        print(f'Task list is empty. Please create a new task to continue.')
        print('')
    else:
        print(f'Current task list:')
        print(f'\n{tasks}')

def main():
    tasks = []  

    while True:
        display_menu()
        user_input = input('Enter an option: ').strip()
        print('')

        if user_input == '1':
            add_task(tasks)
        elif user_input == '2':
            delete_task(tasks)
        elif user_input == '3':
            view_tasks(tasks)
        elif user_input == '4':
            break
        else:
            print(f'Invalid input, please try again.')

if __name__ == "__main__":
    main()