from selenium.webdriver.common.by import By

from page_objects.CheckoutPage import CheckoutPage


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.elements = {
            'product_name': (By.CLASS_NAME, "card-title"),
            'add_button': (By.XPATH, "//button[text()='Add ']"),
            'checkout_button': (By.XPATH, '//a[@class="nav-link btn btn-primary"]'),
        }

    def product_names(self):
        return self.driver.find_elements(*self.elements['product_name'])

    def product_add_button(self, product):
        return product.find_element(*self.elements['add_button'])

    def checkout_button(self):
        return self.driver.find_element(*self.elements['checkout_button'])

    def go_to_checkout_page(self, navigator):
        checkout = self.checkout_button()
        checkout.click()
        navigator.set_current_page(CheckoutPage(self.driver))
