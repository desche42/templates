import pathlib
import os

resources_path = pathlib.Path(__file__).parent.resolve()

def text_resource(path):
    "Reads file from mocks folder"
    with open(f'{resources_path}/{path}', "r", encoding="utf8") as mock_file:
        return mock_file.read()
