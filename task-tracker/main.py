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
    tasks.append({'description': task_input, 'done': False})
    save_tasks(tasks)
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
            save_tasks(tasks)
            print()
            print(f'{removed["description"]} successfully removed.')
            print()
        else:
            print()
            print('Invalid task number, please try again.')
            print()

    except ValueError:
        print()
        print('Please enter a valid task number.')
        print()


def mark_task_done(tasks):
    if not ensure_tasks_exist(tasks):
        return

    view_tasks(tasks)
    user_input = input('Enter task number to mark complete: ').strip()

    try:
        index = int(user_input)

        if 1 <= index <= len(tasks):
            tasks[index - 1]['done'] = True
            save_tasks(tasks)
            print()
            print(f'{tasks[index-1]['description']} marked complete.')
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
        status = '✓' if task['done'] else '✗'
        print(f'    {i}. [{status}] {task['description']}')

    print()


def ensure_tasks_exist(tasks):
    if not tasks:
        print('Task list is empty. Please create a new task to continue.')
        print()
        return False
    return True


def normalize_tasks(data):
    normalized = []

    for item in data:
        if isinstance(item, str):
            normalized.append({'description': item, 'done': False})
        elif isinstance(item, dict) and 'description' in item:
            normalized.append({
                'description': str(item['description']).strip(),
                'done': bool(item.get('done', False))
            })

    return normalized


def load_tasks():
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open('r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            return normalize_tasks(data)
        else:
            return []

    except (json.JSONDecodeError, OSError):
        print('Warning: tasks file is corrupted or unreadable. Creating new tasks file.')
        print()
        return []


def save_tasks(tasks):
    try:
        with TASKS_FILE.open('w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=2)

    except OSError:
        print('Error: could not save tasks.')
        print()


def main():
    tasks = load_tasks()

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
