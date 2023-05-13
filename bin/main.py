import os
import pathlib
import yaml
import commands
import click

task_name = 'tasks.yaml'
build_name = 'builds.yaml'
current_dir = os.getcwd()


@click.group()
def cli():
    pass


def main():
    global task_name
    global build_name


@click.command()
@click.argument('_type')
def list_command(_type):
    task_file_path = pathlib.Path(current_dir, task_name)
    build_file_path = pathlib.Path(current_dir, build_name)
    if _type == 'builds':
        build_yaml = get_file(build_file_path)
        commands.list_command(build_yaml, _type)
    elif _type == 'tasks':
        task_yaml = get_file(task_file_path)
        commands.list_command(task_yaml, _type)
    else:
        print((f'Unknown type {_type}'))


@click.command()
@click.argument('_type')
@click.argument('name')
def get_command(_type: str, name: str) -> None:
    if name == None:
        print(f'No name provided')
    print(_type, name)
    task_file_path = pathlib.Path(current_dir, task_name)
    build_file_path = pathlib.Path(current_dir, build_name)
    if _type == 'build':
        build_yaml = get_file(build_file_path)
        commands.get_command(build_yaml, name, 'build')
    elif _type == 'task':
        task_yaml = get_file(task_file_path)
        commands.get_command(task_yaml, name, 'task')
    else:
        print(f'Unknown type {_type}')


def get_file(file_path: pathlib.Path) -> dict:
    if not file_path.is_file():
        print(f'{file_path} does not exist')
        exit(1)
    with open(file_path, 'r', encoding='utf8') as file:
        yaml_file = yaml.safe_load(file)
        return yaml_file


cli.add_command(list_command, name='list')
cli.add_command(get_command, name='get')

if __name__ == '__main__':
    cli()
