import pytest

# @pytest.fixture()
# def setUp():
#     print('pytest fixture Setup')
#     yield
#     print('Tear down')


#call config method(called -> setUp) from conftest.py file and it will just use that

def test_method_conf_A(one_time_setup):
    print('\nconf test method A')


# calling one_time_setup method from conftest.py file and will be used accordingly.
def test_method_conf_B():
    print('\nconf test method B')
