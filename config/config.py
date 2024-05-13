import json

config_path = 'C:\\Users\\vinsm\\PycharmProjects\\UIAUtomationPytest10May24\\config\\config.json'
def read_config(file_path=config_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config


config = read_config()
