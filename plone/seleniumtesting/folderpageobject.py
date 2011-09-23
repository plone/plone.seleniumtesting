from basepage import BasePage
from pageelements import BaseTextElement
from selenium.webdriver.common.by import By

locators = {
    "contents-tab": [By.XPATH, "//*[@id='contentview-folderContents']//a"],
    "edit-tab": [By.XPATH, "//*[@id='contentview-edit']//a"],
    "title": [By.XPATH, "//input[@id='title']"],
    "save-edit": [By.NAME, "form.button.save"],
    "folder-contents": [By.XPATH, "//table[@id='listing-table']//tbody/tr"],
    "content-item-checkbox": [By.XPATH, "*/input[@type='checkbox']"],
    "cut-folder-content": [By.NAME, "folder_cut:method"],
    "copy-folder-content": [By.NAME, "folder_copy:method"],
    "paste-folder-content": [By.NAME, "folder_paste:method"]
}


class FolderPageObject(object):
    """
    """

    def __init__(self, selenium):
        self.se = selenium

        self.contents = FolderContentsTab(self.se)
        self.edit = FolderEditTab(self.se)
        
    def goto_contents_tab(self):
        self.se.find_element(*locators['contents-tab']).click()

    def goto_edit_tab(self):
        self.se.find_element(*locators['edit-tab']).click()

class FolderContentsTab(BasePage):
    """
    """

    def __init__(self, selenium):
        self.se = selenium

    
    def selectFolderItemByPostition(self, position):
        contents = self.se.find_elements(*locators['folder-contents'])
        itemCheckbox = contents[position].find_element(*locators['content-item-checkbox'])
        if not itemCheckbox.is_selected():
            itemCheckbox.click()

    def numItems(self):
        contents = self.se.find_elements(*locators['folder-contents'])
        return len(contents)
        
    def cut(self):
        self.se.find_element(*locators['cut-folder-content']).click()

    def copy(self):
        self.se.find_element(*locators['copy-folder-content']).click()

    def paste(self):
        self.se.find_element(*locators['paste-folder-content']).click()



class TitleElement(BaseTextElement):

    def __init__(self, selenium):
        self.se = selenium
        self.locator = locators["title"]
    
class FolderEditTab(BasePage):
    """
    """

    def __init__(self, selenium):
        self.se = selenium

        self.title = TitleElement(self.se)

    def save(self):
        self.se.find_element(*locators['save-edit']).click()
