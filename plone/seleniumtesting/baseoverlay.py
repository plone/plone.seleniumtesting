from basepage import BasePage
from selenium.webdriver.common.by import By


locators = {
    "overlay": [By.CSS_SELECTOR, "div.overlay"],
    "close_overlay": [By.CSS_SELECTOR, "div.overlay .close"],
    "status_message":  [By.CSS_SELECTOR, ".overlay dl.portalMessage:last-of-type dd"]
}

class BaseOverlay(BasePage):
    
    def __init__(self):
        self.se = wrapper().connection
        return self.isOpen()
        
    def close(self):
        self.se.find_element(*locators["close_overlay"]).click()
        return self.isClosed()

    def isOpen(self):
        return self.wait_for_visible(locators['overlay'])    

    def isClosed(self):
        return self.wait_for_hidden(locators["overlay"])

