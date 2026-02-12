tasks = []

while True:
    print(f'*Task Tracker Main Menu*')
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
