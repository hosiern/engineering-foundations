tasks = []

while True:
    print(f'\n *Task Tracker Main Menu*')
    print('')
    print(f'1- Create New Task')
    print(f'2- Delete Task')
    print(f'3- View Tasks')
    print(f'4- Exit Program')
    print('')
    user_input = input('Enter an option: ')
    print('')

    if user_input == '1':
        task_input = input('Enter your task name: ')
        tasks.append(task_input)
        print(f'--{task_input} successfully added to task list!')
        print('')
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
