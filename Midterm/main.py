from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#open new tab
def OpenTab():
    driver.get('https://www.google.com')

#close tab
def CloseTab():
    driver.close()

#switch between tabs
def SwitchTabs():
    driver.switch_to.window(driver.window_handles[1])

#display all tabs
def DisplayAll():
    # Open the first tab and navigate to a website
    driver.get("https://www.google.com")

    # Open a new tab
    driver.execute_script("window.open('', '_blank');")

    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        print(f"Tab Title: {driver.title}, URL: {driver.current_url}")

#nested tabs
def NestedTabs():
    # Open the first tab and navigate to a website
    driver.get("https://www.example.com")

    # Open a new tab and navigate to another website
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.google.com")

    # Open a nested tab within the second tab
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get("https://www.facebook.com")
