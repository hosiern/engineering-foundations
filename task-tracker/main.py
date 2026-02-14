def display_menu():
    print(f'\n *Task Tracker Main Menu*')
    print('')
    print(f'1- Create New Task')
    print(f'2- Delete Task')
    print(f'3- View Tasks')
    print(f'4- Exit Program')
    print('')
    user_input = input('Enter an option: ')
    print('')

def add_task():
    if user_input == '1':
        task_input = input('Enter your task name: ')
        tasks.append(task_input)
        print(f'--{task_input} successfully added to task list!')
        print('')

tasks = []

while True:
    
    
    elif user_input == '2':
        if not tasks:
            print(f'Task list is empty. Please create a new task to continue.')
            print('')
        else:
            print(f'Current task list:')
            print(tasks)
            print('')
            task_delete = input('Which task would you like to delete?: ')
            if task_delete in tasks:
                tasks.remove(task_delete)
                print(f'\n{task_delete} successfully removed.')
            else:
                print(f'\n{task_delete} not found. Please try again.')
    elif user_input == '3':
        if not tasks:
            print(f'Task list is empty. Please create a new task to continue.')
            print('')
        else:
            print(f'Current task list:')
            print(f'\n{tasks}')
    elif user_input == '4':
        break
    else:
        print(f'Invalid input, please try again.')
