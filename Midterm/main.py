import webbrowser
import os
from selenium import webdriver


browser = webdriver.Safari()
#open normal tab
def OpenNewTab():
    webbrowser.open('https://spotify.com', new=2)
#close tab
def CloseSafari():
        os.system('TASKKILL /F /IM safari.???')
#open tab with web driver
def OpenWithWebDriver():
      browser.get("https://spotify.com")
      
def CloseTab():
      browser.close()