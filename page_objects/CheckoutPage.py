from selenium.webdriver.common.by import By

from page_objects.ConfirmationPage import ConfirmationPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.elements = {
            'checkout': (By.XPATH, '//button[@class="btn btn-success"]')
        }

    def checkout(self):
        return self.driver.find_element(*self.elements['checkout'])

    def go_to_confirmation_page(self, navigator):
        checkout = self.checkout()
        checkout.click()
        navigator.set_current_page(ConfirmationPage(self.driver))
