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
