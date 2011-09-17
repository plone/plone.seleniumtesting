from basepage import BasePage
from selenium.webdriver.common.by import By

locators = {
    "workflow-content-menu": [By.XPATH, "//dl[@id='plone-contentmenu-workflow']//a"],
    "publish-action": [By.ID, "workflow-transition-publish"]
}

class BaseViewPage(BasePage):
    """
    """

    def __init__(self, selenium, portal):
        self.se = selenium
        self.portal = portal

    def publish(self):
        self.se.find_element(*locators["workflow-content-menu"]).click()
        self.se.find_element(*locators["publish-action"]).click()
