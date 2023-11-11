import webbrowser
import os
from selenium import webdriver



#open normal tab
def OpenNewTab():
    webbrowser.open('https://spotify.com', new=2)
#close tab
def CloseTab():
        os.system('TASKKILL /F /IM safari.???')
#open tab with web driver
def OpenWithWebDriver():
      browser = webdriver.Safari()
      browser.get("https://spotify.com")
      
