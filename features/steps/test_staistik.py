import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("../statistik.feature")


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@given("att användaren öppnar startsidan")
def open_start(page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/", wait_until="networkidle")
    page.wait_for_selector('[data-testid="catalog"]')


@when('användaren klickar på "Statistics"')
def click_statistics(page):
    page.click('[data-testid="statistics"]')


@then("visas statistik över favoriter")
def statistics_visible(page):
    page.wait_for_selector('[data-testid="statistics-view"]')