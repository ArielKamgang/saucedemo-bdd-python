from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import PASSWORD

def test_login_ok():
    driver = webdriver.Chrome()
    try :
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", PASSWORD)
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_loaded(), "La page Products n'est pas affichée"
        print(f"Test OK : login réussi, {inventory_page.product_count()} produit affichés")
    finally :
        driver.quit()

def test_login_wrong_password():
    driver = webdriver.Chrome()
    try :
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard","wrong")
        message = login_page.error_message()
        assert "do not match" in message, f"Message inattendu : {message}"
        print("TEST OK : mauvais mot de passe refusé")
    finally :
        driver.quit()

if __name__ == "__main__":
    test_login_ok()
    test_login_wrong_password()
