from playwright.sync_api import sync_playwright
with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    page.wait_for_selector('//a[contains(text(),"SwitchTo")]').hover()
    page.wait_for_selector('//a[contains(text(),"Windows")]').click()
    page.wait_for_timeout(2000)