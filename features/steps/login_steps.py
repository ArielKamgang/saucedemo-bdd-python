"""Steps du login : chaque @given/@when/@then correspond à une phrase Gherkin."""
from behave import given, then, when


import utils.step_types # noqa: F401(active le type{..:Text})

@given("I am on the login page")
def step_open_login(context):
    context.login_page.open()

@when('I log in as "{username:Text}" with password "{password:Text}"')
def step_login(context, username, password):
    context.login_page.login(username, password)

@then("I should see the products page")
def step_products_page(context):
    assert context.inventory_page.is_loaded(), \
        f"Page produits attendue, URL actuelle : {context.driver.current_url}"

@then('I should see the login error "{message}"')
def step_login_error(context,message):
    actual = context.login_page.error_message()
    assert actual == message, f"Attendu : '{message}' | Obtenu : '{actual}' "
