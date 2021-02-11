import pytest
from test_practice import Practice


@pytest.mark.usefixtures('setUp', 'one_time_setup')  # use this commonly for all methods below. These are coming from conftest.py
class TestDemo:  # if 'TestXxxx' is not used in the class name, then this program will not run
    """
    Below we are defining a method to import the class "Practice" so that I don't have to import to all the methods again.
    ex: ff = Practice() -> ff.add() again & again in all the methods.
    Using (autouse = 'True') -> This will be used automatically under all the below methods.
    """

    @pytest.fixture(autouse=True)
    def class_of_test_practice_py(self):
        self.ab = Practice(20, 10)
        # self.ab = Practice(a, b) -> check conftest.py file to pass values under certain condition. Lec-165(how to return value from fixtures)

    def test_method_A(self):
        self.ab.add()
        print('Method A')

    def test_method_B(self):
        self.ab.sub()
        print('Method B')


""" Run this file and also to create a report using pytest-html.pip3 install pytest-html (already installed)
So run -> 'py.test -s -v Conftest_demo/test_prac_conf.py --html=C:/Users/Admin/Desktop/html.html' in gitbash
"""
