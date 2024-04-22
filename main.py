# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# See PyCharm help at https://www.jetbrains.com/help/pycharm/quick-start-guide.html

import sys
import os
import time
import datetime
import json
import logging
import pptx  # pip install python-pptx
# Documentation: https://python-pptx.readthedocs.io/en/latest/index.html
import docx  # pip install python-docx
# Documentation: https://python-docx.readthedocs.io/en/latest/index.html
import benford_programm

if __name__ == '__main__':
    # Create a logger
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # Get the current date and time
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print the current date and time
    print(f"Current date and time: {current_date_time}")

    logger.info(f"Current date and time: {current_date_time}")

    logger.info(f"Program started at: {current_date_time}")
    benford_programm.benford()
