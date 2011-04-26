from seleniumwrapper import selenium_server_connection

class BaseElement(object):
    """Top of the PageObject element tree
    """
    pass


class BaseTextElement(BaseElement):
    """Base element class for Text fields
    """

    def __get__(self, obj, cls=None):
        se = selenium_server_connection.connection
        return str(se.find_element(*self.locator).text)

    def __set__(self, obj, val):
        se = selenium_server_connection.connection
        se.find_element(*self.locator).send_keys(val)
