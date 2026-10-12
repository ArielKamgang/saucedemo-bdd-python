"""Hookd behave : executés automatiquement autour des scénarios."""
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.driver_factory import create_driver

def before_all(context):
    """une seul fois au debut: lire l'option headless."""
    context.headless = context.config.userdata.getbool("headless", False)

def before_scenario(context, scenario):
    """Avant Chaque scenario : un Chrome neuf + les Pages Objects."""
    context.driver = create_driver(context.headless)
    context.login_page = LoginPage(context.driver)
    context.inventory_page = InventoryPage(context.driver)

def After_scenario(context, scenario):
    """Apres cheaque sceanrio : fermer Chrome, même en cas d'échec"""
    context.driver.quit()
