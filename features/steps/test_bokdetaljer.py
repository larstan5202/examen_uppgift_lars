# TESTAR ÄNDRINGEN
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect

scenarios("../bokdetaljer.feature")

@given("att användaren är på startsidan")
def open_start(page):
    page.goto(
    "https://tap-ht25-testverktyg.github.io/exam/index.html",
    wait_until="domcontentloaded"
)

page.set_extra_http_headers({"User-Agent": "Mozilla/5.0"})
page.wait_for_selector("div.book-card", timeout=15000)


@when("användaren klickar på en bok")
def click_book(page):
    page.locator("div.book-card").first.click()

@then("visas bokdetaljer")
def details_visible(page):
    expect(page.locator("div.book-details")).to_be_visible()
