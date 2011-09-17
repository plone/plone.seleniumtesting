from time import sleep
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from plone.seleniumtesting import TIMEOUT_SECONDS


class BasePage(object):

    def wait_for_visible(self, locator):

        for i in range(TIMEOUT_SECONDS):
            try:
                if self.se.find_element(*locator).is_displayed():
                   return True
            except (NoSuchElementException, StaleElementReferenceException):
                pass
            sleep(1)
        return False

    def wait_for_hidden(self, locator):

        for i in range(TIMEOUT_SECONDS):
            try:
                if self.se.find_element(*locator).is_displayed():
                    sleep(1)
                else:
                    return True
            except NoSuchElementException:
                pass
        return False

