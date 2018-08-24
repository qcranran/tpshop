from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PersonalPage(BaseAction):
    login_enrolment_button = By.XPATH, "//*[@text='登录/注册']"

    def click_login_enrolment_button(self):
        self.click(self.login_enrolment_button)
