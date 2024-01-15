from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/')
    emailtxtbox = page.wait_for_selector('#email')
    emailtxtbox.type('asdms@gmail.com')
    butn = page.wait_for_selector('#enterimg')
    butn.click()
    #xpath selection and label contains drop down value
    page.select_option('//select[@id="Skills"]',label='Android')
    # radio button selection
    radio_btn = page.query_selector('//input[@value="Male"]')
    radio_btn.check()
    if radio_btn.is_checked():
        print('Pass')
    else:
        print ('Fail')
    #checkbox checked
    chk_bx = page.query_selector('//input[@value="Movies"]')
    chk_bx.check()
    if chk_bx.is_checked():
        print('Pass')
    else:
        print ('Fail')

    page.wait_for_timeout(20000)
    browser.close()
