from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test = 'title']")
    ITEMS = (By.CSS_SELECTOR, "[data-test = 'inventory-item']")

    def title(self):
        return self.get_text(self.TITLE)

    def is_loaded(self):
        return "inventory.html" in self.current_url and self.title() == "Products"

    def product_count(self):
        return len(self.find_all(self.ITEMS))
