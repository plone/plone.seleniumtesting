#from seleniumwrapper import selenium_server_connection

class BaseElement(object):
    """Top of the PageObject element tree
    """

    def __get__(self, obj, cls=None):
        return None

    def __set__(self, obj, val):
        pass



class BaseTextElement(BaseElement):
    """Base element class for Text fields
    """

    def __init__(self, selenium):
        self.se = selenium

    #def __get__(self, obj, cls=None):
    #    return str(self.se.find_element(*self.locator).text)
    #
    #def __set__(self, obj, val):
    #    self.se.find_element(*self.locator).send_keys(val)

    def get(self):
        return str(self.se.find_element(*self.locator).text)

    def set(self, val):
        self.se.find_element(*self.locator).send_keys(val)

class BaseCheckboxElement(BaseElement):
    """Base element class for Checkbox fields
    """

    def __init__(self, selenium):
        self.se = selenium
    
    def check(self):
        if not self.se.find_element(*self.locator).is_selected():
            self.se.find_element(*self.locator).click()

    def uncheck(self):
        if self.se.find_element(*self.locator).is_selected():
            self.se.find_element(*self.locator).click()

    def isChecked(self):
        return self.se.find_element(*self.locator).is_selected()

class BaseInAndOutElement(BaseElement):
    """Base element class for In and Out widget
    """

    def __init__(self, selenium):
        self.se = selenium

    def selectOptions(self):
        pass

    def deselectOptions(self):
        pass

    def addSelectedOptions(self):
        pass

    def removeSelectedOptions(self):
        pass

    def addKeywordsByText(self, options):
        """
        """

        optionsList = self.se.find_element(*self.locator['optionsList'])
        # Select keywords
        for opt in options:
            optionsList.find_element_by_xpath("./option[@text='%s']" % opt).click()

        # Click to add options
        self.se.find_element(*self.locator['optionsList-to-chosenList-btn']).click()
    
    def addKeywordsByValue(self, options):
        """
        """

        optionsList = self.se.find_element(*self.locator['optionsList'])
        # Select keywords
        for opt in options:
            optionsList.find_element_by_xpath("./option[@value='%s']" % opt).click()

        # Click to add options
        self.se.find_element(*self.locator['optionsList-to-chosenList-btn']).click()
    
    def removeKeywords(self, options):
        pass

class BaseSelectElement(BaseElement):
    """Base element class for Select fields
    """

    def __init__(self, selenium):
        self.se = selenium

    def selectOptionByValue(self, option):
        selectionList = self.se.find_element(*self.locator)
        selectionList.find_element_by_xpath("./option[@value='%s']" % option).click()
