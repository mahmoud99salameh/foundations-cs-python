from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
# chrome_options = Options()

# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)

# #open new tab
# def OpenTab():
#     driver.get('https://www.google.com')

# #close tab
# def CloseTab():
#     driver.close()

# #switch between tabs
# def SwitchTabs():
#     driver.switch_to.window(driver.window_handles[1])

# #display all tabs
# def DisplayAll():
#     # Open the first tab and navigate to a website
#     driver.get("https://www.google.com")

#     # Open a new tab
#     driver.execute_script("window.open('', '_blank');")

#     for handle in driver.window_handles:
#         driver.switch_to.window(handle)
#         print(f"Tab Title: {driver.title}, URL: {driver.current_url}")

# #nested tabs
# def NestedTabs():
#     # Open the first tab and navigate to a website
#     driver.get("https://www.example.com")

#     # Open a new tab and navigate to another website
#     driver.execute_script("window.open('', '_blank');")
#     driver.switch_to.window(driver.window_handles[1])
#     driver.get("https://www.google.com")

#     # Open a nested tab within the second tab
#     driver.execute_script("window.open('', '_blank');")
#     driver.switch_to.window(driver.window_handles[2])
#     driver.get("https://www.facebook.com")

class WebBrowser:
    def __init__(self):
        self.tabs = {}  # Dictionary to store tabs
        self.tab_order = []  # List to maintain the order of open tabs

    def open_tab(self, tab_id, url, title):#open tab details
        # Check if the tab is already open
        if tab_id in self.tabs:
            print(f"Tab '{tab_id}' is already open.")
            return

        # Create a new tab dictionary
        tab = {
            'url': url,
            'title': title,
            'active': False  # Initially, the tab is not active
        }

        # Add the tab to the dictionary and the order list
        self.tabs[tab_id] = tab
        self.tab_order.append(tab_id)

        print(f"Tab '{tab_id}' opened with URL: {url}")

    def close_tab(self, tab_id):#close tab details
        # Check if the tab is open
        if tab_id not in self.tabs:
            print(f"Tab '{tab_id}' is not open.")
            return

        # Remove the tab from the dictionary and the order list
        del self.tabs[tab_id]
        self.tab_order.remove(tab_id)

        print(f"Tab '{tab_id}' closed.")

    def activate_tab(self, tab_id):#activated tab 
        # Check if the tab is open
        if tab_id not in self.tabs:
            print(f"Tab '{tab_id}' is not open.")
            return

        # Deactivate all tabs
        for tab in self.tab_order:
            self.tabs[tab]['active'] = False

        # Activate the specified tab
        self.tabs[tab_id]['active'] = True

        print(f"Tab '{tab_id}' activated.")

    def display_tabs(self):#showing all tabs details
        # Display the open tabs and their details
        print("Open Tabs:")
        for tab_id in self.tab_order:
            tab = self.tabs[tab_id]
            status = "Active" if tab['active'] else "Inactive"
            print(f"{tab_id}: {tab['title']} ({tab['url']}) - {status}")

# Example Usage
browser = WebBrowser()

browser.open_tab(1, "https://www.google.com", "Example Page")
browser.open_tab(2, "https://www.python.org", "Python Official Site")
browser.open_tab(3, "https://www.github.com", "GitHub")

browser.activate_tab(1)

browser.display_tabs()