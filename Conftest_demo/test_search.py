import pytest
from test_program import GoogleTitle


@pytest.mark.usefixtures('setUp')
class TestAutoSearchUsage:  # if 'Test' is not used before any name in the class name, then this program will not run. collected 0 items will come.

    @pytest.fixture(autouse=True)
    def test_title(self):
        self.ff = GoogleTitle()

    def test_A(self):
        self.ff.title()

    def test_B(self):
        self.ff.maximize()


