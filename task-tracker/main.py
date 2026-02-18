import json
from pathlib import Path

TASKS_FILE = Path(__file__).with_name('tasks.json')


def display_menu():
    print()
    print('*Task Tracker Main Menu*')
    print()
    print('1- Create New Task')
    print('2- Delete Task')
    print('3- View Tasks')
    print('4- Exit Program')
    print()


def add_task(tasks):
    task_input = input('Enter your task name: ').strip()
    if not task_input:
        print()
        print('Task name cannot be empty! Please try again.')
        print()
        return
    tasks.append(task_input)
    print()
    print(f'--{task_input} successfully added to task list!')
    print()


def delete_task(tasks):
    if not ensure_tasks_exist(tasks):
        return

    view_tasks(tasks)
    user_input = input('Enter the task number to delete: ').strip()

    try:
        index = int(user_input)

        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print()
            print(f'{removed} successfully removed.')
            print()
        else:
            print()
            print('Invalid task number, please try again.')
            print()

    except ValueError:
        print()
        print('Please enter a valid task number.')
        print()


def view_tasks(tasks):
    if not ensure_tasks_exist(tasks):
        return

    print('Current task list:')
    for i, task in enumerate(tasks, start=1):
        print(f'    {i}. {task}')

    print()


def ensure_tasks_exist(tasks):
    if not tasks:
        print('Task list is empty. Please create a new task to continue.')
        print()
        return False
    return True


def main():
    tasks = []

    while True:
        display_menu()
        user_input = input('Enter an option: ').strip()
        print()

        if user_input == '1':
            add_task(tasks)
        elif user_input == '2':
            delete_task(tasks)
        elif user_input == '3':
            view_tasks(tasks)
        elif user_input == '4':
            print('Exiting Task Tracker.')
            print()
            break
        else:
            print('Invalid input, please try again.')


if __name__ == "__main__":
    main()
