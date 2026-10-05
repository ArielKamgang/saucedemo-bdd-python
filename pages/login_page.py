from selenium.webdriver.common.by import By 
from pages.base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage): #LOGINPage Hèrite de BasePage
    #--- Locators ---
    USENAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test = 'error']")
    #--- Action ---
    def open(self):
        self.driver.get(BASE_URL)

    def login(self,username,password):
        self.type(self.USENAME,username)
        self.type(self.PASSWORD,password)
        self.click(self.LOGIN_BUTTON)
    def error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    