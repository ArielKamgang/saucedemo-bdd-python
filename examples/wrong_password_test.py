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
    driver.find_element(By.ID, "password").send_keys("wrong")
    #4 Cliquer sur login
    driver.find_element(By.ID,"login-button").click()
    # attendre (max 10s)
    wait = WebDriverWait(driver, 10)
    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='error']")))

    #6 Verifier

    print("Message du Site :", error.text)
    assert "do not match" in error.text, f"Message inattendu : {error.text}"
    print(" Test OK : le login avec mauvais mot de passe est bien refusé")


finally:
    #7 toujours fermer le navigateur meme s il echoue
    driver.quit()
