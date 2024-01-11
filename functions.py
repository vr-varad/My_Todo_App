def get_todos(filepath='todos.txt'):
    """takes a filepath and return the to-do list from the file."""
    with open(filepath, 'r') as fileName:
        todos_local = list(fileName.readlines())
    return todos_local


def write_todo(todos_arg, filepath='todos.txt'):
    """Writes a to-do list in the given filepath"""
    with open(filepath, 'w+') as filename:
        filename.writelines(todos_arg)


if __name__ == '__main__':
    print('functions.py is running alone.')