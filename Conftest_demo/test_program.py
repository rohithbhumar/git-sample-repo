from selenium import webdriver


class GoogleTitle:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def title(self):
        self.driver.get('https://google.com')
        print(self.driver.title)

    def maximize(self):
        self.driver.get('https://google.com')
        self.driver.maximize_window()
        print('maximized')


# ff = GoogleTitle()
# ff.test_title()
# ff.test_maximize()
