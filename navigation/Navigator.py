from page_objects.HomePage import HomePage


class Navigator:

    def __init__(self, driver):
        self.driver = driver
        self.current_page = HomePage(self.driver)

    def set_current_page(self, page):
        self.current_page = page

    def get_current_page(self):
        return self.current_page

    def get_current_page_title(self):
        return self.driver.title

    def get_current_page_url(self):
        return self.driver.current_url
