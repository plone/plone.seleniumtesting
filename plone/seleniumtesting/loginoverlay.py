from selenium.webdriver.common.by import By

from baseoverlay import BaseOverlay
from loginpage import LoginPage, StatusMessageTextElement
from pageelements import BaseTextElement


locators = {
    "username": [By.NAME, "__ac_name"],
    "password": [By.NAME, "__ac_password"],
    "submit": [By.NAME, "submit"],
    "status_message": [By.CSS_SELECTOR, ".overlay dl.portalMessage:last-of-type dd"]
}


class StatusMessageTextElement(BaseTextElement):
    def __init__(self):
        self.locator = locators["status_message"]


class LoginOverlay(LoginPage, BaseOverlay):

    status_message = StatusMessageTextElement()
    
    def submit(self):
        """Override the LoginPage submit and wait until either a status message
        appears or the overlay closes."""
        self.se.find_element(*locators["submit"]).click()
        return self.wait_for_visible(locators["status_message"]) or self.isClosed()
