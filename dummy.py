from playwright.sync_api import sync_playwright
#import synch from library
with sync_playwright() as p:
# function import for playwright
browser = p.chromium.launch(headless=False)
# browser defination and launching
page = browser.new_page()
page.goto('https://hris.netsoltech.com/#/login?returnUrl=%2F')
print('chrome launch successfull')
