import sys
import click
sys.path.append('..')
import bin.commands as commands
import bin.directories as directories


# Create a Click group
@click.group()
def cli():
    pass


# Create a Click command to change the current working directory
@click.command()
@click.argument(r'path', type=click.Path(exists=True, file_okay=False))
def change_filedir_command(path: str) -> None:
    """
       Change the file directory to the specified path.
    """
    # Call the 'change_directory' function from the 'directories' module to change the current directory
    directories.change_directory(path)
    # Display a message to the user indicating that the directory was changed


# Create a Click command to list all tasks or builds
@click.command()
@click.argument('type_')
def list_command(type_: str) -> None:
    """
    List all tasks or builds.
    """
    # Get the path to the appropriate YAML file based on the user's choice of 'type'
    file_path = directories.get_file_path(type_)
    if type_ == 'build':
        # If the user chose 'builds', get the data from the corresponding YAML file using the 'get_file_data' function
        build_yaml = directories.get_file_data(file_path)
        # Call the 'list_command' function from the 'commands' module to display the list of builds
        commands.list_command(build_yaml, type_)
    elif type_ == 'task':
        # If the user chose 'tasks', get the data from the corresponding YAML file using the 'get_file_data' function
        task_yaml = directories.get_file_data(file_path)
        # Call the 'list_command' function from the 'commands' module to display the list of tasks
        commands.list_command(task_yaml, type_)
    else:
        # If the user entered an invalid value for 'type_', display an error message
        click.echo(f'Unknown type {type_}')
        click.echo(f'Type must be builds or tasks')


# Create a Click command to get a specific task or build by name
@click.command()
@click.argument('type_')
@click.argument('name')
def get_command(type_: str, name: str) -> None:
    """
    Get a specific task or build by name.
    """
    if name is None:
        # If the user did not enter a name, display an error message
        print(f'No name provided')
    # Get the path to the appropriate YAML file based on the user's choice of 'type'
    file_path = directories.get_file_path(type_)
    if type_ == 'build':
        # If the user chose 'build', get the data from the corresponding YAML file using the 'get_file_data' function
        build_yaml = directories.get_file_data(file_path)
        # Call the 'get_command' function from the 'commands' module to display the details of the specified build
        commands.get_command(build_yaml, name, 'build')
    elif type_ == 'task':
        # If the user chose 'task', get the data from the corresponding YAML file using the 'get_file_data' function
        task_yaml = directories.get_file_data(file_path)
        # Call the 'get_command' function from the 'commands' module to display the details of the specified task
        commands.get_command(task_yaml, name, 'task')
    else:
        # If the user entered an invalid value for 'type_', display an error message
        click.echo(f'Unknown type {type_}')
        click.echo(f'Type must be build or task')


# Add the commands to the Click group
cli.add_command(list_command, name='list')
cli.add_command(get_command, name='get')
cli.add_command(change_filedir_command, name='cfd')

if __name__ == '__main__':
    cli()
