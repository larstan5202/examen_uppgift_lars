import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("../navigering.feature")

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@given("att användaren är på startsidan")
def open_start(page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/", wait_until="networkidle")
    page.wait_for_selector('[data-testid="catalog"]')

@when('användaren klickar på "Favorites"')
def click_favorites(page):
    page.click('[data-testid="favorites"]')

@then("visas favoritvyn")
def favorites_view(page):
    page.wait_for_selector('[data-testid="favorites-view"]')

@when('användaren klickar på "Statistics"')
def click_statistics(page):
    page.click('[data-testid="statistics"]')

@then("visas statistikvyn")
def statistics_view(page):
    page.wait_for_selector('[data-testid="statistics-view"]')
