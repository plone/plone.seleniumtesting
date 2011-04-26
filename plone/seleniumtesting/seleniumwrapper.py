from selenium.webdriver.firefox.webdriver import WebDriver


class SeleniumWrapper(object):
    
    # singleton
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self, *args):
        self.connection = WebDriver(*args)
        return self.connection