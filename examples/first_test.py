from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#1 ouvrir 
driver = webdriver.Chrome()

try :
    #2 aller sur le site
    driver.get("https://www.saucedemo.com/")
    #3 Trouver + Agir
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    #4 Cliquer sur login
    driver.find_element(By.ID,"login-button").click()
    # attendre (max 10s)
    wait = WebDriverWait(driver, 10)

    title= wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']")))
    #6 Verifier
    assert title.text == "Products", f"Titre inattendu : {title.text}"
    print("Test OK : connection reussi")
   

finally:
    #7 toujours fermer le navigateur meme s il echoue
    driver.quit()
