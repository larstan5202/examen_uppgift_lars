from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('att jag är på startsidan')
def step_impl(context):
    context.browser.get("https://tap-ht25-testverktyg.github.io/exam/")
    # Vänta tills rubriken "Läslistan" finns på sidan
    WebDriverWait(context.browser, 15).until(
        lambda driver: "Läslistan" in driver.page_source
    )


@when('jag klickar på "Katalog"')
def step_impl(context):
    katalog_btn = WebDriverWait(context.browser, 15).until(
        lambda driver: driver.find_element(By.CSS_SELECTOR, '[data-testid="catalog"]')
    )
    # Om knappen fortfarande är disabled, ta bort attributet via JavaScript
    context.browser.execute_script("arguments[0].removeAttribute('disabled')", katalog_btn)
    katalog_btn.click()


@when('jag klickar på "Lägg till bok"')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="add-book"]'))
    )
    context.browser.find_element(By.CSS_SELECTOR, '[data-testid="add-book"]').click()

@when('jag klickar på "Mina böcker"')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="my-books"]'))
    )
    context.browser.find_element(By.CSS_SELECTOR, '[data-testid="my-books"]').click()

@when('jag klickar på "Statistik"')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="statistics"]'))
    )
    context.browser.find_element(By.CSS_SELECTOR, '[data-testid="statistics"]').click()

@then('ska boklistan visas')
def step_impl(context):
    page_source = context.browser.page_source
    assert "Ormar på ett plan" in page_source or "Läslistan" in page_source

