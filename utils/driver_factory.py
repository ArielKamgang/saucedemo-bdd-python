"""Creation du navigateur Chrome avec ou sans fenetre"""
from selenium import webdriver

def create_driver(headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new") # sans fenetre (utile en CI)
    options.add_argument("--window-size=1920,1080")
    #Desactive le popup "mot de passe compromis" de Chrome
    options.add_experimental_option("prefs",{
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,


    })
    return webdriver.Chrome(options=options)