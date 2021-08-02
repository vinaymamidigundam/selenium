from selenium import webdriver
import time

browser = webdriver.Chrome('/home/vinay/selenium/chromedriver')

browser.get('https://www.youtube.com/')
print(browser.title)
try:
    assert "YouTube" == browser.title
except AssertionError:
    print(f"Page title not matched with expected title, Actual title {browser.title} But expected title is {'YouTube'}")

browser.maximize_window()
time.sleep(3)
browser.minimize_window()
time.sleep(3)
browser.maximize_window()
time.sleep(3)
browser.close()