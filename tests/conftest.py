import pytest
from selenium import webdriver

""""# Set webdriver options.
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--start-maximized')
# Create webdriver.
driver = webdriver.Firefox(options=firefox_options)"""
driver = None


def pytest_addoption(parser):
    """Add keys/options to run the test"""
    parser.addoption(
        '--browser_name', action='store', default='edge'
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    global firefox_options

    """Define pre and post conditions"""
    # Retrieve option value.
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'firefox':
        # Set webdriver options.
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--start-maximized')
        # Create webdriver.
        driver = webdriver.Firefox(options=firefox_options)
    elif browser_name == 'chrome':
        # Set webdriver options.
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        # Create webdriver.
        driver = webdriver.Chrome(options=chrome_options)
    else:
        # Set webdriver options.
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--start-maximized')
        # Create webdriver.
        driver = webdriver.Edge(options=edge_options)
    # Set implicit wait.
    driver.implicitly_wait(3)
    # Open url.
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            driver.get_screenshot_as_file(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
