import allure

from pages.practice_form_page import PracticeFormPage
from tests.base_test import BaseTest


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("DemoQA tests")
@allure.feature("Practice form tests")
class PracticeFormTest(BaseTest):
    page_class = PracticeFormPage
    page_url = 'https://demoqa.com/automation-practice-form'

    @allure.description("fill form")
    @allure.title("Fill form to see if all elements are present")
    @allure.story("As a user I want to be able to fill form with required data")
    def test_fill_form(self):
        self.page_class.fill_form(
            self.page,
            'John',
            'Doe',
            'johndoe@example.com',
            'male',
            '1234567890',
            '01 May 2000',
            ['sports', 'reading'],
            '123 Main St',
            'NCR',
            'Delhi'
        )
        with self.subTest("Check input fields are not None"):
            self.assertIsNotNone(self.page_class.FIRST_NAME_INPUT, "FIRST_NAME_INPUT should not be None")
            self.assertIsNotNone(self.page_class.LAST_NAME_INPUT, "LAST_NAME_INPUT should not be None")
            self.assertIsNotNone(self.page_class.EMAIL_INPUT, "EMAIL_INPUT should not be None")
            self.assertIsNotNone(self.page_class.GENDER_MALE_RADIO, "GENDER_MALE_RADIO should not be None")
            self.assertIsNotNone(self.page_class.GENDER_FEMALE_RADIO, "GENDER_FEMALE_RADIO should not be None")
            self.assertIsNotNone(self.page_class.GENDER_OTHER_RADIO, "GENDER_OTHER_RADIO should not be None")
            self.assertIsNotNone(self.page_class.MOBILE_INPUT, "MOBILE_INPUT should not be None")
            self.assertIsNotNone(self.page_class.DATE_OF_BIRTH_INPUT, "DATE_OF_BIRTH_INPUT should not be None")
            self.assertIsNotNone(self.page_class.HOBBIES_SPORTS_CHECKBOX, "HOBBIES_SPORTS_CHECKBOX should not be None")
            self.assertIsNotNone(self.page_class.HOBBIES_READING_CHECKBOX, "HOBBIES_READING_CHECKBOX should not be None")
            self.assertIsNotNone(self.page_class.HOBBIES_MUSIC_CHECKBOX, "HOBBIES_MUSIC_CHECKBOX should not be None")
            self.assertIsNotNone(self.page_class.CURRENT_ADDRESS_INPUT, "CURRENT_ADDRESS_INPUT should not be None")
            self.assertIsNotNone(self.page_class.STATE_DROPDOWN, "STATE_DROPDOWN should not be None")
            self.assertIsNotNone(self.page_class.CITY_DROPDOWN, "CITY_DROPDOWN should not be None")
            self.assertIsNotNone(self.page_class.SUBMIT_BUTTON, "SUBMIT_BUTTON should not be None")
