from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    phone_num = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/edit_phone_num']"
    password = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/edit_password']"
    login_button = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/btn_login']"

    def input_phone_num(self, text):
        self.input(self.phone_num, text )

    def input_password(self,text):
        self.input(self.password,text)

    def click_login_button(self):
        self.click(self.login_button)

