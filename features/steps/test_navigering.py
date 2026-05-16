from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect

scenarios("../navigering.feature")

@given("att användaren är på startsidan")
def open_start(page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/index.html", wait_until="domcontentloaded")

@when('användaren klickar på "Favorites"')
def click_favorites(page):
    page.locator('[data-testid="favorites"]').click()

@then("visas favoritvyn")
def favorites_view(page):
    expect(page.locator("div.book-card")).to_be_visible()

@when('användaren klickar på "Statistics"')
def click_statistics(page):
    page.locator('[data-testid="statistics"]').click()

@then("visas statistikvyn")
def statistics_view(page):
    expect(page.locator("div.statistics")).to_be_visible()
