from email.policy import default

import click

#def get_value(yaml_file: dict, searched_key: str) -> any:
#     if type(yaml_file) is not dict:
#         return None
#     if searched_key in yaml_file:
#         return yaml_file.get(searched_key)
#     for value in yaml_file.values():
#         if result := get_value(value, searched_key):
#             return result
#     else:
#         result = None
#     return result
@click.group()
def cli():
    pass


@click.command()
@click.argument('name')
def hello(name):
    click.echo(f"Hello {name}")


priorities = {
    'o': 'optional',
    'l': 'low',
    'h': 'high',
    'm': 'medium'
}


@click.command()
@click.argument('priority', type=click.Choice(priorities.keys()), default='m')
@click.argument('todofile', type=click.Path(exists=False), required=0)
@click.option('-n', '--name', prompt='Your name', help='Insert Your name')
@click.option('-d', '--desc', prompt='Your description', help='Insert Your description')
def add_todo(priority, todofile, name, desc):
    filename = todofile if todofile else 'todo.txt'
    with open(filename, 'a+') as f:
        f.write(f'{name} {desc} [PRIORITY: {priorities.get(priority)}]\n')


@click.command()
@click.argument('idx', type=click.INT, required=1)
def delete_todo(idx):
    with open('todo.txt', 'w+') as f:
        lines = f.readlines()
        lines.pop(idx)
        f.seek(0)
        f.writelines(lines)
        f.truncate()


@click.command()
@click.option('-p', '--priority', prompt='Your priority',
              help='Insert Your priority')
@click.argument('todofile', type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    filename = todofile if todofile else 'todo.txt'
    with open(filename, 'r') as f:
        todo_list = f.readlines()
        if priority is None:
            for idx, todo in enumerate(todo_list):
                print(f'{idx}: {todo}')
        else:
            for idx, todo in enumerate(todo_list):
                if f'[PRIORITY: {priorities.get(priority)}' in todo_list:
                    print(f'{idx}: {todo}')


cli.add_command(hello)
cli.add_command(add_todo)
cli.add_command(delete_todo)
cli.add_command(list_todos)


if __name__ == '__main__':
    cli()
