import inspect
import logging
from datetime import datetime

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    @staticmethod
    def get_logger(file_name: str = 'logfile'):
        # gett the name from which this method is being called, to avoid printing only this parent class name.
        logger_name = inspect.stack()[1][3]
        # Creating the logger object.
        logger = logging.getLogger(logger_name)
        # create the file handler object.
        execution_date_time = datetime.now()
        execution_dt_string = execution_date_time.strftime('_%d_%m_%Y-%Hh%Mm%Ss')
        file_handler = logging.FileHandler(
            f'C:/Users/HP/Documents/PyProjects/E2E_example/tests/logs/{file_name}{execution_dt_string}.log')
        # Define the format to log.
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        # Add the format to the file handler object.
        file_handler.setFormatter(formatter)
        # Add Handler to the logger.
        logger.addHandler(file_handler)  # filehandler object
        # Set Logging level
        logger.setLevel(logging.DEBUG)
        return logger

    @staticmethod
    def wait_for_element_presence(driver, locator, timeout=10):
        wait = WebDriverWait(driver, timeout)
        wait.until(expected_conditions.presence_of_element_located(locator))

    @staticmethod
    def select_option_by_text(element, text):
        sel = Select(element)
        sel.select_by_visible_text(text)
