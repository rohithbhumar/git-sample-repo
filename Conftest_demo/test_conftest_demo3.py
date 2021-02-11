import pytest


@pytest.mark.run(order=2)
def test_method_conf_E(one_time_setup):
    print('\nconf test method E')


@pytest.mark.run(order=1)
def test_method_conf_F():
    print('\nconf test method F')
