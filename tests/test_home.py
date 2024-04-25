import pytest

from navigation.Navigator import Navigator
from test_data.HomePageTestData import HomePageTestData
from utilities.BaseClass import BaseClass


class TestHome(BaseClass):
    driver = None

    def test_home(self, get_data):
        # Set Logger.
        logger = self.get_logger('test_home')
        # Expected results.
        expected_alert_text = 'Success!'
        logger.info(f'\n********** Test Data **********\n  - Name: {get_data["first_name"]}\n'
                    f'  - Email: {get_data["email"]}\n  - Gender: {get_data["gender"]}')
        # Define Navigator and homepage.
        logger.info(" - Starting Test at Home Page.")
        navigator = Navigator(self.driver)
        home_page = navigator.get_current_page()
        logger.info(f"Current Page - Home - Title: {navigator.get_current_page_title()}")
        logger.info(f"Current Page - Home - Url: {navigator.get_current_page_url()}")
        # Enter data in home page form.
        logger.info(f'- Enter name: {get_data["first_name"]}')
        home_page.name_field().send_keys(get_data["first_name"])
        logger.info(f'- Enter email: {get_data["email"]}')
        home_page.email_field().send_keys(get_data["email"])
        logger.info(f'- Check the "I like Icecream" checkbox.')
        home_page.icecream_check().click()
        self.select_option_by_text(home_page.gender_options(), get_data["gender"])
        # Submit form.
        logger.info(f'- Click on Submit button.')
        home_page.submit_button().click()
        # Verify alert Text.
        alert_text = home_page.success_alert().text
        logger.info(f"\n********** Success Alert Text ********** \n   - Expected text included: {expected_alert_text}"
                    f"\n   - Current text: {alert_text}")
        assert expected_alert_text in alert_text
        # Refresh page to restart test conditions.
        logger.info(" - Refresh page to restart test conditions.")
        self.driver.refresh()

    @pytest.fixture(params=HomePageTestData.get_test_data('test_case_2'))
    def get_data(self, request):
        return request.param
