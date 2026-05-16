# TESTAR ÄNDRING
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect

scenarios("../favoriter.feature")

@given("att användaren är på startsidan")
def open_start(page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/index.html", wait_until="domcontentloaded")

@when("användaren lägger till en bok i favoriter")
def add_favorite(page):
    page.locator("div.book-card").first.click()
    page.locator('[data-testid="add-favorite"]').click()

@then("visas boken i favoritlistan")
def favorite_list(page):
    page.locator('[data-testid="favorites"]').click()
    expect(page.locator("div.book-card")).to_be_visible()

@when("användaren tar bort en bok från favoriter")
def remove_favorite(page):
    page.locator('[data-testid="favorites"]').click()
    page.locator('[data-testid="remove-favorite"]').first.click()

@then("är favoritlistan tom")
def empty_favorites(page):
    expect(page.locator("div.book-card")).to_have_count(0)
