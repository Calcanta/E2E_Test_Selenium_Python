from selenium.webdriver.common.by import By

from page_objects.ShopPage import ShopPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.elements = {
            'shop_link': (By.XPATH, "//a[text()='Shop']"),
            'name_field': (By.CSS_SELECTOR, 'input[name="name"]'),
            'email_field': (By.CSS_SELECTOR, 'input[name="email"]'),
            'icecream_check': (By.ID, 'exampleCheck1'),
            'gender_options': (By.ID, 'exampleFormControlSelect1'),
            'submit_button': (By.CSS_SELECTOR, 'input[type="submit"]'),
            'success_alert': (By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')
        }

    def shop_link(self):
        return self.driver.find_element(*self.elements['shop_link'])

    def go_to_shop(self, navigator):
        shop = self.shop_link()
        shop.click()
        navigator.set_current_page(ShopPage(self.driver))

    def name_field(self):
        return self.driver.find_element(*self.elements['name_field'])

    def email_field(self):
        return self.driver.find_element(*self.elements['email_field'])

    def icecream_check(self):
        return self.driver.find_element(*self.elements['icecream_check'])

    def gender_options(self):
        return self.driver.find_element(*self.elements['gender_options'])

    def submit_button(self):
        return self.driver.find_element(*self.elements['submit_button'])

    def success_alert(self):
        return self.driver.find_element(*self.elements['success_alert'])