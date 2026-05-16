from pytest_bdd import scenarios, given, then
from playwright.sync_api import expect

scenarios("../katalog.feature")

@given("att användaren är på startsidan")
def open_start(page):
    page.goto("https://tap-ht25-testverktyg.github.io/exam/", wait_until="domcontentloaded")

@then("visas bokkatalogen")
def katalog_visible(page):
    expect(page.locator("div.book-card")).to_be_visible()
