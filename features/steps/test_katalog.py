import pytest
from pytest_bdd import scenarios, given, then

scenarios("../katalog.feature")

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@given("att användaren är på startsidan")
def open_start(page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/", wait_until="networkidle")
    page.wait_for_selector('[data-testid="catalog"]')

@then("visas bokkatalogen")
def katalog_visible(page):
    page.wait_for_selector('[data-testid="catalog"]')
