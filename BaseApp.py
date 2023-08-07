from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://only.digital/projects#brief'

        self.actions = ActionChains(self.driver)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_base_site(self):
        return self.driver.get(self.base_url)
