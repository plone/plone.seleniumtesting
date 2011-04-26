from basepage import BasePage
from loginoverlay import LoginOverlay

from seleniumwrapper import SeleniumWrapper as wrapper
from selenium.webdriver.common.by import By


locators = {
    "login-link": [By.ID,"personaltools-login"],
    "edit-link": [By.ID,"personaltools-login"]
}

class HomePage(BasePage):
    """
    PageObject for the Home page
    """
    
    def __init__(self, portal):
        self.se = wrapper().connection
        self.portal = portal
        
    def open_default_url(self):
        """
        Goes to the default url for this PO
        """
        self.se.get(self.portal.absolute_url())
    
    def login(self):
        self.se.find_element(*locators["login-link"]).click()
        return LoginOverlay()
        
    def go_to_login_page(self):
        """
        Goes to the login page
        
        :returns: :class:`pages.LoginPage.LoginPage`
        """
        self.se.find_element(*locators["login"]).click()
        return LoginPage()
