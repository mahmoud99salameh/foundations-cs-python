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

class WebBrowser:
    def __init__(self):
        self.tabs = {}  # Dictionary to store tabs
        self.tab_order = []  # List to maintain the order of open tabs

    def open_tab(self, tab_id, url, title, parent_tab=None):
        # Check if the tab is already open
        if tab_id in self.tabs:
            print(f"Tab '{tab_id}' is already open.")
            return

        # Create a new tab dictionary
        tab = {
            'url': url,
            'title': title,
            'active': False,  # Initially, the tab is not active
            'subtabs': {}  # Dictionary to store subtabs
        }
        # Display the open tabs and their details
        print("Open Tabs:")
        for tab_id in self.tab_order:
            tab = self.tabs[tab_id]
            status = "Active" if tab['active'] else "Inactive"
            print(f"{tab_id}: {tab['title']} ({tab['url']}) - {status}")

 # Add the tab to the parent tab if provided, otherwise add it to the main dictionary
        if parent_tab:
            self.tabs[parent_tab]['subtabs'][tab_id] = tab
        else:
            self.tabs[tab_id] = tab
            self.tab_order.append(tab_id)

        print(f"Tab '{tab_id}' opened with URL: {url}")
# Example Usage
browser = WebBrowser()

browser.open_tab(1, "https://www.google.com", "Example Page")
browser.open_tab(2, "https://www.python.org", "Python Official Site")
browser.open_tab(3, "https://www.github.com", "GitHub")

browser.activate_tab(1)

browser.display_tabs()
