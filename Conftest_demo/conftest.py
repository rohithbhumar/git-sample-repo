"""
Instead of using @pytest.fixture to every file. We use a concept of conftest.py to have a common place for use
"""

import pytest
from selenium import webdriver


@pytest.fixture()
def setUp():
    print('\npytest fixture Setup')
    yield
    print('\nTear down')


@pytest.fixture(scope='module')
def one_time_setup(browser, request):
    print('\nOnly one time setup for a full module and not for all TCs/methods')
    if browser == 'firefox':
        # a = 20
        # b = 10
        driver_ff = webdriver.Firefox(executable_path="C:\\Users\\Admin\\geckodriver.exe")
        print('Open Firefox')
        driver_ff.get('https://google.com')
    else:
        # a = 30
        # b = 20
        driver = webdriver.Chrome()
        print('Open Chrome')
        driver.get('https://www.google.com')
    # if request.module is not None:
    #     request.module.a = a
    #     request.module.b = b

    # yield a, b
    yield
    print('\nOnly one time tear down for a full module and not for all TCs/methods')

# ---------------------------------------------------------------------------- #


# this is to add option from command line for using platform ex: --udid = 43.88.90.82
def pytest_addoption(parser):
    # it should be pytest_addoption only. https://www.udemy.com/course/selenium-webdriver-with-python3/learn/lecture/5277884#questions/2474582
    parser.addoption("--browser")


# this is to communicate with pytest_addoption
@pytest.fixture(scope='module')
def browser(request):
    return request.config.getoption("--browser")
