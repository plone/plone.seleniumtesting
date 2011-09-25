from basepage import BasePage
from loginoverlay import LoginOverlay
from loginpage import LoginPage

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
        return LoginOverlay(self.se)
        
    def go_to_login_page(self):
        """
        Goes to the login page
        
        :returns: :class:`pages.LoginPage.LoginPage`
        """
        self.se.get('%s/login_form' % self.portal.absolute_url())
        return LoginPage(self.se)

    def add_new_collection(self):
        """
        Adds a new Collection content type.

        ToDo: Create generic add_newType method.
        """
        self.se.find_element(*locators["add-new-type"]).click()
        self.se.find_element(*locators["add-new-collection"]).click()
        return CollectionEditPage(self.se)
        
