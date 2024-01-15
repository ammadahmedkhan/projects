from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    # create context to store multiple tab
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    page.wait_for_selector('//body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/button[1]').click()
    page.wait_for_timeout(20000)
    #To find total pages
    total_pages = context.pages
    print(len(total_pages))
    for i in total_pages:
        print(i)
        print(page.title())
browser.close()