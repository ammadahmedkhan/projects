from playwright.sync_api import sync_playwright
with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    page.select_option('//select[@id="Skills"]',label='Adobe Photoshop')
    radio = page.query_selector('//body/section[@id="section"]/div[1]/div[1]/div[2]/form[1]/div[5]/div[1]/label[2]/input[1]')
    radio.check()
    if radio.is_checked():
        print("Pass")
    else:
        print("Fail")

        chk = page.query_selector('//input[@id="checkbox2"]')
        chk.check()
    page.wait_for_timeout(7000)