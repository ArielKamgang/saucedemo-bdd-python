"""BasePage : methodes communes à toutes les pages"""
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        StaleElementReferenceException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.config import DEFAULT_TIMEOUT

class BasePage:
    """ class principale utilisé par toute les autres classe"""
    def __init__(self,driver):
        self.driver = driver
        #Ignore les elements "stale"(page re-dessinée) et réessaie
        self.wait = WebDriverWait(
            driver,DEFAULT_TIMEOUT,
              ignored_exceptions=[StaleElementReferenceException,
                                  ElementClickInterceptedException])
    def find (self, locator) :
        """attend qu'element soit visible pius le renvoie""" 
        return self.wait.until(EC.visibility_of_element_located(locator)) 
    def find_all(self,locator) :
        """attend qu au moins un élement existe, puis renvoie la liste"""
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)   
    def click (self,locator) :
        """Clique des que l'élement est cliquable (réessaie si besoin) """
        def _click(driver):
            element = EC.element_to_be_clickable(locator)(driver) 
            if element:
                element.click()
                return True
            return False
        self.wait.until(_click)      
    def type(self,locator,text):
        """Vide le champ puis tape le texte"""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
    def get_text(self,locator):
        return self.find(locator).text
    
    def is_displayed(self,locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False
    @property
    def current_url(self) :
        return self.driver.current_url