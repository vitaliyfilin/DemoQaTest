import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'firstName')
    LAST_NAME_INPUT = (By.ID, 'lastName')
    EMAIL_INPUT = (By.ID, 'userEmail')
    GENDER_MALE_RADIO = (By.XPATH, "//label[@for='gender-radio-1']")
    GENDER_FEMALE_RADIO = (By.XPATH, "//label[@for='gender-radio-2']")
    GENDER_OTHER_RADIO = (By.XPATH, "//label[@for='gender-radio-3']")
    MOBILE_INPUT = (By.ID, 'userNumber')
    DATE_OF_BIRTH_INPUT = (By.ID, 'dateOfBirthInput')
    HOBBIES_SPORTS_CHECKBOX = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    HOBBIES_READING_CHECKBOX = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    HOBBIES_MUSIC_CHECKBOX = (By.XPATH, "//label[@for='hobbies-checkbox-3']")
    CURRENT_ADDRESS_INPUT = (By.ID, 'currentAddress')
    STATE_DROPDOWN = (By.XPATH, "//*[contains(text(), 'Select State')]")
    CITY_DROPDOWN = (By.ID, 'city')
    SUBMIT_BUTTON = (By.ID, 'submit')

    def fill_form(self, first_name, last_name, email, gender, mobile, date_of_birth, hobbies, current_address, state,
                  city):
        self.enter_name(first_name, last_name)
        self.enter_email(email)
        self.select_gender(gender)
        self.enter_mobile(mobile)
        self.enter_date_of_birth(date_of_birth)
        self.select_hobbies(hobbies)
        self.enter_current_address(current_address)
        self.select_state(state)
        self.select_city(city)
        self.submit_form()

    @allure.step("Enter name")
    def enter_name(self, first_name, last_name):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)

    @allure.step("Enter email")
    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    @allure.step("Select gender")
    def select_gender(self, gender):
        if gender == 'male':
            self.click(self.GENDER_MALE_RADIO)
        elif gender == 'female':
            self.click(self.GENDER_FEMALE_RADIO)
        else:
            self.click(self.GENDER_OTHER_RADIO)

    @allure.step("Enter mobile phone")
    def enter_mobile(self, mobile):
        self.send_keys(self.MOBILE_INPUT, mobile)

    @allure.step("Enter date of birth")
    def enter_date_of_birth(self, date_of_birth):
        self.click(self.DATE_OF_BIRTH_INPUT)
        self.send_keys(self.DATE_OF_BIRTH_INPUT, Keys.CONTROL + "a")
        self.send_keys(self.DATE_OF_BIRTH_INPUT, date_of_birth)

    @allure.step("Select hobbies")
    def select_hobbies(self, hobbies):
        for hobby in hobbies:
            if hobby == 'sports':
                self.click(self.HOBBIES_SPORTS_CHECKBOX)
            elif hobby == 'reading':
                self.click(self.HOBBIES_READING_CHECKBOX)
            else:
                self.click(self.HOBBIES_MUSIC_CHECKBOX)

    @allure.step("Enter current address")
    def enter_current_address(self, current_address):
        self.send_keys(self.CURRENT_ADDRESS_INPUT, current_address)

    @allure.step("Select state")
    def select_state(self, state):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.click(self.STATE_DROPDOWN)
        self.click((By.XPATH, f"//div[text()='{state}']"))

    @allure.step("Select city")
    def select_city(self, city):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.click(self.CITY_DROPDOWN)
        self.click((By.XPATH, f"//div[text()='{city}']"))

    @allure.step("Submit form")
    def submit_form(self):
        self.click((By.XPATH, f"//*[contains(@class, 'tlfecz')][1]"))
        self.click(self.SUBMIT_BUTTON)
