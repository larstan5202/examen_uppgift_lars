import pytest
from pytest_bdd import scenarios, given when

scenarios("../navigering.feature")

@pytets.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@given
def open_start(page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/", wait_until="networkidl")
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