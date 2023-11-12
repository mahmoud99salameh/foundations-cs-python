from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
import json
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

      def OpenTab(self, tab_id, url, title, parent_tab=None):
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

      def CloseTab(self, tab_id):
        # Check if the tab is open
        if tab_id not in self.tabs:
            print(f"Tab '{tab_id}' is not open.")
            return

        # Remove the tab from the dictionary and the order list
        if tab_id in self.tab_order:
            self.tab_order.remove(tab_id)
        else:
            # If the tab is a subtab, remove it from the parent tab's subtabs
            parent_tab_id = [parent for parent, tab in self.tabs.items() if tab_id in tab['subtabs']]
            if parent_tab_id:
                parent_tab_id = parent_tab_id[0]
                del self.tabs[parent_tab_id]['subtabs'][tab_id]

        print(f"Tab '{tab_id}' closed.") 
      def ActivateTab(self, tab_id):
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
      def DisplayTabs(self, tab_id=None, level=0):
        # Display the open tabs and their details
        if tab_id is None:
            tabs_to_display = self.tab_order
        else:
            tabs_to_display = [tab_id]

        for tab_id in tabs_to_display:
            tab = self.tabs[tab_id]
            status = "Active" if tab['active'] else "Inactive"
            print("  " * level + f"{tab_id}: {tab['title']} ({tab['url']}) - {status}")

            # Display subtabs recursively
            self.display_tabs(tab_id=tab_id, level=level + 1)
      def ClearAllTabs(self):
        # Clear all tabs
        self.tabs = {}
        self.tab_order = []
        print("All tabs cleared.")
      def SaveTabs(self, filename="tabs.json"):
        # Save tabs to a JSON file
        with open(filename, 'w') as file:
            json.dump({'tabs': self.tabs, 'tab_order': self.tab_order}, file)
        print(f"Tabs saved to {filename}.")
      def ImportTabs(self, filename="tabs.json"):
        # Import tabs from a JSON file
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            self.tabs = data.get('tabs', {})
            self.tab_order = data.get('tab_order', [])
            print(f"Tabs imported from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON in {filename}.")
# Example Usage
browser = WebBrowser()
browser.OpenTab(1, "https://www.google.com", "Google Page")
browser.OpenTab(2, "https://www.python.org", "Python Official Site")
browser.OpenTab(3, "https://www.github.com", "GitHub")
browser.OpenTab(4, "https://www.subtab.com", "Subtab", parent_tab=1)
browser.OpenTab(5, "https://www.subsubtab.com", "SubSubtab", parent_tab=4)
browser.DisplayTabs()
browser.ActivateTab(2)
browser.DisplayTabs()
browser.ClearAllTabs(1)
browser.DisplayTabs()
browser.SaveTabs()
browser.ImportTabs()