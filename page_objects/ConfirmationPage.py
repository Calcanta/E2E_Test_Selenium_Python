from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver
        self.elements = {
            'country_field': (By.ID, 'country'),
            'suggestions_list': (By.CLASS_NAME, 'suggestions'),
            'countries_list': (By.XPATH, '//div[@class="suggestions"]/ul'),
            'purchase_button': (By.CSS_SELECTOR, '.btn.btn-success.btn-lg'),
            'success_alert': (By.CSS_SELECTOR,'.alert.alert-success.alert-dismissible')
        }

    def country_field(self):
        return self.driver.find_element(*self.elements['country_field'])

    def suggestions_list(self):
        return self.elements['suggestions_list']

    def countries_list(self):
        return self.driver.find_elements(*self.elements['countries_list'])

    def purchase_button(self):
        return self.driver.find_element(*self.elements['purchase_button'])

    def success_alert(self):
        return self.driver.find_element(*self.elements['success_alert'])
