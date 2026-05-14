import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("../bokdetaljer.feature")


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@given("att användaren öppnar startsidan")
def open_start(page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/", wait_until="networkidle")
    page.wait_for_selector('[data-testid="catalog"]')


@when("användaren klickar på första boken")
def click_first_book(page):
    page.click('(//div[@data-testid="book-item"])[1]')


@then("visas en dialog med bokinformation")
def dialog_visible(page):
    page.wait_for_selector('[role="dialog"]')