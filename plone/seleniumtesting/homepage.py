from basepage import BasePage
from loginoverlay import LoginOverlay

from selenium.webdriver.common.by import By
from collectionpageobject import CollectionEditPage

locators = {
    "login-link": [By.ID,"personaltools-login"],
    "edit-link": [By.ID,"personaltools-login"],
    "add-new-type": [By.ID, "plone-contentmenu-factories"],
    "add-new-collection": [By.ID, "topic"]
}

class HomePage(BasePage):
    """
    PageObject for the Home page
    """
    
    def __init__(self, selenium, portal):
        self.se = selenium
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

    def add_new_collection(self):
        """
        Adds a new Collection content type.

        ToDo: Create generic add_newType method.
        """
        self.se.find_element(*locators["add-new-type"]).click()
        self.se.find_element(*locators["add-new-collection"]).click()
        return CollectionEditPage(self.se)
        
