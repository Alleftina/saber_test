import configparser
import pathlib
import yaml
import os

# Initialize the configuration parser and read settings from the setting.ini file
setting = configparser.ConfigParser()
setting.read('setting.ini')

# Get the current working directory and set it in the setting.ini file
cwd = str(pathlib.Path.cwd())
try:
    setting.set('PATH', 'CURRENT_DIR', cwd)
except configparser.NoSectionError as e:
    print(f'Failed to set the new path')
with open('setting.ini', 'w') as setting_file:
    setting.write(setting_file)


def get_directory() -> pathlib.Path:
    """
    Get the current working directory or the directory specified in the setting.ini file.
    """
    # If the 'new_dir' option exists in the setting.ini file, use it as the current directory
    if setting.has_option('PATH', 'new_dir'):
        current_dir = setting.get('PATH', 'new_dir')
    # Otherwise, use the current working directory
    else:
        current_dir = cwd
    return pathlib.Path(current_dir)


def change_directory(new_dir: str) -> None:
    """
    Change the needed working directory to the specified directory and update the setting.ini file.
    """
    try:
        new_dir = pathlib.Path(new_dir)
        # Set the 'new_dir' option in the setting.ini file to the new directory
        setting.set('PATH', 'new_dir', str(new_dir))
        with open('setting.ini', 'w') as f:
            setting.write(f)
        print(f'Changed directory to {new_dir}')
    except configparser.NoSectionError as e:
        print(f'Failed to change directory, setting.ini is corrupt: {e}')
    except Exception as e:
        print(f'Failed to change directory: {e}')


def get_file_path(type_: str) -> pathlib.Path | None:
    """
    Get the file path for the specified file type (tasks or builds).
    """
    if type_ == 'task':
        task_file_path = pathlib.Path(get_directory(), setting.get('PATH', 'TASKS_FILE_NAME'))
        return task_file_path
    elif type_ == 'build':
        build_file_path = pathlib.Path(get_directory(), setting.get('PATH', 'BUILDS_FILE_NAME'))
        return build_file_path
    else:
        return None


def get_file_data(file_path: pathlib.Path) -> dict:
    """
    Load the YAML data from the specified file path.
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f'File not found: {file_path}')
        print(f'Use: app.py cfd path_to_file" to change file path, autoset path to current working directory')
        file_path_name = file_path.name
        file_path = pathlib.Path(cwd, file_path_name)
        if not os.path.isfile(file_path):
            print(f'File not found: {file_path}')
            print(f'Use: app.py cfd path_to_file" to change file path')
    # Load the YAML data from the file
    with open(file_path, 'r', encoding='utf8') as file:
        try:
            yaml_file = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f'Failed to parse YAML file: {file_path}')
            print(f'Error: {e}')
            exit(1)
        return yaml_file
