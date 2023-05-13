import pathlib
from typing import Generator
import colorama

colorama.init()

white = colorama.Fore.LIGHTWHITE_EX
green = colorama.Fore.LIGHTGREEN_EX


def find_all_names(yaml_file: dict) -> Generator:
    if type(yaml_file) is not dict:
        yield None
        return None
    for body in yaml_file.values():
        for dict_ in body:
            if name := dict_.get('name'):
                yield name


def find_all_keys(yaml_file: dict) -> Generator:
    if type(yaml_file) is not dict:
        yield None
        return None
    for body in yaml_file.values():
        for dict_ in body:
            yield dict_


def list_command(yaml_file: dict, _type: str) -> None:
    names = find_all_names(yaml_file)
    print(f'list of available {_type}:')
    print(green + "--------------------")
    for name in names:
        print(white, name)
    print(green + "--------------------")
    print(f'end list of available {_type}')


def get_command(yaml_file: dict, name_to_find: str, type_arg: str) -> None:
    if type(yaml_file) is not dict:
        return None
    key_to_find = None
    dicts = find_all_keys(yaml_file)
    if type_arg == 'task':
        key_to_find = 'dependencies'
    elif type_arg == 'build':
        key_to_find = 'tasks'
    else:
        raise ValueError('Unknown type spec. Must be task or build')
    for dict_ in dicts:
        if name_to_find == dict_.get('name'):
            print(f"{green}{type_arg} info: ")
            print(f"{green}*{white} name: {name_to_find}")
            if dependencies := dict_.get(key_to_find):
                print(f"{green}* {white}{key_to_find}: {', '.join(dependencies)}")
            else:
                print(f"{green}* {white}{key_to_find}: {None}")
