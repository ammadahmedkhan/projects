from playwright.sync_api import  sync_playwright
with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')
    table = page.wait_for_selector('//table[@id="customers"]')
    tr = table.query_selector_all('tr')
    print(len(tr))
    td = table.query_selector_all('td')
    print(len(td))
    for row in tr:
        cells = row.query_selector_all('td')
        for cell in cells:
            
    page.wait_for_timeout(2000)