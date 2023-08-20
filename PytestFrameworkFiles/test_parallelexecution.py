import pytest
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor

# Define browsers to be tested
browsers = ["chrome", "edge"]


def init_browser(browser):
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()

    return driver


class TestParallelBrowsers:

    drivers = None

    @classmethod
    def setup_class(cls):
        cls.drivers = []

        with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
            cls.drivers = list(executor.map(init_browser, browsers))

    @classmethod
    def teardown_class(cls):
        for driver in cls.drivers:
            driver.quit()

    def test_example_domain_title(self):
        for driver in self.drivers:
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            assert "Example Domain" in driver.title


if __name__ == "__main__":
    pytest.main(["-v", "test_parallelexecution.py"])
