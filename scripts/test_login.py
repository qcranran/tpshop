from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login(self):
        self.page.home.click_mine()
        self.page.personal.click_login_enrolment_button()
        self.page.login.input_phone_num("13800138006")
        self.page.login.input_password("123456")
        self.page.login.click_login_button()