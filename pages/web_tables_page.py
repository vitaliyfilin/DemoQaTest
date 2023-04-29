import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class WebTablesPage(BasePage):
    ADD_RECORD_BTN_ID = "addNewRecordButton"
    FIRST_NAME_FIELD_ID = "firstName"
    LAST_NAME_FIELD_ID = "lastName"
    EMAIL_FIELD_ID = "userEmail"
    AGE_FIELD_ID = "age"
    SALARY_FIELD_ID = "salary"
    DEPARTMENT_FIELD_ID = "department"
    SUBMIT_BTN_ID = "submit"
    ROW_XPATH_TEMPLATE = "//div[@class='rt-tbody']//div[contains(text(),'{0}')]/ancestor::div[@role='row']"

    def _get_column_index(self, column_name):
        headers = self.driver.find_elements(By.XPATH, "//div[@class='rt-thead']//div[@role='row']")
        index = -1
        for i, header in enumerate(headers):
            if header.text == column_name:
                index = i
                break
        return index

    @allure.step("Create record")
    def create_new_record(self, first_name, last_name, email, age, salary, department):
        self.driver.find_element(By.ID, self.ADD_RECORD_BTN_ID).click()
        self.driver.find_element(By.ID, self.FIRST_NAME_FIELD_ID).send_keys(first_name)
        self.driver.find_element(By.ID, self.LAST_NAME_FIELD_ID).send_keys(last_name)
        self.driver.find_element(By.ID, self.EMAIL_FIELD_ID).send_keys(email)
        self.driver.find_element(By.ID, self.AGE_FIELD_ID).send_keys(age)
        self.driver.find_element(By.ID, self.SALARY_FIELD_ID).send_keys(salary)
        self.driver.find_element(By.ID, self.DEPARTMENT_FIELD_ID).send_keys(department)
        self.driver.find_element(By.ID, self.SUBMIT_BTN_ID).click()

    @allure.step("Verify record")
    def is_record_created(self, first_name, last_name, email, age, salary, department, ):
        row_xpath = self.ROW_XPATH_TEMPLATE.format(first_name)
        rows = self.driver.find_elements(By.XPATH, row_xpath)
        if not rows:
            return False
        row = rows[0]
        cells = row.find_elements(By.XPATH, "./div")
        cell_values = [cell.text for cell in cells][:-1]
        expected_values = [first_name, last_name, email, age, salary, department]
        return cell_values == expected_values

    @allure.step("Edit record")
    def edit_record(self, email, column_name, new_value):
        row_xpath = self.ROW_XPATH_TEMPLATE.format(email)
        row = self.driver.find_element(By.XPATH, row_xpath)
        editButton = row.find_element(By.XPATH, f"//descendant-or-self::span[@title='Edit']")
        editButton.click()
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[@placeholder='{column_name}']"))
        )
        input_element.clear()
        input_element.send_keys(new_value)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    @allure.step("Verify that record is edited")
    def is_record_edited(self, email, new_value):
        row_xpath = self.ROW_XPATH_TEMPLATE.format(email)
        row = self.driver.find_elements(By.XPATH, row_xpath)[0]
        cell_values = [cell.text for cell in row.find_elements(By.XPATH, ".//div[@role='gridcell']")]
        salary = cell_values[4]
        return salary.__eq__(new_value)

    @allure.step("Delete record")
    def delete_record(self, email):
        row_xpath = self.ROW_XPATH_TEMPLATE.format(email)
        row = self.driver.find_element(By.XPATH, row_xpath)
        deleteButton = row.find_element(By.XPATH, f"//descendant-or-self::span[@title='Delete']")
        deleteButton.click()

    @allure.step("Verify that record is deleted")
    def is_record_deleted(self, email):
        row_xpath = self.ROW_XPATH_TEMPLATE.format(email)
        rows = self.driver.find_elements(By.XPATH, row_xpath)

        for row in rows:
            email_element = row.find_elements(By.XPATH, f".//div[contains(text(), '{email}')]")
            if email_element:
                return False

        return True
