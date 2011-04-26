from basepage import BasePage
from pageelements import BaseTextElement
from selenium.webdriver.common.by import By
from seleniumwrapper import SeleniumWrapper as wrapper


locators = {
    "username": [By.NAME, "__ac_name"],
    "password": [By.NAME, "__ac_password"],
    "submit": [By.NAME, "submit"],
    "status_message": [By.CSS_SELECTOR, "dl.portalMessage:last-of-type dd"]
}


class UsernameElement(BaseTextElement):
    def __init__(self):
        self.locator = locators["username"]


class PasswordElement(BaseTextElement):
    def __init__(self):
        self.locator = locators["password"]


class StatusMessageTextElement(BaseTextElement):
    def __init__(self):
        self.locator = locators["status_message"]


class LoginPage(BasePage):
    
    username = UsernameElement()
    password = PasswordElement()
    status_message = StatusMessageTextElement()
    
    def __init__(self):
        self.se = wrapper().connection
        # TODO Make sure we really are on the login page
        # self.assertTrue("Forgot your password?" in self.se.get_page_source())

    def submit(self):
        self.se.find_element(*locators["submit"]).click()