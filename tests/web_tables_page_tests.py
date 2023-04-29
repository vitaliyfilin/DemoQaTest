import allure

from pages.web_tables_page import WebTablesPage
from tests.base_test import BaseTest


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("DemoQA tests")
@allure.feature("Web table tests")
class TestWebTablesPage(BaseTest):
    page_class = WebTablesPage
    page_url = 'https://demoqa.com/webtables'

    @allure.description("create record")
    @allure.title("Create new record and validate it's created")
    @allure.story("As a user I want to be able to create new record")
    def test_create_new_record(self):
        self.page_class.create_new_record(
            self.page,
            'John',
            'Doe',
            'john.doe@example.com',
            '25',
            '10000',
            'Software Engineer'
        )

        assert self.page_class.is_record_created(
            self.page,
            'John',
            'Doe',
            '25',
            'john.doe@example.com',
            '10000',
            'Software Engineer'
        )

    @allure.description("edit record")
    @allure.title("Edit existing record and validate it's edited")
    @allure.story("As a user I want to be able to edit existing record")
    def test_edit_existing_record(self):
        self.page_class.edit_record(
            self.page,
            'cierra@example.com',
            'Salary',
            '20000'
        )

        assert self.page_class.is_record_edited(
            self.page,
            'cierra@example.com',
            '20000'
        )

    @allure.description("delete record")
    @allure.title("Delete existing record and validate it's deleted")
    @allure.story("As a user I want to be able to delete existing record")
    def test_delete_existing_record(self):
        self.page_class.delete_record(self.page, 'cierra@example.com')
        assert self.page_class.is_record_deleted(self.page, 'cierra@example.com')
