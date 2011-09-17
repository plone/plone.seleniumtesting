from basepage import BasePage
from selenium.webdriver.common.by import By

locators = {
    "default-tab": [By.ID,"fieldsetlegend-default"],
    "categorization-tab": [By.ID,"fieldsetlegend-categorization"],
    "dates-tab": [By.ID,"fieldsetlegend-dates"],
    "ownership-tab": [By.ID,"fieldsetlegend-ownership"],
    "settings-tab": [By.ID,"fieldsetlegend-settings"],
    "save": [By.NAME, "form.button.save"],
    "cancel": [By.NAME, "form.button.cancel"]
}


locators_cat = {
    "tags": [By.ID,"subject_keywords"],
    "related-items": [By.ID,""],
    "location": [By.ID,"location"],
    "language": [By.ID,"language"]
}

locators_dates = {
    "publishing-year": [By.ID, "edit_form_effectiveDate_0_year"],
    "publishing-month": [By.ID, "edit_form_effectiveDate_0_month"],
    "publishing-day": [By.ID, "edit_form_effectiveDate_0_day"],
    "publishing-hour": [By.ID, "edit_form_effectiveDate_0_hour"],
    "publishing-minute": [By.ID, "edit_form_effectiveDate_0_minute"],
    "publishing-ampm": [By.ID, "edit_form_effectiveDate_0_ampm"],
    "expiration-year": [By.ID, "edit_form_effectiveDate_1_year"],
    "expiration-month": [By.ID, "edit_form_effectiveDate_1_month"],
    "expiration-day": [By.ID, "edit_form_effectiveDate_1_day"],
    "expiration-hour": [By.ID, "edit_form_effectiveDate_1_hour"],
    "expiration-minute": [By.ID, "edit_form_effectiveDate_1_minute"],
    "expiration-ampm": [By.ID, "edit_form_effectiveDate_1_ampm"]
}
    
# ... etc., etc.


class BaseEditPage(BasePage):
    """
    """

    def __init__(self, selenium, portal):
        self.se = selenium
        self.portal = portal
        

    def save(self):
        self.se.find_element(*locators["save"]).click()
        
