from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    options = Options()
    options.add_argument("--headless=new")
    service = Service(ChromeDriverManager().install())
    context.browser = webdriver.Chrome(service=service, options=options)

def after_all(context):
    context.browser.quit()

