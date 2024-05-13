import logging
import os
from datetime import datetime
import json

config_path = 'C:\\Users\\vinsm\\PycharmProjects\\UIAUtomationPytest10May24\\config\\config.json'
def read_config(file_path=config_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config


config = read_config()


def setup_logger(test_name):
    # Create a logger
    logger = logging.getLogger(test_name)

    # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.INFO)

    # Create a logs directory at the root location if it doesn't exist
    log_dir = os.path.join(os.getcwd(), 'logs')

    # Create a log directory if it doesn't exist
    # log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    # Create a filename based on the test name and timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"{log_dir}/{test_name}_{timestamp}.log"

    # Create a file handler and set its format
    file_handler = logging.FileHandler(log_filename)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger
