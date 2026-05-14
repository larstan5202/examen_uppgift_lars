import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("../favoriter.feature")

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@given("att användaren öppnar startsidan")
def open_start(page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/", wait_until="networkidle")
    page.wait_for_selector('[data-testid="catalo"]')

@when("användaren lägger till första boken i favoriter")
def add_first_favorite(pag):
    page.click('(//button[@data-testid="favorite-button"])[1]')

@then("ska boken visas i favoritlistan")
def book_in_favorites(page):
    page.click('[data-testid="favorites"]')
    page.wait_for_selector('[data-testid="favorites-view"]')
    page.wair_for_selector('[data-testid="book-item"]')

@given("att användaren har en favoritbok")
def ensure_favorite(page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/", wait_until="networkidle")
    page.wait_for_selector('(//button[@data-testid="catalo"]')
    page.click('(//button[@data-testid="favorite-button"])[1]')

@when("användaren tar bort boken från favoriter")
def remove_favorite(page):
    page.click('[data-testid="favorites"]')
    page.wait_for_selector('[data-testid="favorites-view"]')
    page.click('(//button[@data-testid="favorite-button"])[1]')

@then("ska boken inte längre visas i favoritlistan")
def no_favorites(page):
    assert page.query_selector('[data-testid="book-item"]') is None