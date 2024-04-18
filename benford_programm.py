import sys
import os
import time
import datetime
import json
import logging
import pptx  # pip install python-pptx
import docx  # pip install python-docx
import benfordslaw as bl


def setup():
    # Create a logger
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # Get the current date and time
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print the current date and time
    print(f"Current date and time: {current_date_time}")

    # Log the current date and time
    logger.info(f"Current date and time: {current_date_time}")

    # Print the command line arguments
    print(f"Command line arguments: {sys.argv}")

    # Log the command line arguments
    logger.info(f"Command line arguments: {sys.argv}")

    # Print the current working directory
    print(f"Current working directory: {os.getcwd()}")

    # Log the current working directory
    logger.info(f"Current working directory: {os.getcwd()}")

    # Print the environment variables
    print(f"Environment variables: {os.environ}")

    # Log the environment variables
    logger.info(f"Environment variables: {os.environ}")

    # Print the Python version
    print(f"Python version: {sys.version}")

    # Log the Python version
    logger.info(f"Python version: {sys.version}")

    # Print the Python path
    print(f"Python path: {sys.path}")

    # Log the Python path
    logger.info(f"Python path: {sys.path}")

    # Print the Python executable
    print(f"Python executable: {sys.executable}")

    # Log the Python executable
    logger.info(f"Python executable: {sys.executable}")

    # Print the Python version info
    print(f"Python version info: {sys.version_info}")

    # Log the Python version info
    logger.info(f"Python version info: {sys.version_info}")

    # Print the Python version info major
    print(f"Python version info major: {sys.version_info.major}")


def benford():
    input("Press Enter if you have pasted the files for verification if they follow Benford's Law")
    setup()

    #
