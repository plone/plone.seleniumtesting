from basepage import BasePage
from baseedit import BaseEditPage
from baseview import BaseViewPage
from pageelements import BaseTextElement, BaseCheckboxElement
from pageelements import BaseInAndOutElement, BaseSelectElement

from selenium.webdriver.common.by import By


locators = {
    # Collection Edit Page
    "title-ID": [By.ID, "title"],
    "title": [By.XPATH, "//input[@id='title']"],
    "description": [By.ID, "description"],
    "display-as-table-checkbox": [By.NAME, "customView:boolean"],
    "table-columns": {
        "optionsList": [By.ID, "customViewFields_options"],
        "optionsList-to-chosenList-btn": [By.XPATH, "//div[@id='archetypes-fieldname-customViewFields']//input[@class='context'][last()-1]"],
        "chosenList-to-optionsList-btn": [By.XPATH, "//div[@id='archetypes-fieldname-customViewFields']//input[@class='context'][last()]"],
        "chosenList": [By.ID, "customViewFields"] },
    "save": [By.NAME, "form.button.save"],

    # Collection View Page
    "criteria-tab": [By.XPATH, "//*[@id='contentview-criteria']//a"],
    "view-tab": [By.XPATH, "//*[@id='contentview-view']//a"],
    "collection-results": [By.XPATH, "//table[attribute::class='listing']/tbody/tr"],
    "collection-result-headers": [By.XPATH, "//table[attribute::class='listing']/thead/tr/th"],
    
    # Collection Criteria
    "criteria-field-name": [By.XPATH, "//*[@id='field']"],
    "criteria-type": [By.XPATH, "//*[@id='criterion_type']"],
    "add-criteria-btn": [By.NAME, "form.button.AddCriterion"],
    "title-criteria-detail-value": [By.ID, "crit__Title_ATSimpleStringCriterion_value"],
    "save-criteria-details": [By.NAME, "form.button.Save"]
    
}


# Collection Edit Page

class TitleElement(BaseTextElement):

    def __init__(self, selenium):
        self.se = selenium
        self.locator = locators["title"]
    
class DescriptionElement(BaseTextElement):

    def __init__(self, selenium):
        self.se = selenium
        self.locator = locators["description"]
    
class DisplayAsTableElement(BaseCheckboxElement):

    def __init__(self, selenium):
        self.se = selenium
        self.locator = locators["display-as-table-checkbox"]

class TableColumnsElement(BaseInAndOutElement):

    def __init__(self, selenium):
        self.se = selenium
        self.locator = locators["table-columns"]

class CollectionEditPage(BaseEditPage):
    """
    """

    def __init__(self, selenium):
        self.se = selenium

        self.title = TitleElement(selenium)
        self.description = DescriptionElement(selenium)
        self.display_as_table = DisplayAsTableElement(selenium)
        self.table_columns = TableColumnsElement(selenium)

    def save(self):
        self.se.find_element(*locators["save"]).click()
        return CollectionViewPage(self.se)


# Collection View Page

class CollectionViewPage(BaseViewPage):
    """
    """

    def __init__(self, selenium):
        self.se = selenium

    def setCriteria(self):
        self.se.find_element(*locators["criteria-tab"]).click()
        return CollectionCriteriaPage(self.se)

    def viewCollection(self):
        self.se.find_element(*locators["view-tab"]).click()
        
    def getCollectionResults(self):
        return self.se.find_elements(*locators["collection-results"])

    def isColumnDisplayed(self, opt):
        headers =  self.se.find_elements(*locators["collection-result-headers"])
        for header in headers:
            if opt == header.text:
                return True            
        return False
        

# Collection Criteria Page

class CriteriaFieldNameElement(BaseSelectElement):

    def __init__(self, selenium):
        self.se = selenium
        self.locator = locators["criteria-field-name"]

class CriteriaTypeElement(BaseSelectElement):

    def __init__(self, selenium):
        self.se = selenium
        self.locator = locators["criteria-type"]


class CollectionCriteriaPage(BasePage):
    """
    """

    def __init__(self, selenium):
        self.se = selenium

        self.criteriafieldname = CriteriaFieldNameElement(self.se)

    def addCriteria(self):
        self.se.find_element(*locators["add-criteria-btn"]).click()


    def setCriteriaDetail(self, ctype, cvalue):

        if ctype == "Title":
            self.se.find_element(*locators["title-criteria-detail-value"]).send_keys(cvalue)
            
        #elif == so other criteria type
        #    ToDo
        
    def saveCriteriaDetails(self):
        self.se.find_element(*locators["save-criteria-details"]).click()
