from navigation.Navigator import Navigator
from utilities.BaseClass import BaseClass


class TestShop(BaseClass):
    driver = None

    def test_shop(self):
        # Set Logger.
        logger = self.get_logger('test_shop')
        # Expected results.
        expected_country = 'India'
        expected_product = 'Blackberry'
        expected_checkout = 'Checkout ( 1 )'
        expected_alert_visibility = True
        expected_alert_text = 'Success!'

        # Define Navigator and homepage.
        logger.info(" - Starting Test at Home Page.")
        navigator = Navigator(self.driver)
        home_page = navigator.get_current_page()
        logger.info(f"Current Page - Home - Title: {navigator.get_current_page_title()}")
        logger.info(f"Current Page - Home - Url: {navigator.get_current_page_url()}")
        # Go to Shop.
        home_page.go_to_shop(navigator)
        logger.info(" - Go To Shop Page.")
        shop_page = navigator.get_current_page()
        logger.info(f"Current Page - Shop - Title: {navigator.get_current_page_title()}")
        logger.info(f"Current Page - Shop - Url: {navigator.get_current_page_url()}")
        # Find the product and add it to the cart.
        logger.info(" - Selecting one product and adding it to cart.")
        products = shop_page.product_names()
        for product in products:
            title = product.text
            if title == expected_product:
                shop_page.product_add_button(product).click()
                break
        # Verify the product has been added to the checkout option.
        current_checkout_text = shop_page.checkout_button().text
        logger.info(f"\n********** Checkout Button Text ********** \n   - Expected text included: {expected_checkout}"
                    f"\n   - Current text: {current_checkout_text}")
        assert expected_checkout in current_checkout_text
        # Go to Checkout Page.
        logger.info(" - Go To Checkout Page.")
        shop_page.go_to_checkout_page(navigator)
        checkout_page = navigator.get_current_page()
        logger.info(f"Current Page - Checkout - Title: {navigator.get_current_page_title()}")
        logger.info(f"Current Page - Checkout - Url: {navigator.get_current_page_url()}")
        # Go to Confirmation Page
        logger.info(" - Go To Confirmation Page.")
        checkout_page.go_to_confirmation_page(navigator)
        confirmation_page = navigator.get_current_page()
        logger.info(f"Current Page - Confirmation - Title: {navigator.get_current_page_title()}")
        logger.info(f"Current Page - Confirmation - Url: {navigator.get_current_page_url()}")
        # Look for country.
        logger.info(" - Selecting Country.")
        confirmation_page.country_field().send_keys('Ind')
        self.wait_for_element_presence(self.driver, confirmation_page.suggestions_list())
        countries = confirmation_page.countries_list()
        # Select the desired country.
        for country in countries:
            name = country.text
            if name == expected_country:
                country.click()
                break
        # Verify the country has been selected.
        selected_country = confirmation_page.country_field().get_attribute('value')
        logger.info(f"\n********** Selected Country ********** \n   - Expected country: {expected_country}"
                    f"\n   - Current country: {selected_country}")
        assert selected_country == expected_country
        # Click on Purchase.
        logger.info(" - Press Purchase Button.")
        confirmation_page.purchase_button().click()
        success_alert_on = confirmation_page.success_alert().is_displayed()
        logger.info(f"\n********** Success alert visibility ********** \n   "
                    f"- Expected visibility: {expected_alert_visibility}"
                    f"\n   - Current visibility: {success_alert_on}")
        assert success_alert_on == expected_alert_visibility
        success_alert_text = confirmation_page.success_alert().text
        logger.info(f"\n********** Success alert text ********** \n   "
                    f"- Expected Text Included: {expected_alert_text}"
                    f"\n   - Current Text: {success_alert_text}")
        assert expected_alert_text in success_alert_text
