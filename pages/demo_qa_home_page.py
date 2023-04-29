from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoQaHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com"

    def navigate_to(self):
        self.driver.get(self.url)

    def click_elements_card(self):
        elements_card = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h5[contains(text(), 'Elements')]"))
        )
        elements_card.click()
        return DemoQAElementsPage(self.driver)


class DemoQAElementsPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_page_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "elements-wrapper"))
        )
        return True
