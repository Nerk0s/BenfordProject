import sys
import os
import time
import datetime
import json
import logging
from logging import Logger
from venv import logger

import pptx  # pip install python-pptx
import docx  # pip install python-docx
import benfordslaw as bl


def setup():
    # Create a logger
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger(__name__)

    # Get the current date and time
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print the current date and time
    print(f"Current date and time: {current_date_time}")

    # Log the current date and time
    logger.info(f"Current date and time: {current_date_time}")

    # Log the Python version info
    logger.info(f"Python version info: {sys.version_info}")

    # Print the Python version info major
    print(f"Python version info major: {sys.version_info.major}")


def files_listing(file):
    for file in os.listdir(file):
        logger.info(f"File: {file}")


def benford():
    print("Benford Law \n Press Enter if you have pasted the files for verification if they follow Benford's Law:")
    str_input = input()
    if str_input == '':
        setup()

    # get the input path from the config file TODO Correct it
    with open('config.json') as f:
        data = json.load(f)
        if data['input_path'] != "":
            input_path = data['input_path']

    # get the files from the input path

    files = os.listdir(input_path)
    print(files)
    files_listing(files)

    # get the file extension
    file_extension = os.path.splitext(files[0])[1]
    print(file_extension)
